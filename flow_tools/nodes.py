from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langchain.prompts.prompt import PromptTemplate

from typing_extensions import Dict, List
import operator
from typing import Annotated, Literal

import json
import re
import pyaudio



# Fonction pour générer une réponse avec OpenAI
def model_query(llm, prompt_template, inputs:dict) :
    """
    Extrait interroge un llm à partir d'un prompt dynamique
    
    Args:
        llm (model): model extrait à partir de langchain
        prompt_template (text): prompt dynamique 
        inputs (dict) : dictionnaire des pramètres utilisés pour enrichir le prompt
    
    Returns:
        response.content: Réponse sans métadata.
    """
    # Creation du template
    summary_prompt_template = PromptTemplate(
        input_variables=[v for v in inputs.keys()], template=prompt_template
    )


    chain = summary_prompt_template | llm 
    response = chain.invoke(input=inputs)
    return response.content


def extract_list_from_text(text):
    """
    Extrait une liste à partir d'un texte contenant du JSON entre backticks
    
    Args:
        text (str): Texte contenant le JSON entre backticks
    
    Returns:
        list: Liste extraite du JSON
    """
    try:
        # Extraire le contenu JSON entre les backticks
        json_match = re.search(r'```json\s*([\s\S]*?)\s*```', text)
        if not json_match:
            raise ValueError("No JSON content found between backticks")
        
        json_content = json_match.group(1)
        
        # Parser le contenu JSON directement en liste
        questions_list = json.loads(json_content)
        
        return questions_list
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return []
    

def from_text_to_speech(text, voice="ash"):
    """
    Lit un texte avec la voix de ash
    
    Args:
        text (str): Texte contenant le texte à lire
    
    Returns:

    """
    return 0
    client = OpenAI()
    stream = pyaudio.PyAudio().open(format=8,
                channels=1,
                rate=24_000,
                output=True)
    # Stream et client seront à passer dans le satet
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=text,
        response_format="pcm"
    ) as response:
        for chunk in response.iter_bytes(1024):
            stream.write(chunk)

## Definition du state du flow
class Interview_State(Dict) :
    """
    Classe représentant l'état d'un entretien,  les questions posées, 
    les réponses fournies, ainsi que le CV et la description du poste et les infos sur l'entreprise
    """
    questions: List[str] = []
    responses: List[str] = []
    resume: str = ""
    job_description: str = ""
    infos_firm: Annotated[list, operator.add]

## Defintition des noeuds
class Flow :
    def __init__(self):
        # Init_models
        # Les api_ekys sont passées dans l'environnement
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.tavily_research_tool = TavilySearchResults(
            max_results=1,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=True,
        )
        


    def prepare_interview(self, interview_state) :
        """
        Description du noeud de création des questions.
        """
        prepare_interview_template = """
            given the following information about the job, Imagine a list of questions you can ask the candidate to see if he is suitable for the role, the answer must be a json array, exemple ['What is your experience in this field?', 'How many years of experience on data projects']  :
            {job_description}
        """
        print("inter")

        questions_to_the_candidate = model_query(llm=self.llm, prompt_template=prepare_interview_template, inputs={"job_description":interview_state["job_description"]})
    
        return {"questions": extract_list_from_text(questions_to_the_candidate)[:], "responses":[]}

    def question_to_candidate(self, interview_state) :
        """
        Description du noeud d'interrogation du candidat.
        """
    
        nb_reponses = len(interview_state["responses"])
        if len(interview_state["questions"]) <= nb_reponses:
            text_to_read = "No more question"
        else :
            text_to_read = interview_state["questions"][nb_reponses]

        #from_text_to_speech(text=text_to_read)     
        return None

    def candidate_response(self, interview_state) :
        """
        Description du noeud qui permet la reponse du candidat.
        """
    
        nb_reponses = len(interview_state["responses"])
        if len(interview_state["questions"]) <= nb_reponses:
            response = "I'll be waiting for news. Good bye"
        else :
            question = interview_state["questions"][nb_reponses]
            interview_template = """
                Your role is to be the candidate, your were asked the following question {question},
                and you must give a response based on the folowing resume {resume}
            """
            
            response = model_query(llm=self.llm, prompt_template=interview_template, inputs={"question": question, "resume": interview_state["resume"]})

        #from_text_to_speech(text=response, client=interview_state["client"], stream=interview_state["stream"], voice="shimmer")     
        return {"responses" : interview_state["responses"]+[response]}


    # Codnitionnal edge
    def test_end(self, interview_state) -> Literal["search_infos", "question_to_candidate"]:
        # Comparaions du nombre de questions et reponses 
        print("test_end : " , interview_state['responses'])
        if len(interview_state['responses']) >= len(interview_state['questions']) :
            print(f"___Test_end___ : \n {len(interview_state['responses'])} responses -> search_infos")
            # 50% of the time, we return Node 2
            return "search_infos"
        
        print(f"___Test_end___ : \n {len(interview_state['responses'])} responses -> question_to_candidate")
        # 50% of the time, we return Node 3
        return "question_to_candidate"


    def generate_cover_letter(self, interview_state) :
        """
        Description du noeud qui permet la rédaction de la lettre de motivation
        """
        
        transcription = ""
        for q, r in zip(
                    interview_state["questions"][:len(interview_state["responses"])],
                    interview_state["responses"],
                ):
            transcription += f"""QUESTION: {q}\nRESPONSE: {r}\n\n"""
        cover_letter_template = """
            As a senior candidate, imagine an interview where the recruiter asks the following questions, along with your corresponding answers:  
            {transcription}  

            Additionally, you have the following resume:  
            {resume}  
            And infos about the firm, you want to work in 
            {search_infos}

            Based on this information, write a compelling and concise cover letter that highlights your suitability for the position.  
            """
        cover_letter = model_query(llm=self.llm, prompt_template=cover_letter_template, inputs={"transcription": transcription, "resume": interview_state['resume'], "search_infos": interview_state['infos_firm']})
        print(f"___COVER_LETTER___ : \n {cover_letter}")

        return None


    def evaluate_candidate(self, interview_state) :
        """
        Description du noeud qui permet la rédaction de la lettre de motivation
        """
        transcription = ""
        
        for q, r in zip(
                    interview_state["questions"][:len(interview_state["responses"])],
                    interview_state["responses"],
                ):
            transcription += f"""QUESTION: {q}\nRESPONSE: {r}\n\n"""

        candidate_evaluation_prompt = """
            Based on the transcription of the interview of the candidate by a recruiter, how would you evaluate the candidate:
            {transcription}  
        """
        candidate_evaluation = model_query(llm=self.llm, prompt_template=candidate_evaluation_prompt, inputs={"transcription": transcription})
        print(f"___CANDIDATE_EVALUATION___ : \n {candidate_evaluation}")

        return None


    def modify_interview_state(self, state: Interview_State):
        # Ici, tu peux ajouter une interface (Streamlit, CLI, etc.)
        print("Modification de l'état en cours...")
        #user_input = input(f"Do you wish to modify the following answer ? {state['responses'][-1]} ")  # Remplace par une interface UI si nécessaire
        return None



    def search_infos(self, interview_state : Interview_State) :
        prompt_template = """
            given the following information about the job, can you extract the name of the firm, your answer must be as concise as possible  :
            {job_description}
        """

        firm_infos = model_query(llm=self.llm, prompt_template=prompt_template, inputs={"job_description":interview_state['job_description']})


        results=self.tavily_research_tool.invoke({"query": f"Can you get a description about {'firm_infos'}"})

        return {"infos_firm": [results[0]['content']]}