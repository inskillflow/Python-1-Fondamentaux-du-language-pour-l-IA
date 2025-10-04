#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
50 EXERCICES PYTHON - VERSION SIMPLE POUR DÉBUTANTS
==================================================

Ce fichier contient les 50 exercices avec leurs corrections.
Format simple : pas de fonctions, juste le code direct.
Parfait pour les débutants qui veulent voir les solutions rapidement.

Auteur: Cours Python Fondamentaux
Date: 2025
"""

# ============================================================================
# SECTION 1 : BASES DE PYTHON (Exercices 1-10)
# ============================================================================

print("="*60)
print("SECTION 1 : BASES DE PYTHON (Exercices 1-10)")
print("="*60)

# EXERCICE 1 : Afficher "Bonjour"
print("\n--- Exercice 1 : Afficher 'Bonjour' ---")
print("Bonjour")

# Explication :
# print() affiche du texte à l'écran
# Les guillemets indiquent que c'est du texte


# EXERCICE 2 : Afficher ton prénom
print("\n--- Exercice 2 : Afficher ton prénom ---")
print("Haythem")  # Remplacez par votre prénom

# Explication :
# On peut utiliser des guillemets simples ' ou doubles "


# EXERCICE 3 : Deux lignes d'affichage
print("\n--- Exercice 3 : Deux lignes d'affichage ---")
print("Bonjour")
print("Python")

# Explication :
# Chaque print() crée une nouvelle ligne automatiquement


# EXERCICE 4 : Calcul simple
print("\n--- Exercice 4 : Calcul simple ---")
print(2 + 3)

# Explication :
# Sans guillemets, Python calcule l'expression mathématique
# 2 + 3 = 5


# EXERCICE 5 : Texte + résultat
print("\n--- Exercice 5 : Texte + résultat ---")
print("2+3=", 2+3)

# Explication :
# On peut mélanger texte et calculs dans print()
# Python ajoute un espace entre les éléments


# EXERCICE 6 : Variable nombre
print("\n--- Exercice 6 : Variable nombre ---")
x = 7
print(x)

# Explication :
# x = 7 crée une variable et lui donne la valeur 7
# print(x) affiche la valeur de la variable


# EXERCICE 7 : Variable texte
print("\n--- Exercice 7 : Variable texte ---")
nom = "Nadia"
print(nom)

# Explication :
# Les guillemets créent une variable de type texte (string)


# EXERCICE 8 : Addition avec variables
print("\n--- Exercice 8 : Addition avec variables ---")
a = 4
b = 6
print(a + b)

# Explication :
# Les variables numériques peuvent être additionnées
# a + b = 4 + 6 = 10


# EXERCICE 9 : Lire un prénom (input)
print("\n--- Exercice 9 : Lire un prénom (input) ---")
# nom = input("Prénom: ")  # Décommentez pour tester
# print("Bonjour", nom)

# Version pour démonstration (sans saisie) :
nom = "Karim"  # Simule la saisie utilisateur
print("Bonjour", nom)

# Explication :
# input() demande à l'utilisateur de taper quelque chose
# La valeur tapée est stockée dans une variable


# EXERCICE 10 : Somme de deux nombres (input)
print("\n--- Exercice 10 : Somme de deux nombres (input) ---")
# a = int(input("Premier nombre: "))   # Décommentez pour tester
# b = int(input("Deuxième nombre: "))
# print(a + b)

# Version pour démonstration :
a = 3  # Simule la saisie
b = 8  # Simule la saisie
print(a + b)

# Explication :
# int() convertit le texte saisi en nombre entier
# Sans int(), "3" + "8" donnerait "38" (texte collé)


# ============================================================================
# SECTION 2 : MANIPULATION ET CALCULS (Exercices 11-20)
# ============================================================================

print("\n" + "="*60)
print("SECTION 2 : MANIPULATION ET CALCULS (Exercices 11-20)")
print("="*60)

# EXERCICE 11 : Multiplication
print("\n--- Exercice 11 : Multiplication ---")
n = 4  # Simule input("Nombre: ")
print(n * 10)

# Explication :
# L'opérateur * multiplie les nombres
# 4 * 10 = 40


# EXERCICE 12 : Aire d'un rectangle
print("\n--- Exercice 12 : Aire d'un rectangle ---")
L = 5  # Simule input("Largeur: ")
H = 3  # Simule input("Hauteur: ")
print(L * H)

# Explication :
# Aire = Largeur × Hauteur
# 5 × 3 = 15


# EXERCICE 13 : Concaténer du texte
print("\n--- Exercice 13 : Concaténer du texte ---")
nom = "Aya"  # Simule input("Votre nom: ")
print("Bonjour, " + nom + "!")

# Explication :
# L'opérateur + colle (concatène) des textes
# Attention aux espaces dans les chaînes


# EXERCICE 14 : Longueur d'un mot
print("\n--- Exercice 14 : Longueur d'un mot ---")
mot = "chat"  # Simule input("Tapez un mot: ")
print(len(mot))

# Explication :
# len() compte le nombre de caractères
# "chat" a 4 caractères : c-h-a-t


# EXERCICE 15 : Majuscules
print("\n--- Exercice 15 : Majuscules ---")
mot = "salut"  # Simule input("Tapez un mot: ")
print(mot.upper())

# Explication :
# .upper() convertit en MAJUSCULES
# "salut" devient "SALUT"


# EXERCICE 16 : Minuscules
print("\n--- Exercice 16 : Minuscules ---")
mot = "BonJour"  # Simule input("Tapez un mot: ")
print(mot.lower())

# Explication :
# .lower() convertit en minuscules
# "BonJour" devient "bonjour"


# EXERCICE 17 : Remplacer un caractère
print("\n--- Exercice 17 : Remplacer un caractère ---")
s = "salade"  # Simule input("Tapez un mot: ")
print(s.replace("a", "@"))

# Explication :
# .replace(ancien, nouveau) remplace toutes les occurrences
# "salade" devient "s@l@de"


# EXERCICE 18 : Extraire la première lettre
print("\n--- Exercice 18 : Extraire la première lettre ---")
mot = "Python"  # Simule input("Tapez un mot: ")
print(mot[0])

# Explication :
# mot[0] donne le premier caractère (index 0)
# "Python" → "P"


# EXERCICE 19 : Dernière lettre
print("\n--- Exercice 19 : Dernière lettre ---")
mot = "chat"  # Simule input("Tapez un mot: ")
print(mot[-1])

# Explication :
# mot[-1] donne le dernier caractère
# Les indices négatifs comptent depuis la fin


# EXERCICE 20 : Échanger prénom/nom
print("\n--- Exercice 20 : Échanger prénom/nom ---")
prenom = "Sara"   # Simule input("Prénom: ")
nom = "Dupont"    # Simule input("Nom: ")
print(nom, prenom)

# Explication :
# L'ordre dans print() détermine l'affichage
# print(nom, prenom) affiche d'abord le nom


# ============================================================================
# SECTION 3 : CONDITIONS ET LOGIQUE (Exercices 21-30)
# ============================================================================

print("\n" + "="*60)
print("SECTION 3 : CONDITIONS ET LOGIQUE (Exercices 21-30)")
print("="*60)

# EXERCICE 21 : Pair ou impair (if)
print("\n--- Exercice 21 : Pair ou impair (if) ---")
n = 6  # Simule int(input("Nombre: "))
if n % 2 == 0:
    print("pair")
else:
    print("impair")

# Explication :
# % donne le reste de la division
# 6 % 2 = 0 → pair, 7 % 2 = 1 → impair


# EXERCICE 22 : Positif, négatif ou zéro
print("\n--- Exercice 22 : Positif, négatif ou zéro ---")
n = -3  # Simule int(input("Tapez un nombre: "))
if n > 0:
    print("positif")
elif n < 0:
    print("négatif")
else:
    print("zéro")

# Explication :
# if-elif-else teste plusieurs conditions
# elif = "else if" (sinon si)


# EXERCICE 23 : Comparer deux nombres
print("\n--- Exercice 23 : Comparer deux nombres ---")
a = 7  # Simule int(input("Premier nombre: "))
b = 2  # Simule int(input("Deuxième nombre: "))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Les nombres sont égaux:", a)

# Explication :
# On compare a et b pour trouver le plus grand


# EXERCICE 24 : Mot de passe simple
print("\n--- Exercice 24 : Mot de passe simple ---")
mdp = "python"  # Simule input("Mot de passe: ")
if mdp == "python":
    print("OK")
else:
    print("Non")

# Explication :
# == compare l'égalité entre deux textes
# Sensible à la casse : "Python" ≠ "python"


# EXERCICE 25 : Compter de 1 à N (boucle for)
print("\n--- Exercice 25 : Compter de 1 à N (boucle for) ---")
N = 5  # Simule int(input("Jusqu'à quel nombre? "))
for i in range(1, N + 1):
    print(i)

# Explication :
# range(1, N+1) génère les nombres de 1 à N
# for i in range(...) répète le code pour chaque valeur


# EXERCICE 26 : Somme de 1 à N
print("\n--- Exercice 26 : Somme de 1 à N ---")
N = 4  # Simule int(input("Jusqu'à quel nombre? "))
s = 0
for i in range(1, N + 1):
    s += i  # s = s + i
print(s)

# Explication :
# s = 0 : on commence avec une somme de 0
# s += i : on ajoute i à la somme à chaque tour
# Pour N=4 : 0+1+2+3+4 = 10


# EXERCICE 27 : Table de multiplication (N)
print("\n--- Exercice 27 : Table de multiplication (N) ---")
N = 3  # Simule int(input("Table de multiplication de: "))
for i in range(1, 11):  # De 1 à 10
    print(N * i)

# Explication :
# On multiplie N par chaque nombre de 1 à 10
# Pour N=3 : 3×1=3, 3×2=6, ..., 3×10=30


# EXERCICE 28 : Répéter un mot
print("\n--- Exercice 28 : Répéter un mot ---")
mot = "Python"  # Simule input("Tapez un mot: ")
for i in range(5):
    print(mot)

# Explication :
# range(5) génère 0,1,2,3,4 (5 valeurs)
# Le mot s'affiche 5 fois


# EXERCICE 29 : Compter les voyelles
print("\n--- Exercice 29 : Compter les voyelles ---")
mot = "salut"  # Simule input("Tapez un mot: ")
compteur = 0
for lettre in mot:
    if lettre in "aeiou":
        compteur += 1
print(compteur)

# Explication :
# On parcourt chaque lettre du mot
# Si la lettre est une voyelle (a,e,i,o,u), on compte
# "salut" : s(non), a(oui), l(non), u(oui), t(non) → 2


# EXERCICE 30 : Deviner un nombre (while simple)
print("\n--- Exercice 30 : Deviner un nombre (while simple) ---")
# Version simplifiée pour démonstration :
n = 5  # Première tentative
print(f"Tentative : {n}")
while n != 7:
    print("Raté ! Essayez encore.")
    n += 1  # Simule une nouvelle tentative
    print(f"Tentative : {n}")
print("Bravo ! Vous avez trouvé 7 !")

# Explication :
# while n != 7 : tant que n est différent de 7
# La boucle continue jusqu'à trouver 7


# ============================================================================
# SECTION 4 : STRUCTURES DE DONNÉES (Exercices 31-40)
# ============================================================================

print("\n" + "="*60)
print("SECTION 4 : STRUCTURES DE DONNÉES (Exercices 31-40)")
print("="*60)

# EXERCICE 31 : Saisie jusqu'à "stop"
print("\n--- Exercice 31 : Saisie jusqu'à 'stop' ---")
# Version simplifiée pour démonstration :
mots = ["hello", "world", "python", "stop"]  # Simule les saisies
for mot in mots:
    print(f"Mot saisi : {mot}")
    if mot == "stop":
        break
    print(f"Vous avez tapé : {mot}")
print("Arrêt du programme.")

# Explication :
# while True crée une boucle infinie
# break sort de la boucle quand on tape "stop"


# EXERCICE 32 : Minimum de 3 nombres
print("\n--- Exercice 32 : Minimum de 3 nombres ---")
a = 9  # Simule int(input("Premier nombre: "))
b = 2  # Simule int(input("Deuxième nombre: "))
c = 5  # Simule int(input("Troisième nombre: "))

m = a  # On suppose que a est le minimum
if b < m:
    m = b
if c < m:
    m = c
print(m)

# Explication :
# On compare chaque nombre avec le minimum actuel
# Si on trouve plus petit, on met à jour le minimum


# EXERCICE 33 : Liste de 3 prénoms
print("\n--- Exercice 33 : Liste de 3 prénoms ---")
noms = ["Ali", "Mina", "Zoe"]
print(noms)

# Explication :
# Les crochets [] créent une liste
# Les éléments sont séparés par des virgules


# EXERCICE 34 : Accéder à un élément de liste
print("\n--- Exercice 34 : Accéder à un élément de liste ---")
noms = ["Ali", "Mina", "Zoe"]
print(noms[1])  # Affiche le 2e élément

# Explication :
# L'indexation commence à 0 : Ali=0, Mina=1, Zoe=2
# noms[1] donne "Mina"


# EXERCICE 35 : Ajouter dans une liste
print("\n--- Exercice 35 : Ajouter dans une liste ---")
noms = ["Ali", "Mina", "Zoe"]
print("Liste avant :", noms)
x = "Sara"  # Simule input("Nouveau prénom: ")
noms.append(x)
print("Liste après :", noms)

# Explication :
# .append() ajoute un élément à la fin de la liste
# La liste grandit automatiquement


# EXERCICE 36 : Parcourir une liste
print("\n--- Exercice 36 : Parcourir une liste ---")
noms = ["Ali", "Mina", "Zoe", "Sara"]
for p in noms:
    print(p)

# Explication :
# for p in noms : p prend chaque valeur de la liste
# Plus simple que d'utiliser les indices


# EXERCICE 37 : Moyenne de 3 notes
print("\n--- Exercice 37 : Moyenne de 3 notes ---")
a = 10  # Simule int(input("Première note: "))
b = 12  # Simule int(input("Deuxième note: "))
c = 14  # Simule int(input("Troisième note: "))

m = (a + b + c) / 3
print(m)

# Explication :
# Moyenne = (somme des valeurs) / (nombre de valeurs)
# (10+12+14)/3 = 36/3 = 12.0


# EXERCICE 38 : Formater l'affichage
print("\n--- Exercice 38 : Formater l'affichage ---")
a = 10  # Simule int(input("Première note: "))
b = 12  # Simule int(input("Deuxième note: "))
c = 14  # Simule int(input("Troisième note: "))

m = (a + b + c) / 3
print(f"Moyenne: {m:.2f}")

# Explication :
# f"..." permet le formatage avancé
# {m:.2f} affiche m avec 2 décimales


# EXERCICE 39 : Tronquer / convertir float→int
print("\n--- Exercice 39 : Tronquer / convertir float→int ---")
x = 12.9  # Simule float(input("Nombre décimal: "))
print(int(x))

# Explication :
# int() coupe la partie décimale (troncature)
# 12.9 devient 12 (pas 13 !)


# EXERCICE 40 : Compter jusqu'à dépasser 100
print("\n--- Exercice 40 : Compter jusqu'à dépasser 100 ---")
s = 0
nombres = [30, 40, 50]  # Simule les saisies utilisateur
for nombre in nombres:
    print(f"Somme actuelle: {s}. Ajout de {nombre}")
    s += nombre
    if s > 100:
        break
print(f"Somme finale : {s} (dépasse 100)")

# Explication :
# On additionne des nombres jusqu'à dépasser 100
# while s <= 100 continuerait tant que s ≤ 100


# ============================================================================
# SECTION 5 : ALGORITHMES ET STRUCTURES (Exercices 41-50)
# ============================================================================

print("\n" + "="*60)
print("SECTION 5 : ALGORITHMES ET STRUCTURES (Exercices 41-50)")
print("="*60)

# EXERCICE 41 : Mot palindrome (simple)
print("\n--- Exercice 41 : Mot palindrome (simple) ---")
mot = "kayak"  # Simule input("Tapez un mot: ")
if mot == mot[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

# Explication :
# mot[::-1] inverse la chaîne
# "kayak" inversé = "kayak" → palindrome


# EXERCICE 42 : Compter lettres spécifiques
print("\n--- Exercice 42 : Compter lettres spécifiques ---")
phrase = "Je mange des cerises"  # Simule input("Tapez une phrase: ")
print(phrase.count("e"))

# Explication :
# .count("e") compte le nombre de "e" dans la phrase
# "Je mange des cerises" contient 4 fois la lettre "e"


# EXERCICE 43 : Trouver le max dans une liste
print("\n--- Exercice 43 : Trouver le max dans une liste ---")
# Simulation de la saisie de N nombres :
N = 4
liste = [15, 8, 23, 12]  # Simule la construction progressive
print(f"Liste : {liste}")
m = max(liste)
print(f"Le maximum est : {m}")

# Explication :
# max(liste) trouve automatiquement la plus grande valeur
# Dans [15, 8, 23, 12], le maximum est 23


# EXERCICE 44 : Tri simple
print("\n--- Exercice 44 : Tri simple ---")
noms = ["Zoe", "Ali", "Mina", "Bob"]
print("Liste avant tri :", noms)
noms.sort()
print("Liste après tri :", noms)

# Explication :
# .sort() trie la liste par ordre alphabétique
# Modifie la liste directement (tri sur place)


# EXERCICE 45 : Dictionnaire très basique
print("\n--- Exercice 45 : Dictionnaire très basique ---")
perso = {"nom": "Ali", "age": 20}
print(perso["nom"])

# Explication :
# Les dictionnaires utilisent des accolades {}
# perso["nom"] accède à la valeur de la clé "nom"


# EXERCICE 46 : Ajouter une clé au dictionnaire
print("\n--- Exercice 46 : Ajouter une clé au dictionnaire ---")
perso = {"nom": "Ali", "age": 20}
print("Avant ajout :", perso)
perso["ville"] = "Montréal"
print("Après ajout :", perso)

# Explication :
# perso["ville"] = "Montréal" ajoute une nouvelle clé-valeur
# Les dictionnaires peuvent grandir dynamiquement


# EXERCICE 47 : Vérifier la présence d'une clé
print("\n--- Exercice 47 : Vérifier la présence d'une clé ---")
perso = {"nom": "Ali", "age": 20, "ville": "Montréal"}

if "age" in perso:
    print("Clé 'age' trouvée !")
    print(f"Âge : {perso['age']} ans")
else:
    print("Clé 'age' non trouvée")

# Explication :
# "age" in perso vérifie si la clé existe
# Évite les erreurs si on accède à une clé inexistante


# EXERCICE 48 : Lire un fichier
print("\n--- Exercice 48 : Lire un fichier ---")
# Créer d'abord un fichier de test
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour Python !\nCeci est un test.\nFin du fichier.")

# Lire le fichier
with open("data.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(contenu)

# Explication :
# with open() ouvre un fichier et le ferme automatiquement
# "r" = mode lecture, "w" = mode écriture
# .read() lit tout le contenu du fichier


# EXERCICE 49 : Écrire un fichier
print("\n--- Exercice 49 : Écrire un fichier ---")
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour")

print("Fichier 'out.txt' créé avec succès !")

# Vérification :
with open("out.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(f"Contenu du fichier : '{contenu}'")

# Explication :
# "w" écrase le fichier s'il existe
# .write() écrit du texte dans le fichier


# EXERCICE 50 : Petite fonction
print("\n--- Exercice 50 : Petite fonction ---")
def double(n):
    """Retourne le double du nombre donné."""
    return 2 * n

# Test de la fonction :
print(double(5))   # 10
print(double(3.5)) # 7.0
print(double(-4))  # -8

# Explication :
# def double(n): définit une fonction
# return 2 * n retourne le résultat
# On peut appeler la fonction avec différents nombres


# ============================================================================
# RÉSUMÉ FINAL
# ============================================================================

print("\n" + "="*60)
print("RÉSUMÉ : CONCEPTS PYTHON APPRIS")
print("="*60)

print("""
1. AFFICHAGE :
   - print("texte") : afficher du texte
   - print(nombre) : afficher un nombre
   - print(variable) : afficher une variable

2. VARIABLES :
   - nom = "Alice" : variable texte
   - age = 25 : variable nombre
   - x = 3.14 : variable décimale

3. SAISIE UTILISATEUR :
   - input("Message: ") : lire du texte
   - int(input("Nombre: ")) : lire un nombre entier
   - float(input("Décimal: ")) : lire un nombre décimal

4. OPÉRATIONS :
   - + : addition ou concaténation
   - - : soustraction
   - * : multiplication
   - / : division
   - % : reste de division (modulo)

5. CONDITIONS :
   - if condition: ... : si
   - elif condition: ... : sinon si
   - else: ... : sinon

6. BOUCLES :
   - for i in range(n): ... : répéter n fois
   - for element in liste: ... : parcourir une liste
   - while condition: ... : tant que

7. LISTES :
   - liste = [1, 2, 3] : créer une liste
   - liste[0] : premier élément
   - liste.append(x) : ajouter un élément
   - len(liste) : nombre d'éléments

8. DICTIONNAIRES :
   - dict = {"clé": "valeur"} : créer un dictionnaire
   - dict["clé"] : accéder à une valeur
   - "clé" in dict : vérifier si une clé existe

9. CHAÎNES DE CARACTÈRES :
   - texte[0] : premier caractère
   - texte[-1] : dernier caractère
   - texte.upper() : majuscules
   - texte.lower() : minuscules
   - texte.replace("a", "b") : remplacer

10. FONCTIONS :
    - def nom_fonction(paramètre): ... : définir
    - return résultat : retourner une valeur
    - nom_fonction(argument) : appeler
""")

print("="*60)
print("FÉLICITATIONS ! Vous connaissez maintenant les bases de Python !")
print("Prochaine étape : NumPy, Pandas, et l'IA !")
print("="*60)
