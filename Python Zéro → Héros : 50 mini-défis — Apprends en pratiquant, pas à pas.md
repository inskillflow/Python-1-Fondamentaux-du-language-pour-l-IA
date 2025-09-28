### 1) Afficher “Bonjour”

* Objectif : afficher un texte.
* Étapes : ouvre un notebook → écris `print("Bonjour")` → exécute.
* Indice : `print(...)` affiche à l’écran.
* Exemple attendu : `Bonjour`

### 2) Afficher ton prénom

* Objectif : afficher ton prénom.
* Étapes : remplace “Alice” par ton prénom.
* Indice : guillemets pour du texte.
* Exemple : `print("Haythem")`

### 3) Deux lignes d’affichage

* Objectif : afficher deux lignes.
* Étapes : deux `print(...)` l’un sous l’autre.
* Indice : chaque print fait une nouvelle ligne.
* Exemple :

  ```
  Bonjour
  Python
  ```

### 4) Calcul simple

* Objectif : afficher 2 + 3.
* Étapes : `print(2 + 3)`.
* Indice : pas de guillemets pour un nombre.
* Attendu : `5`

### 5) Texte + résultat

* Objectif : afficher `2+3=` puis le résultat.
* Étapes : `print("2+3=", 2+3)`.
* Indice : on peut passer plusieurs éléments à print.
* Attendu : `2+3= 5`

### 6) Variable nombre

* Objectif : créer une variable `x=7` et l’afficher.
* Étapes : `x = 7` puis `print(x)`.
* Indice : `=` assigne une valeur.
* Attendu : `7`

### 7) Variable texte

* Objectif : `nom = "Nadia"` puis afficher.
* Étapes : créer puis `print(nom)`.
* Indice : guillemets pour le texte.
* Attendu : `Nadia`

### 8) Addition avec variables

* Objectif : `a=4`, `b=6`, afficher `a+b`.
* Étapes : créer, puis `print(a+b)`.
* Indice : variables numériques s’additionnent.
* Attendu : `10`

### 9) Lire un prénom (input)

* Objectif : demander un prénom et l’afficher.
* Étapes : `nom = input("Prénom: ")`; `print("Bonjour", nom)`.
* Indice : `input` lit au clavier.
* Attendu : `Bonjour Karim`

### 10) Somme de deux nombres (input)

* Objectif : lire deux nombres et afficher la somme.
* Étapes : `a = int(input(...))`; `b = int(input(...))`; `print(a+b)`.
* Indice : `int(...)` transforme en entier.
* Attendu : si 3 et 8 → `11`

### 11) Multiplication

* Objectif : lire un nombre et afficher ×10.
* Étapes : `n=int(input(...))`; `print(n*10)`.
* Indice : `*` multiplie.
* Attendu : si 4 → `40`

### 12) Aire d’un rectangle

* Objectif : lire largeur/hauteur et afficher `L*H`.
* Étapes : `L=int(input(...))`; `H=int(input(...))`; `print(L*H)`.
* Indice : produit.
* Attendu : 5 et 3 → `15`

### 13) Concaténer texte

* Objectif : afficher `Bonjour, NOM !`.
* Étapes : `nom=input(...)`; `print("Bonjour, " + nom + "!")`.
* Indice : `+` colle des textes.
* Attendu : `Bonjour, Aya!`

### 14) Longueur d’un mot

* Objectif : lire un mot et afficher sa longueur.
* Étapes : `mot=input(...)`; `print(len(mot))`.
* Indice : `len(...)` donne la longueur.
* Attendu : “chat” → `4`

### 15) Majuscules

* Objectif : lire un mot et l’afficher en MAJ.
* Étapes : `mot=input(...)`; `print(mot.upper())`.
* Indice : `.upper()`.
* Attendu : “salut” → `SALUT`

### 16) Minuscules

* Objectif : lire et afficher en minuscules.
* Étapes : `.lower()`.
* Indice : méthodes de chaîne.
* Attendu : “BonJour” → `bonjour`

### 17) Remplacer un caractère

* Objectif : remplacer “a” par “@”.
* Étapes : `s=input(...)`; `print(s.replace("a","@"))`.
* Indice : `.replace(ancien, nouveau)`.
* Attendu : “salade” → `s@l@de`

### 18) Extraire première lettre

* Objectif : afficher la première lettre d’un mot.
* Étapes : `mot=input(...)`; `print(mot[0])`.
* Indice : indices commencent à 0.
* Attendu : “Python” → `P`

### 19) Dernière lettre

* Objectif : afficher la dernière lettre.
* Étapes : `print(mot[-1])`.
* Indice : `-1` = dernier.
* Attendu : “chat” → `t`

### 20) Échanger prénom/nom

* Objectif : lire prénom et nom, afficher “Nom Prénom”.
* Étapes : deux `input`; `print(nom, prenom)`.
* Indice : l’ordre compte.
* Attendu : `Dupont Sara`

### 21) Pair ou impair (if)

* Objectif : dire si un nombre est pair.
* Étapes : `n=int(input(...))`; `if n%2==0: ... else: ...`
* Indice : `%` est le reste.
* Attendu : 6 → “pair”

### 22) Positif, négatif ou zéro

* Objectif : classer un nombre.
* Étapes : `if n>0`, `elif n<0`, `else`.
* Indice : conditions en chaîne.
* Attendu : -3 → “négatif”

### 23) Comparer deux nombres

* Objectif : afficher le plus grand.
* Étapes : lire a,b → if/elif/else.
* Indice : `>` `<` `==`.
* Attendu : 7 et 2 → “7”

### 24) Mot de passe simple

* Objectif : vérifier si `mdp=="python"`.
* Étapes : `mdp=input(...)`; if égal → “OK” sinon “Non”.
* Indice : égalité `==`.
* Attendu : “python” → OK

### 25) Compter de 1 à N (boucle for)

* Objectif : afficher 1,2,...,N.
* Étapes : `N=int(input(...))`; `for i in range(1, N+1): print(i)`
* Indice : `range(debut, fin_exclu)`.
* Attendu : N=5 → 1..5

### 26) Somme de 1 à N

* Objectif : calculer la somme 1+...+N.
* Étapes : `s=0`; boucle `for`; ajoute `i`.
* Indice : accumulateur.
* Attendu : N=4 → `10`

### 27) Table de multiplication (N)

* Objectif : afficher N×1 à N×10.
* Étapes : boucle 1..10; print.
* Indice : `i` change à chaque tour.
* Attendu : N=3 → 3,6,...,30

### 28) Répéter un mot

* Objectif : afficher un mot 5 fois.
* Étapes : `mot=input(...)`; boucle `for` 5 tours.
* Indice : `range(5)`.
* Attendu : 5 lignes identiques

### 29) Compter les voyelles

* Objectif : compter aeiou dans un mot.
* Étapes : boucle sur lettres; si lettre dans “aeiou”.
* Indice : `in` vérifie la présence.
* Attendu : “salut” → 2

### 30) Deviner un nombre (while simple)

* Objectif : tant que réponse ≠ 7, redemander.
* Étapes : `n=int(input(...))`; `while n!=7: re-demander`.
* Indice : `while` = tant que.
* Attendu : finit quand 7.

### 31) Saisie jusqu’à “stop”

* Objectif : lire des mots jusqu’à écrire “stop”.
* Étapes : `while True`; break si “stop”.
* Indice : `break` sort de la boucle.
* Attendu : s’arrête sur “stop”.

### 32) Minimum de 3 nombres

* Objectif : afficher le plus petit de 3.
* Étapes : lire a,b,c; `m=a`; comparer et mettre à jour.
* Indice : conditions successives.
* Attendu : 9,2,5 → `2`

### 33) Liste de 3 prénoms

* Objectif : créer une liste et l’afficher.
* Étapes : `noms=["Ali","Mina","Zoe"]`; `print(noms)`.
* Indice : crochets `[]`.
* Attendu : `["Ali","Mina","Zoe"]`

### 34) Accéder à un élément de liste

* Objectif : afficher le 2e prénom.
* Étapes : `print(noms[1])`.
* Indice : index 0,1,2…
* Attendu : `Mina`

### 35) Ajouter dans une liste

* Objectif : ajouter un prénom saisi.
* Étapes : `x=input(...)`; `noms.append(x)`; afficher.
* Indice : `.append(...)`.
* Attendu : liste avec un 4e prénom.

### 36) Parcourir une liste

* Objectif : afficher chaque prénom.
* Étapes : `for p in noms: print(p)`.
* Indice : boucle sur la liste.
* Attendu : un prénom par ligne.

### 37) Moyenne de 3 notes

* Objectif : calculer la moyenne.
* Étapes : lire 3 entiers; `m=(a+b+c)/3`; afficher.
* Indice : division `/`.
* Attendu : 10,12,14 → `12.0`

### 38) Formater l’affichage

* Objectif : afficher “Moyenne: 12.00”.
* Étapes : `print(f"Moyenne: {m:.2f}")`.
* Indice : f-string et `:.2f`.
* Attendu : deux décimales.

### 39) Tronquer / convertir float→int

* Objectif : montrer `int(12.9)`.
* Étapes : `x=float(input(...))`; `print(int(x))`.
* Indice : `int()` coupe la partie décimale.
* Attendu : 12.9 → `12`

### 40) Compter jusqu’à dépasser 100

* Objectif : additionner des nombres jusqu’à somme>100.
* Étapes : `s=0`; `while s<=100: s+=int(input(...))`; print s.
* Indice : condition dans while.
* Attendu : s’arrête quand s>100.

### 41) Mot palindrome (simple)

* Objectif : dire si mot == mot inversé.
* Étapes : `mot=input(...)`; `mot[::-1]`.
* Indice : slicing `[start:stop:step]`.
* Attendu : “kayak” → oui.

### 42) Compter lettres spécifiques

* Objectif : compter “e” dans une phrase.
* Étapes : `phrase=input(...)`; `phrase.count("e")`.
* Indice : `.count(...)`.
* Attendu : entier.

### 43) Trouver le max dans une liste

* Objectif : lire N, puis N nombres, trouver max.
* Étapes : construire liste; `m = max(liste)`.
* Indice : fonction `max`.
* Attendu : affiche le maximum.

### 44) Tri simple (sans algorithme complexe)

* Objectif : trier une liste de prénoms.
* Étapes : `noms.sort()`; afficher.
* Indice : `.sort()` modifie sur place.
* Attendu : ordre alphabétique.

### 45) Dictionnaire très basique

* Objectif : créer `perso={"nom":"Ali","age":20}`; afficher.
* Étapes : créer puis `print(perso["nom"])`.
* Indice : clés entre guillemets.
* Attendu : `Ali`

### 46) Ajouter une clé au dict

* Objectif : `perso["ville"]="Montréal"`.
* Étapes : ajouter puis afficher.
* Indice : même syntaxe qu’une variable.
* Attendu : dict avec “ville”.

### 47) Vérifier la présence d’une clé

* Objectif : tester si “age” est dans le dict.
* Étapes : `if "age" in perso: ...`.
* Indice : `in` avec dict → clés.
* Attendu : affiche “clé trouvée”.

### 48) Lire un fichier (optionnel si colab)

* Objectif : lire `data.txt` et afficher son contenu.
* Étapes : créer un petit fichier → `open("data.txt").read()`.
* Indice : `with open(..., "r") as f: print(f.read())`.
* Attendu : contenu affiché.

### 49) Écrire un fichier

* Objectif : écrire “Bonjour” dans `out.txt`.
* Étapes : `with open("out.txt","w") as f: f.write("Bonjour")`.
* Indice : mode `"w"` écrit.
* Attendu : fichier créé.

### 50) Petite fonction

* Objectif : créer une fonction `double(n)` qui renvoie `2*n`.
* Étapes : `def double(n): return 2*n`; tester avec `print(double(5))`.
* Indice : `def` définit une fonction.
* Attendu : `10`

