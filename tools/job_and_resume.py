from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
import os


def extract_content_pdf(pdf_path):
    """
    Extrait le contenu d'un fichier PDF avec PyPDFLoader de LangChain
    """
    print(f"Extraction du contenu du PDF: {pdf_path}")
    
    # Chargement du document PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    
    print(f"Nombre de pages extraites: {len(pages)}")
    
    return pages

def split_chunks(pages, taille_chunk=2000, chevauchement=500):
    """
    Découpe le contenu extrait en chunks pour un traitement plus efficace
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=taille_chunk,
        chunk_overlap=chevauchement,
        length_function=len
    )
    
    chunks = text_splitter.split_documents(pages)
    
    print(f"Nombre de chunks créés: {len(chunks)}")
    
    return chunks

def save_text(pages, nom_fichier="contenu_cours_proba.txt"):
    """
    Sauvegarde le contenu extrait dans un fichier texte
    """
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for page in pages:
            f.write(f"--- Page {page.metadata['page']} ---\n\n")
            f.write(page.page_content)
            f.write("\n\n")
    
    print(f"Contenu sauvegardé dans {nom_fichier}")

def create_vectorstore(pdf_path):
    """
    Crée une base de connaissances interrogeable à partir d'un PDF
    """
    # Chargement du PDF
    pages = extract_content_pdf(pdf_path)
    
    # Découpage en chunks
    chunks = split_chunks(pages)
    
    # Création des embeddings et de la base vectorielle
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    print(f"Base de connaissances créée avec {len(chunks)} chunks")
    
    return vectorstore

def question_to_vectorstore(vectorstore, question):
    """
    Interroge la base de connaissances avec une question
    """
    # Recherche des documents pertinents
    docs = vectorstore.similarity_search(question, k=5)
    
    # Création de la chaîne de question-réponse
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    
    # Génération de la réponse
    reponse = chain.run(input_documents=docs, question=question)
    
    return reponse, docs

