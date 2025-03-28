Voici une présentation commentée et illustrée des définitions extraites du chapitre 1 "Dénombrement". Chaque concept est expliqué avec des exemples pour faciliter la compréhension.

---

## 1.1 PERMUTATIONS

**DÉFINITION 1.**  
Le nombre de permutations de \( n \) éléments distincts est le nombre de manières de les ordonner. On le note \( P_n \) et on a  
\[ P_n = n! = 1 \times 2 \times \cdots \times (n-2) \times (n-1) \times n \]

### Commentaire :
Les permutations concernent l'ordre des éléments. Par exemple, si nous avons trois lettres distinctes : A, B et C, les différentes façons de les ordonner sont : ABC, ACB, BAC, BCA, CAB, CBA. Ici, nous avons \( 3! = 6 \) permutations.

### Illustration :
- **Éléments :** A, B, C
- **Permutations :** 
  - ABC
  - ACB
  - BAC
  - BCA
  - CAB
  - CBA

---

## 1.2 ARRANGEMENTS

**DÉFINITION 3.**  
Le nombre d'arrangements de \( k \) éléments pris parmi \( n \) éléments distincts est le nombre de manières de choisir et d'ordonner ces \( k \) éléments. On le note \( A_k \) et on a  
\[ A_k = \frac{n!}{(n-k)!} \]

### Commentaire :
Les arrangements prennent en compte à la fois le choix et l'ordre des éléments. Par exemple, si nous avons 5 fruits (pomme, banane, cerise, datte, figue) et que nous voulons choisir et ordonner 3 d'entre eux, nous calculons \( A_3 \) comme suit :  
\[ A_3 = \frac{5!}{(5-3)!} = \frac{120}{2} = 60 \]

### Illustration :
- **Éléments :** Pomme, Banane, Cerise, Datte, Figue
- **Arrangements de 3 fruits :** 
  - Pomme, Banane, Cerise
  - Pomme, Cerise, Banane
  - Banane, Pomme, Cerise
  - ... (et ainsi de suite jusqu'à 60)

---

## 1.3 COMBINAISONS

**DÉFINITION 5.**  
Le nombre de combinaisons de \( k \) éléments parmi \( n \) est le nombre de manières de choisir ces \( k \) éléments sans les ordonner. On le note \( \binom{n}{k} \) et on a  
\[ \binom{n}{k} = \frac{n!}{k!(n-k)!} \]

### Commentaire :
Les combinaisons ne tiennent pas compte de l'ordre. Par exemple, si nous avons 4 couleurs (rouge, bleu, vert, jaune) et que nous voulons choisir 2 couleurs, les combinaisons possibles sont : rouge-bleu, rouge-vert, rouge-jaune, bleu-vert, bleu-jaune, vert-jaune. Ici, nous avons \( \binom{4}{2} = 6 \).

### Illustration :
- **Éléments :** Rouge, Bleu, Vert, Jaune
- **Combinaisons de 2 couleurs :** 
  - Rouge, Bleu
  - Rouge, Vert
  - Rouge, Jaune
  - Bleu, Vert
  - Bleu, Jaune
  - Vert, Jaune

---

## 1.4 PRINCIPES ADDITIF ET MULTIPLICATIF

**PROPOSITION 10.**  
On suppose qu'il y a \( N_1 \) TRUCS et \( N_2 \) MACHINS. On peut conclure qu'il y a \( N_1 + N_2 \) BIDULES.

### Commentaire :
Le principe additif s'applique lorsque nous avons plusieurs options distinctes. Par exemple, si nous avons 3 types de fruits (pomme, banane, cerise) et 2 types de légumes (carotte, brocoli), le total des choix est \( 3 + 2 = 5 \).

### Illustration :
- **Fruits :** 3 (Pomme, Banane, Cerise)
- **Légumes :** 2 (Carotte, Brocoli)
- **Total :** 5 (3 fruits + 2 légumes)

---

**PROPOSITION 12.**  
On suppose qu'il y a \( N_1 \) TRUCS et \( N_2 \) MACHINS. On peut conclure qu'il y a \( N_1 \times N_2 \) paires (TRUC, MACHIN).

### Commentaire :
Le principe multiplicatif s'applique lorsque nous combinons des choix. Par exemple, si nous avons 3 chemises et 2 pantalons, le nombre total de combinaisons de tenues est \( 3 \times 2 = 6 \).

### Illustration :
- **Chemises :** 3 (Rouge, Bleu, Vert)
- **Pantalons :** 2 (Noir, Beige)
- **Total des tenues :** 6 (Rouge-Noir, Rouge-Beige, Bleu-Noir, Bleu-Beige, Vert-Noir, Vert-Beige)

---

## 1.5 CARDINAL

**DÉFINITION 8.**  
Si \( E \) est un ensemble, on appelle cardinal de \( E \) et on note \( \text{card}(E) \) le nombre d'éléments de \( E \).

### Commentaire :
Le cardinal d'un ensemble est simplement le nombre d'éléments qu'il contient. Par exemple, si \( E = \{1, 2, 3, 4\} \), alors \( \text{card}(E) = 4 \).

### Illustration :
- **Ensemble :** \( E = \{1, 2, 3, 4\} \)
- **Cardinal :** \( \text{card}(E) = 4 \)

---
