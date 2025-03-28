## Qu'est-ce qu'un arrangement ?

Un arrangement est une manière de choisir et d'ordonner un certain nombre d'éléments à partir d'un ensemble donné. Contrairement aux combinaisons, où l'ordre n'a pas d'importance, dans les arrangements, l'ordre des éléments est crucial. 

### Définition

Soit \( n \) le nombre total d'éléments distincts et \( k \) le nombre d'éléments à choisir et à ordonner. Le nombre d'arrangements de \( k \) éléments pris parmi \( n \) éléments distincts est donné par la formule :

\[
A_k = \frac{n!}{(n-k)!}
\]

où \( n! \) (factorielle de \( n \)) est le produit de tous les entiers de 1 à \( n \).

### Illustration

Prenons un exemple simple : imaginons que nous avons 5 livres distincts : A, B, C, D, et E. Si nous voulons savoir de combien de façons nous pouvons choisir et ordonner 3 de ces livres, nous utiliserons la formule des arrangements.

1. **Calculons \( A_3 \) pour \( n = 5 \)** :
   \[
   A_3 = \frac{5!}{(5-3)!} = \frac{5!}{2!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{2 \times 1} = 5 \times 4 \times 3 = 60
   \]

Il y a donc 60 façons de choisir et d'ordonner 3 livres parmi 5.

### Exercice proposé

**Exercice :**

Une compétition de chant a lieu avec 10 participants. Les 3 premiers (or, argent, bronze) seront récompensés. 

1. Combien de façons différentes peut-on attribuer les médailles aux 3 premiers participants ?
2. Si l'on décide de récompenser 5 participants (or, argent, bronze, et deux mentions honorables), combien de façons différentes peut-on attribuer ces récompenses ?

**Solution :**

1. Pour le premier cas, nous devons calculer \( A_3 \) pour \( n = 10 \) :
   \[
   A_3 = \frac{10!}{(10-3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720
   \]
   Il y a donc 720 façons d'attribuer les médailles aux 3 premiers participants.

2. Pour le second cas, nous devons calculer \( A_5 \) pour \( n = 10 \) :
   \[
   A_5 = \frac{10!}{(10-5)!} = \frac{10!}{5!} = 10 \times 9 \times 8 \times 7 \times 6 = 30240
   \]
   Il y a donc 30,240 façons d'attribuer les récompenses aux 5 participants.