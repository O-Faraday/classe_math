## DÉFINITION 25
La probabilité d'un événement \( A \) sachant qu'un événement \( B \) a eu lieu est notée \( P(A|B) \) et est définie par la formule :
\[
P(A|B) = \frac{P(A \cap B)}{P(B)}
\]

#### Exercice
**Exemple 26.**  
On veut calculer la probabilité qu'un jet de dé équilibré donne au moins un 2 sachant que le résultat est inférieur ou égal à 5.

---

## DÉFINITION 27
Deux événements \( A \) et \( B \) sont dits indépendants si :
\[
P(A \cap B) = P(A)P(B)
\]
Cela est équivalent à dire que :
\[
P(A|B) = P(A)
\]
On admet que si \( A \) et \( B \) sont indépendants, alors \( B \) et \( A \) le sont aussi.

#### Illustration
Considérons un tirage de cartes dans un jeu de 52 cartes. L'événement \( A \) est "tirer un cœur" et l'événement \( B \) est "tirer un roi". Ces événements sont indépendants car le fait de tirer un cœur n'affecte pas la probabilité de tirer un roi.

#### Exercice
**Exemple 28.**  
On tire une boule parmi 15 boules numérotées de 1 à 15. Les événements «le numéro tiré est pair» et «le numéro tiré est un multiple de 3» sont-ils indépendants ?

---

## DÉFINITION 29
Une partition de \( \Omega \) est un ensemble d'événements \( (A_1, \ldots, A_k) \) tel que :
1. Les événements \( (A_i) \) sont disjoints : \( \forall i,j \in \llbracket 1;k \rrbracket, A_i \cap A_j = \emptyset \)
2. Les événements \( (A_i) \) recouvrent \( \Omega \) : \( A_1 \cup A_2 \cup \ldots \cup A_k = \Omega \)

#### Illustration
Considérons un ensemble de résultats d'un lancer de dé. Les événements \( A_1 \) : "obtenir un nombre pair", \( A_2 \) : "obtenir un nombre impair" forment une partition de l'espace des résultats possibles {1, 2, 3, 4, 5, 6}.

---

## THÉORÈME 30
Soit \( (A_1, \ldots, A_k) \) une partition de \( \Omega \) avec \( \forall i \in \llbracket 1;k \rrbracket, P(A_i) \neq 0 \) et \( B \) un événement d'un espace probabilisé \( \Omega \). Alors :
\[
P(B) = \sum_{i=1}^{k} P(A_i \cap B) = \sum_{i=1}^{k} P(B|A_i)P(A_i)
\]

#### Illustration
Imaginons une urne contenant 3 boules rouges et 2 boules bleues. On peut partitionner l'espace des événements en \( A_1 \) : "tirer une boule rouge" et \( A_2 \) : "tirer une boule bleue". La probabilité de tirer une boule peut être calculée en utilisant la formule du théorème.

#### Exercice
**Exemple 31.**  
Dans une urne composée de 5 boules rouges et 4 boules jaunes, quelle est la probabilité de tirer 2 boules rouges d'affilée (utiliser un arbre de probabilités) ?

---

## Exercice 15
Un bijoutier vend des perles. Le tableau ci-dessous donne la répartition des perles selon leur forme et leur couleur :  

|               | Sphérique | Équilibrée | Baroque | Total |
|---------------|-----------|------------|---------|-------|
| Argentée      | 200       | 550        | 750     | 1500  |
| Noire         | 200       | 550        | 250     | 1000  |
| **Total**     | 400       | 1100       | 1000    | 2500  |

On note respectivement \( A, N, S, E, B \) les événements «la perle est Argentée/Noire/Sphérique/Équilibrée/Baroque». Les probabilités seront écrites sous forme de fraction irréductible.  

a) Calculer la probabilité des événements S et A.  
b) Traduire par une phrase l'événement \( S \cap A \) et calculer sa probabilité. Les événements S et A sont-ils indépendants ?  
c) Calculer \( P(N \cup E) \) et interpréter le résultat.  
d) Le bijoutier choisit une perle parmi les perles équilibrées. Calculer la probabilité que la perle soit noire.  
e) Calculer \( P(B) \) et traduire par une phrase.  

---

## Exercice 16
Pour contacter une compagnie d'assurances, deux possibilités sont offertes : rendez-vous en agence ou par téléphone. Le responsable du pôle « satisfaction » décide de réaliser une enquête afin de savoir si les client.e.s sont satisfait.e.s de leur accueil. À l'issue de l'enquête, les résultats sont les suivants :  
- 38% se sont rendu.e.s en agence  
- parmi les client.e.s qui se sont rendus en agence, 90% se sont déclaré.e.s satisfait.e.s de l'accueil  
- parmi les client.e.s qui ont téléphoné, 15% ne sont pas satisfait.e.s de l'accueil  

On interroge Lambda, une cliente ayant participé à l'enquête et on considère les événements suivants :  
A: «Lambda s'est rendue en agence». S: «Lambda est satisfaite». Les probabilités seront arrondies à \( 10^{-3} \) si nécessaire.  

a) Traduire les données (en pourcentage) de l'exercice en probabilités (éventuellement conditionnelles).  
b) Construire un arbre de probabilités permettant de représenter la situation.  
c) Calculer la probabilité que Lambda se soit rendue en agence et qu'elle ait été satisfaite de l'accueil.  
d) Montrer que \( P(S) = 0.869 \).  
e) Calculer \( P(A \cup S) \).  
f) Le responsable a pour objectif qu'il y ait moins de 12% des client.e.s non satisfait.e.s de l'accueil. Cet objectif est-il atteint ?  
g) Sachant que Lambda se dit satisfaite, quelle est la probabilité qu'elle se soit rendue en agence ?  
