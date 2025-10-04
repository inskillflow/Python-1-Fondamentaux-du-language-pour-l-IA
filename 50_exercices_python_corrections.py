#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
50 EXERCICES PYTHON - FONDAMENTAUX POUR L'IA
===============================================

Ce fichier contient les 50 exercices avec leurs corrections complètes.
Chaque exercice est documenté avec :
- Objectif pédagogique
- Code de solution
- Explications détaillées
- Variantes et bonnes pratiques

Auteur: Cours Python Fondamentaux
Date: 2025
"""

# ============================================================================
# SECTION 1 : BASES DE PYTHON (Exercices 1-10)
# ============================================================================

def exercice_1():
    """
     EXERCICE 1 : Afficher "Bonjour"
    
    Objectif : Afficher un texte simple à l'écran
    Concept : Fonction print() de base
    """
    print("=== Exercice 1 : Afficher 'Bonjour' ===")
    
    # ✅ Solution :
    print("Bonjour")
    
    #   Explication :
    # - print() est une fonction intégrée de Python
    # - Les guillemets indiquent que "Bonjour" est une chaîne de caractères
    # - Le texte s'affiche dans la console
    
    print("Exercice 1 terminé\n")


def exercice_2():
    """
     EXERCICE 2 : Afficher ton prénom
    
    Objectif : Afficher votre prénom personnel
    Concept : Variables et chaînes de caractères
    """
    print("=== Exercice 2 : Afficher ton prénom ===")
    
    # ✅ Solution :
    print("Haythem")  # Remplacez par votre prénom
    
    #   Explication :
    # - Vous pouvez utiliser des guillemets simples ' ou doubles "
    # - Les deux sont équivalents en Python
    # - Exemple alternatif : print('Haythem')
    
    print("Exercice 2 terminé\n")


def exercice_3():
    """
     EXERCICE 3 : Deux lignes d'affichage
    
    Objectif : Afficher deux lignes de texte
    Concept : Instructions séquentielles
    """
    print("=== Exercice 3 : Deux lignes d'affichage ===")
    
    # ✅ Solution :
    print("Bonjour")
    print("Python")
    
    #   Explication :
    # - Chaque print() crée automatiquement une nouvelle ligne
    # - Les instructions s'exécutent dans l'ordre (de haut en bas)
    # - Alternative sur une ligne : print("Bonjour\nPython") avec \n
    
    print("Exercice 3 terminé\n")


def exercice_4():
    """
     EXERCICE 4 : Calcul simple
    
    Objectif : Afficher le résultat de 2 + 3
    Concept : Expressions mathématiques
    """
    print("=== Exercice 4 : Calcul simple ===")
    
    # ✅ Solution :
    print(2 + 3)
    
    #   Explication :
    # - Python évalue d'abord l'expression 2 + 3 = 5
    # - Puis print() affiche le résultat
    # - Différence importante : print("2 + 3") afficherait le texte "2 + 3"
    # - Sans guillemets = calcul, avec guillemets = texte
    
    print("Exercice 4 terminé\n")


def exercice_5():
    """
     EXERCICE 5 : Texte + résultat
    
    Objectif : Afficher "2+3=" suivi du résultat
    Concept : Mélanger texte et calculs
    """
    print("=== Exercice 5 : Texte + résultat ===")
    
    # ✅ Solution :
    print("2+3=", 2+3)
    
    #   Explication :
    # - print() peut prendre plusieurs arguments séparés par des virgules
    # - "2+3=" est une chaîne de caractères (texte)
    # - 2+3 est une expression mathématique qui donne 5
    # - Python ajoute automatiquement un espace entre les arguments
    
    #   Alternatives :
    print("2+3=" + str(2+3))  # Concaténation
    print(f"2+3={2+3}")       # f-string (plus moderne)
    
    print("Exercice 5 terminé\n")


def exercice_6():
    """
     EXERCICE 6 : Variable nombre
    
    Objectif : Créer une variable x=7 et l'afficher
    Concept : Variables et assignation
    """
    print("=== Exercice 6 : Variable nombre ===")
    
    # ✅ Solution :
    x = 7
    print(x)
    
    #   Explication :
    # - x = 7 crée une variable nommée 'x' et lui assigne la valeur 7
    # - print(x) affiche la valeur contenue dans la variable x
    # - En Python, pas besoin de déclarer le type de la variable
    # - La variable est créée automatiquement lors de l'assignation
    
    print("Exercice 6 terminé\n")


def exercice_7():
    """
     EXERCICE 7 : Variable texte
    
    Objectif : Créer une variable nom = "Nadia" puis l'afficher
    Concept : Variables de type string
    """
    print("=== Exercice 7 : Variable texte ===")
    
    # ✅ Solution :
    nom = "Nadia"
    print(nom)
    
    # 📖 Explication :
    # - nom = "Nadia" crée une variable de type string (chaîne de caractères)
    # - Les guillemets indiquent à Python que c'est du texte, pas du code
    # - Python détermine automatiquement que 'nom' est une chaîne
    # - On peut vérifier le type avec : print(type(nom))
    
    print("Exercice 7 terminé\n")


def exercice_8():
    """
     EXERCICE 8 : Addition avec variables
    
    Objectif : Créer a=4 et b=6, puis afficher a+b
    Concept : Opérations avec variables
    """
    print("=== Exercice 8 : Addition avec variables ===")
    
    # ✅ Solution :
    a = 4
    b = 6
    print(a + b)
    
    # 📖 Explication :
    # - a et b sont des variables numériques (entiers)
    # - L'opérateur + additionne les valeurs des variables
    # - Python évalue d'abord a + b (4 + 6 = 10), puis affiche le résultat
    
    # 🔄 Variantes utiles :
    print("La somme est :", a + b)  # Avec texte explicatif
    print(f"{a} + {b} = {a + b}")   # f-string pour un affichage élégant
    
    print("✅ Exercice 8 terminé\n")


def exercice_9():
    """
    📝 EXERCICE 9 : Lire un prénom (input)
    
    🎯 Objectif : Demander un prénom à l'utilisateur et l'afficher
    💡 Concept : Saisie utilisateur avec input()
    """
    print("=== Exercice 9 : Lire un prénom (input) ===")
    
    # ✅ Solution :
    nom = input("Prénom: ")
    print("Bonjour", nom)
    
    # 📖 Explication :
    # - input("Prénom: ") affiche "Prénom: " et attend que l'utilisateur tape quelque chose
    # - La valeur tapée est stockée dans la variable 'nom'
    # - input() retourne toujours une chaîne de caractères (string)
    # - print("Bonjour", nom) affiche les deux éléments séparés par un espace
    
    # 🔄 Alternative avec f-string :
    # print(f"Bonjour {nom}!")
    
    print("✅ Exercice 9 terminé\n")


def exercice_10():
    """
    📝 EXERCICE 10 : Somme de deux nombres (input)
    
    🎯 Objectif : Lire deux nombres et afficher leur somme
    💡 Concept : Conversion de types avec int()
    """
    print("=== Exercice 10 : Somme de deux nombres (input) ===")
    
    # ✅ Solution :
    a = int(input("Premier nombre: "))
    b = int(input("Deuxième nombre: "))
    print(a + b)
    
    # 📖 Explication :
    # - input() retourne toujours une chaîne de caractères
    # - int() convertit cette chaîne en nombre entier
    # - Sans int(), "3" + "8" donnerait "38" (concaténation de texte)
    # - Avec int(), 3 + 8 donne 11 (addition mathématique)
    
    # ⚠️ Attention : si l'utilisateur tape du texte non-numérique, 
    #    int() génèrera une erreur ValueError
    
    print("✅ Exercice 10 terminé\n")


# ============================================================================
# 🔧 SECTION 2 : MANIPULATION ET CALCULS (Exercices 11-20)
# ============================================================================

def exercice_11():
    """
    📝 EXERCICE 11 : Multiplication
    
    🎯 Objectif : Lire un nombre et afficher sa valeur multipliée par 10
    💡 Concept : Opérateur de multiplication
    """
    print("=== Exercice 11 : Multiplication ===")
    
    # ✅ Solution :
    n = int(input("Nombre: "))
    print(n * 10)
    
    # 📖 Explication :
    # - L'opérateur * effectue une multiplication
    # - Fonctionne avec tous les types numériques (int, float)
    # - Exemple : si n = 4, alors n * 10 = 40
    
    # 🔄 Affichage plus explicite :
    print(f"{n} × 10 = {n * 10}")
    
    print("✅ Exercice 11 terminé\n")


def exercice_12():
    """
    📝 EXERCICE 12 : Aire d'un rectangle
    
    🎯 Objectif : Lire largeur et hauteur, puis afficher l'aire (L×H)
    💡 Concept : Application mathématique pratique
    """
    print("=== Exercice 12 : Aire d'un rectangle ===")
    
    # ✅ Solution :
    L = int(input("Largeur: "))
    H = int(input("Hauteur: "))
    print(L * H)
    
    # 📖 Explication :
    # - Formule mathématique : Aire = Largeur × Hauteur
    # - Deux input() successifs pour saisir les dimensions
    # - Le résultat est calculé et affiché directement
    
    # 🔄 Version plus explicite :
    aire = L * H
    print(f"L'aire du rectangle {L}×{H} est {aire}")
    
    print("✅ Exercice 12 terminé\n")


def exercice_13():
    """
    📝 EXERCICE 13 : Concaténer du texte
    
    🎯 Objectif : Afficher "Bonjour, NOM !" avec le nom saisi
    💡 Concept : Concaténation de chaînes
    """
    print("=== Exercice 13 : Concaténer du texte ===")
    
    # ✅ Solution :
    nom = input("Votre nom: ")
    print("Bonjour, " + nom + "!")
    
    # 📖 Explication :
    # - L'opérateur + avec des chaînes effectue une concaténation (collage)
    # - "Bonjour, " + "Aya" + "!" devient "Bonjour, Aya!"
    # - Attention aux espaces : ils doivent être inclus dans les chaînes
    
    # 🔄 Méthodes alternatives :
    print("Bonjour,", nom, "!")      # Avec des virgules (espaces automatiques)
    print(f"Bonjour, {nom}!")        # f-string (plus moderne et lisible)
    
    print("✅ Exercice 13 terminé\n")


def exercice_14():
    """
    📝 EXERCICE 14 : Longueur d'un mot
    
    🎯 Objectif : Lire un mot et afficher sa longueur (nombre de caractères)
    💡 Concept : Fonction len()
    """
    print("=== Exercice 14 : Longueur d'un mot ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    print(len(mot))
    
    # 📖 Explication :
    # - len() est une fonction intégrée qui compte les caractères
    # - Fonctionne avec toutes les séquences : chaînes, listes, tuples
    # - Compte tous les caractères, y compris les espaces
    # - "chat" a 4 caractères : c-h-a-t
    
    # 🔄 Version plus explicite :
    longueur = len(mot)
    print(f"Le mot '{mot}' contient {longueur} caractères")
    
    print("✅ Exercice 14 terminé\n")


def exercice_15():
    """
    📝 EXERCICE 15 : Majuscules
    
    🎯 Objectif : Lire un mot et l'afficher en MAJUSCULES
    💡 Concept : Méthodes de chaînes (.upper())
    """
    print("=== Exercice 15 : Majuscules ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    print(mot.upper())
    
    # 📖 Explication :
    # - .upper() est une méthode des chaînes de caractères
    # - Elle retourne une nouvelle chaîne en majuscules
    # - La chaîne originale n'est pas modifiée (les strings sont immuables)
    # - Utile pour normaliser des données ou comparer sans tenir compte de la casse
    
    # 🔄 Autres méthodes utiles :
    print(mot.lower())      # minuscules
    print(mot.capitalize()) # Première lettre en majuscule
    print(mot.title())      # Chaque Mot Commence Par Une Majuscule
    
    print("✅ Exercice 15 terminé\n")


def exercice_16():
    """
    📝 EXERCICE 16 : Minuscules
    
    🎯 Objectif : Lire un mot et l'afficher en minuscules
    💡 Concept : Méthodes de chaînes (.lower())
    """
    print("=== Exercice 16 : Minuscules ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    print(mot.lower())
    
    # 📖 Explication :
    # - .lower() convertit tous les caractères en minuscules
    # - Très utile pour normaliser les données utilisateur
    # - Exemple d'usage : comparaisons insensibles à la casse
    
    # 💼 Cas d'usage pratique :
    reponse = input("Voulez-vous continuer? (oui/non): ")
    if reponse.lower() == "oui":  # Accepte "OUI", "Oui", "oui"
        print("On continue !")
    
    print("✅ Exercice 16 terminé\n")


def exercice_17():
    """
    📝 EXERCICE 17 : Remplacer un caractère
    
    🎯 Objectif : Remplacer toutes les lettres "a" par "@" dans un mot
    💡 Concept : Méthode .replace()
    """
    print("=== Exercice 17 : Remplacer un caractère ===")
    
    # ✅ Solution :
    s = input("Tapez un mot: ")
    print(s.replace("a", "@"))
    
    # 📖 Explication :
    # - .replace(ancien, nouveau) remplace TOUTES les occurrences
    # - Sensible à la casse : "a" ≠ "A"
    # - Retourne une nouvelle chaîne (l'originale n'est pas modifiée)
    # - Si le caractère n'existe pas, retourne la chaîne inchangée
    
    # 🔄 Exemples supplémentaires :
    print(s.replace("a", "@").replace("e", "3"))  # Remplacements multiples
    print(s.replace("a", "@", 1))  # Remplacer seulement la première occurrence
    
    print("✅ Exercice 17 terminé\n")


def exercice_18():
    """
    📝 EXERCICE 18 : Extraire la première lettre
    
    🎯 Objectif : Afficher la première lettre d'un mot
    💡 Concept : Indexation des chaînes
    """
    print("=== Exercice 18 : Extraire la première lettre ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    print(mot[0])
    
    # 📖 Explication :
    # - L'indexation en Python commence à 0
    # - mot[0] = premier caractère, mot[1] = deuxième, etc.
    # - Pour "Python" : P=0, y=1, t=2, h=3, o=4, n=5
    # - ⚠️ Attention : si le mot est vide, mot[0] génère une erreur IndexError
    
    # 🛡️ Version sécurisée :
    if len(mot) > 0:
        print(f"Première lettre : {mot[0]}")
    else:
        print("Le mot est vide !")
    
    print("✅ Exercice 18 terminé\n")


def exercice_19():
    """
    📝 EXERCICE 19 : Dernière lettre
    
    🎯 Objectif : Afficher la dernière lettre d'un mot
    💡 Concept : Indexation négative
    """
    print("=== Exercice 19 : Dernière lettre ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    print(mot[-1])
    
    # 📖 Explication :
    # - Les indices négatifs comptent depuis la fin
    # - mot[-1] = dernier caractère
    # - mot[-2] = avant-dernier caractère
    # - Pour "chat" : c=0/-4, h=1/-3, a=2/-2, t=3/-1
    
    # 🔄 Autres exemples d'indexation :
    print(f"Premier : {mot[0]}, Dernier : {mot[-1]}")
    if len(mot) > 1:
        print(f"Avant-dernier : {mot[-2]}")
    
    print("✅ Exercice 19 terminé\n")


def exercice_20():
    """
    📝 EXERCICE 20 : Échanger prénom/nom
    
    🎯 Objectif : Lire prénom et nom, puis afficher "Nom Prénom"
    💡 Concept : Ordre des variables dans l'affichage
    """
    print("=== Exercice 20 : Échanger prénom/nom ===")
    
    # ✅ Solution :
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    print(nom, prenom)
    
    # 📖 Explication :
    # - L'ordre des variables dans print() détermine l'ordre d'affichage
    # - print(nom, prenom) affiche d'abord nom, puis prenom
    # - Python ajoute automatiquement un espace entre les arguments
    
    # 🔄 Autres formats possibles :
    print(f"{nom}, {prenom}")           # Format "Dupont, Sara"
    print(f"{nom.upper()} {prenom}")    # "DUPONT Sara"
    print(prenom + " " + nom)           # Ordre normal avec concaténation
    
    print("✅ Exercice 20 terminé\n")


# ============================================================================
# 🔀 SECTION 3 : CONDITIONS ET LOGIQUE (Exercices 21-30)
# ============================================================================

def exercice_21():
    """
    📝 EXERCICE 21 : Pair ou impair (if)
    
    🎯 Objectif : Dire si un nombre est pair ou impair
    💡 Concept : Structures conditionnelles if/else
    """
    print("=== Exercice 21 : Pair ou impair (if) ===")
    
    # ✅ Solution :
    n = int(input("Nombre: "))
    if n % 2 == 0:
        print("pair")
    else:
        print("impair")
    
    # 📖 Explication :
    # - L'opérateur % (modulo) donne le reste de la division
    # - 6 % 2 = 0 (6 divisé par 2 = 3 reste 0) → pair
    # - 7 % 2 = 1 (7 divisé par 2 = 3 reste 1) → impair
    # - Un nombre est pair si le reste de sa division par 2 est 0
    
    # 🔄 Version avec f-string :
    resultat = "pair" if n % 2 == 0 else "impair"
    print(f"Le nombre {n} est {resultat}")
    
    print("✅ Exercice 21 terminé\n")


def exercice_22():
    """
    📝 EXERCICE 22 : Positif, négatif ou zéro
    
    🎯 Objectif : Classer un nombre en positif, négatif ou zéro
    💡 Concept : Structure if-elif-else
    """
    print("=== Exercice 22 : Positif, négatif ou zéro ===")
    
    # ✅ Solution :
    n = int(input("Tapez un nombre: "))
    if n > 0:
        print("positif")
    elif n < 0:
        print("négatif")
    else:
        print("zéro")
    
    # 📖 Explication :
    # - if-elif-else permet de tester plusieurs conditions mutuellement exclusives
    # - Python teste les conditions dans l'ordre et s'arrête à la première vraie
    # - elif = "else if" (sinon si)
    # - Le bloc else capture tous les autres cas (ici, n == 0)
    
    # 🔄 Version compacte avec opérateur ternaire :
    resultat = "positif" if n > 0 else ("négatif" if n < 0 else "zéro")
    print(f"Le nombre {n} est {resultat}")
    
    print("✅ Exercice 22 terminé\n")


def exercice_23():
    """
    📝 EXERCICE 23 : Comparer deux nombres
    
    🎯 Objectif : Afficher le plus grand de deux nombres
    💡 Concept : Comparaisons et conditions
    """
    print("=== Exercice 23 : Comparer deux nombres ===")
    
    # ✅ Solution :
    a = int(input("Premier nombre: "))
    b = int(input("Deuxième nombre: "))
    
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Les nombres sont égaux:", a)
    
    # 📖 Explication :
    # - Trois cas possibles : a > b, b > a, ou a == b
    # - Les opérateurs de comparaison : >, <, >=, <=, ==, !=
    # - Le cas d'égalité est géré par le else
    
    # 🔄 Version avec fonction max() :
    print(f"Le plus grand est : {max(a, b)}")
    
    print("✅ Exercice 23 terminé\n")


def exercice_24():
    """
    📝 EXERCICE 24 : Mot de passe simple
    
    🎯 Objectif : Vérifier si le mot de passe est "python"
    💡 Concept : Comparaison de chaînes
    """
    print("=== Exercice 24 : Mot de passe simple ===")
    
    # ✅ Solution :
    mdp = input("Mot de passe: ")
    if mdp == "python":
        print("OK")
    else:
        print("Non")
    
    # 📖 Explication :
    # - L'opérateur == compare l'égalité entre deux chaînes
    # - Sensible à la casse : "Python" ≠ "python"
    # - Important pour la sécurité : comparaison exacte
    
    # 🔄 Version insensible à la casse :
    if mdp.lower() == "python":
        print("OK (insensible à la casse)")
    
    print("✅ Exercice 24 terminé\n")


def exercice_25():
    """
    📝 EXERCICE 25 : Compter de 1 à N (boucle for)
    
    🎯 Objectif : Afficher les nombres de 1 à N
    💡 Concept : Boucle for avec range()
    """
    print("=== Exercice 25 : Compter de 1 à N (boucle for) ===")
    
    # ✅ Solution :
    N = int(input("Jusqu'à quel nombre? "))
    for i in range(1, N + 1):
        print(i)
    
    # 📖 Explication :
    # - range(1, N+1) génère les nombres de 1 à N inclus
    # - range(début, fin_exclue) : la fin n'est pas incluse
    # - for i in range(...) : i prend successivement chaque valeur
    # - Chaque print(i) affiche le nombre sur une nouvelle ligne
    
    # 🔄 Affichage sur une seule ligne :
    for i in range(1, N + 1):
        print(i, end=" ")  # end=" " évite le saut de ligne
    print()  # Saut de ligne final
    
    print("✅ Exercice 25 terminé\n")


def exercice_26():
    """
    📝 EXERCICE 26 : Somme de 1 à N
    
    🎯 Objectif : Calculer la somme 1+2+...+N
    💡 Concept : Accumulateur dans une boucle
    """
    print("=== Exercice 26 : Somme de 1 à N ===")
    
    # ✅ Solution :
    N = int(input("Jusqu'à quel nombre? "))
    s = 0
    for i in range(1, N + 1):
        s += i  # Équivalent à s = s + i
    print(s)
    
    # 📖 Explication :
    # - s = 0 : initialisation de l'accumulateur
    # - s += i : ajoute i à la somme actuelle à chaque itération
    # - Pattern classique : initialiser → boucler → accumuler → afficher
    # - Pour N=4 : s=0, puis s=1, s=3, s=6, s=10
    
    # 🔄 Vérification avec la formule mathématique :
    formule = N * (N + 1) // 2
    print(f"Vérification avec formule : {formule}")
    
    # 🔄 Version avec sum() et range() :
    print(f"Avec sum() : {sum(range(1, N + 1))}")
    
    print("✅ Exercice 26 terminé\n")


def exercice_27():
    """
    📝 EXERCICE 27 : Table de multiplication (N)
    
    🎯 Objectif : Afficher la table de multiplication de N (N×1 à N×10)
    💡 Concept : Boucle for avec calculs
    """
    print("=== Exercice 27 : Table de multiplication (N) ===")
    
    # ✅ Solution :
    N = int(input("Table de multiplication de: "))
    for i in range(1, 11):  # De 1 à 10
        print(N * i)
    
    # 📖 Explication :
    # - range(1, 11) génère les nombres de 1 à 10
    # - À chaque tour, i change : 1, 2, 3, ..., 10
    # - N * i calcule le produit : N×1, N×2, N×3, ..., N×10
    # - Pour N=3 : 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
    
    # 🔄 Version avec affichage formaté :
    print(f"\nTable de {N} (format élégant) :")
    for i in range(1, 11):
        print(f"{N} × {i} = {N * i}")
    
    print("✅ Exercice 27 terminé\n")


def exercice_28():
    """
    📝 EXERCICE 28 : Répéter un mot
    
    🎯 Objectif : Afficher un mot 5 fois
    💡 Concept : Boucle for avec nombre fixe d'itérations
    """
    print("=== Exercice 28 : Répéter un mot ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    for i in range(5):
        print(mot)
    
    # 📖 Explication :
    # - range(5) génère 0, 1, 2, 3, 4 (5 valeurs)
    # - La variable i n'est pas utilisée dans le bloc, c'est normal
    # - On peut utiliser _ pour indiquer qu'on n'utilise pas la variable
    
    # 🔄 Version avec _ (convention Python) :
    for _ in range(5):
        print(mot)
    
    # 🔄 Version avec numérotation :
    for i in range(1, 6):
        print(f"{i}. {mot}")
    
    print("✅ Exercice 28 terminé\n")


def exercice_29():
    """
    📝 EXERCICE 29 : Compter les voyelles
    
    🎯 Objectif : Compter les voyelles (a,e,i,o,u) dans un mot
    💡 Concept : Boucle sur caractères et condition in
    """
    print("=== Exercice 29 : Compter les voyelles ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    compteur = 0
    for lettre in mot:
        if lettre in "aeiou":
            compteur += 1
    print(compteur)
    
    # 📖 Explication :
    # - for lettre in mot : parcourt chaque caractère du mot
    # - if lettre in "aeiou" : vérifie si le caractère est une voyelle
    # - compteur += 1 : incrémente le compteur si c'est une voyelle
    # - "salut" : s(non), a(oui), l(non), u(oui), t(non) → 2 voyelles
    
    # 🔄 Version insensible à la casse :
    compteur_total = 0
    for lettre in mot.lower():  # Convertir en minuscules d'abord
        if lettre in "aeiou":
            compteur_total += 1
    print(f"Voyelles (insensible casse) : {compteur_total}")
    
    # 🔄 Version avec compréhension de liste (avancé) :
    voyelles = sum(1 for lettre in mot.lower() if lettre in "aeiou")
    print(f"Avec compréhension : {voyelles}")
    
    print("✅ Exercice 29 terminé\n")


def exercice_30():
    """
    📝 EXERCICE 30 : Deviner un nombre (while simple)
    
    🎯 Objectif : Tant que la réponse n'est pas 7, redemander
    💡 Concept : Boucle while avec condition
    """
    print("=== Exercice 30 : Deviner un nombre (while simple) ===")
    
    # ✅ Solution :
    n = int(input("Devinez le nombre (entre 1 et 10): "))
    while n != 7:
        print("Raté ! Essayez encore.")
        n = int(input("Devinez le nombre (entre 1 et 10): "))
    print("Bravo ! Vous avez trouvé 7 !")
    
    # 📖 Explication :
    # - while n != 7 : tant que n est différent de 7
    # - La boucle continue jusqu'à ce que l'utilisateur tape 7
    # - Important : redemander la saisie dans la boucle, sinon boucle infinie
    # - != signifie "différent de"
    
    # 🔄 Version avec compteur de tentatives :
    tentatives = 1
    while n != 7:
        print(f"Tentative {tentatives} ratée !")
        n = int(input("Réessayez: "))
        tentatives += 1
    print(f"Trouvé en {tentatives} tentative(s) !")
    
    print("✅ Exercice 30 terminé\n")


# ============================================================================
# 🔄 SECTION 4 : BOUCLES AVANCÉES (Exercices 31-40)
# ============================================================================

def exercice_31():
    """
    📝 EXERCICE 31 : Saisie jusqu'à "stop"
    
    🎯 Objectif : Lire des mots jusqu'à ce que l'utilisateur écrive "stop"
    💡 Concept : Boucle infinie avec break
    """
    print("=== Exercice 31 : Saisie jusqu'à 'stop' ===")
    
    # ✅ Solution :
    while True:
        mot = input("Tapez un mot (ou 'stop' pour arrêter): ")
        if mot == "stop":
            break
        print(f"Vous avez tapé : {mot}")
    print("Arrêt du programme.")
    
    # 📖 Explication :
    # - while True : boucle infinie (condition toujours vraie)
    # - break : sort immédiatement de la boucle
    # - Pattern classique pour les menus ou saisies répétées
    # - L'utilisateur contrôle l'arrêt avec un mot-clé spécial
    
    # 🔄 Version avec liste pour stocker les mots :
    mots_saisis = []
    while True:
        mot = input("Mot: ")
        if mot == "stop":
            break
        mots_saisis.append(mot)
    print(f"Vous avez saisi {len(mots_saisis)} mots : {mots_saisis}")
    
    print("✅ Exercice 31 terminé\n")


def exercice_32():
    """
    📝 EXERCICE 32 : Minimum de 3 nombres
    
    🎯 Objectif : Afficher le plus petit de 3 nombres
    💡 Concept : Comparaisons multiples et algorithme de minimum
    """
    print("=== Exercice 32 : Minimum de 3 nombres ===")
    
    # ✅ Solution :
    a = int(input("Premier nombre: "))
    b = int(input("Deuxième nombre: "))
    c = int(input("Troisième nombre: "))
    
    m = a  # Supposer que a est le minimum
    if b < m:
        m = b
    if c < m:
        m = c
    print(m)
    
    # 📖 Explication :
    # - Algorithme classique : supposer que le premier est le minimum
    # - Comparer avec chaque autre nombre et mettre à jour si nécessaire
    # - m garde toujours la plus petite valeur trouvée jusqu'à présent
    # - Pour 9, 2, 5 : m=9, puis m=2 (car 2<9), puis m=2 (car 5≥2)
    
    # 🔄 Version avec fonction min() :
    print(f"Avec fonction min() : {min(a, b, c)}")
    
    # 🔄 Version avec liste :
    nombres = [a, b, c]
    print(f"Avec liste : {min(nombres)}")
    
    print("✅ Exercice 32 terminé\n")


def exercice_33():
    """
    📝 EXERCICE 33 : Liste de 3 prénoms
    
    🎯 Objectif : Créer une liste de prénoms et l'afficher
    💡 Concept : Création et affichage de listes
    """
    print("=== Exercice 33 : Liste de 3 prénoms ===")
    
    # ✅ Solution :
    noms = ["Ali", "Mina", "Zoe"]
    print(noms)
    
    # 📖 Explication :
    # - Les crochets [] définissent une liste
    # - Les éléments sont séparés par des virgules
    # - Une liste peut contenir différents types de données
    # - print(noms) affiche toute la liste avec les crochets
    
    # 🔄 Affichage élément par élément :
    print("Affichage individuel :")
    for nom in noms:
        print(f"- {nom}")
    
    # 🔄 Informations sur la liste :
    print(f"La liste contient {len(noms)} prénoms")
    print(f"Type de la variable : {type(noms)}")
    
    print("✅ Exercice 33 terminé\n")


def exercice_34():
    """
    📝 EXERCICE 34 : Accéder à un élément de liste
    
    🎯 Objectif : Afficher le 2e prénom de la liste
    💡 Concept : Indexation des listes
    """
    print("=== Exercice 34 : Accéder à un élément de liste ===")
    
    # ✅ Solution :
    noms = ["Ali", "Mina", "Zoe"]
    print(noms[1])  # Index 1 = 2e élément
    
    # 📖 Explication :
    # - L'indexation commence à 0 : Ali=0, Mina=1, Zoe=2
    # - noms[1] accède au 2e élément (Mina)
    # - ⚠️ Attention : noms[3] génèrerait une erreur IndexError
    
    # 🔄 Affichage de tous les éléments avec leurs indices :
    for i, nom in enumerate(noms):
        print(f"Index {i} : {nom}")
    
    # 🔄 Accès sécurisé :
    index = 1
    if 0 <= index < len(noms):
        print(f"Élément à l'index {index} : {noms[index]}")
    else:
        print("Index hors limites !")
    
    print("✅ Exercice 34 terminé\n")


def exercice_35():
    """
    📝 EXERCICE 35 : Ajouter dans une liste
    
    🎯 Objectif : Ajouter un prénom saisi à la liste
    💡 Concept : Méthode .append() des listes
    """
    print("=== Exercice 35 : Ajouter dans une liste ===")
    
    # ✅ Solution :
    noms = ["Ali", "Mina", "Zoe"]
    print("Liste initiale :", noms)
    
    x = input("Nouveau prénom à ajouter: ")
    noms.append(x)
    print("Liste après ajout :", noms)
    
    # 📖 Explication :
    # - .append(élément) ajoute un élément à la fin de la liste
    # - Les listes sont mutables : elles peuvent être modifiées
    # - La liste grandit automatiquement
    # - L'élément ajouté devient le dernier (index len(liste)-1)
    
    # 🔄 Autres méthodes utiles :
    noms.insert(0, "Premier")  # Insérer au début
    print("Après insert(0) :", noms)
    
    noms.extend(["Nouveau1", "Nouveau2"])  # Ajouter plusieurs éléments
    print("Après extend() :", noms)
    
    print("✅ Exercice 35 terminé\n")


def exercice_36():
    """
    📝 EXERCICE 36 : Parcourir une liste
    
    🎯 Objectif : Afficher chaque prénom de la liste
    💡 Concept : Boucle for sur une liste
    """
    print("=== Exercice 36 : Parcourir une liste ===")
    
    # ✅ Solution :
    noms = ["Ali", "Mina", "Zoe", "Sara"]
    for p in noms:
        print(p)
    
    # 📖 Explication :
    # - for p in noms : p prend successivement chaque valeur de la liste
    # - Plus pythonique que for i in range(len(noms))
    # - La variable p est temporaire et existe seulement dans la boucle
    # - Chaque print(p) affiche un prénom sur une nouvelle ligne
    
    # 🔄 Avec numérotation :
    print("\nAvec numérotation :")
    for i, p in enumerate(noms, 1):  # Commencer à 1
        print(f"{i}. {p}")
    
    # 🔄 Avec formatage :
    print("\nFormatage élégant :")
    for p in noms:
        print(f"👤 {p}")
    
    print("✅ Exercice 36 terminé\n")


def exercice_37():
    """
    📝 EXERCICE 37 : Moyenne de 3 notes
    
    🎯 Objectif : Calculer la moyenne de 3 notes
    💡 Concept : Division et moyenne arithmétique
    """
    print("=== Exercice 37 : Moyenne de 3 notes ===")
    
    # ✅ Solution :
    a = int(input("Première note: "))
    b = int(input("Deuxième note: "))
    c = int(input("Troisième note: "))
    
    m = (a + b + c) / 3
    print(m)
    
    # 📖 Explication :
    # - Formule de la moyenne : (somme des valeurs) / (nombre de valeurs)
    # - L'opérateur / effectue une division flottante
    # - Le résultat est un float même si les notes sont des entiers
    # - Pour 10, 12, 14 : (10+12+14)/3 = 36/3 = 12.0
    
    # 🔄 Version avec liste :
    notes = [a, b, c]
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne avec liste : {moyenne}")
    
    # 🔄 Arrondi à 2 décimales :
    print(f"Moyenne arrondie : {round(m, 2)}")
    
    print("✅ Exercice 37 terminé\n")


def exercice_38():
    """
    📝 EXERCICE 38 : Formater l'affichage
    
    🎯 Objectif : Afficher "Moyenne: 12.00" avec 2 décimales
    💡 Concept : Formatage de nombres avec f-string
    """
    print("=== Exercice 38 : Formater l'affichage ===")
    
    # ✅ Solution :
    a = int(input("Première note: "))
    b = int(input("Deuxième note: "))
    c = int(input("Troisième note: "))
    
    m = (a + b + c) / 3
    print(f"Moyenne: {m:.2f}")
    
    # 📖 Explication :
    # - f"..." : f-string pour formatage avancé
    # - {m:.2f} : affiche m avec 2 décimales (.2f)
    # - .2f = format flottant avec 2 chiffres après la virgule
    # - Très utile pour l'affichage professionnel de nombres
    
    # 🔄 Autres formats utiles :
    print(f"Moyenne (1 décimale) : {m:.1f}")
    print(f"Moyenne (entier) : {m:.0f}")
    print(f"Moyenne (pourcentage) : {m:.1%}")  # Multiplie par 100 et ajoute %
    
    print("✅ Exercice 38 terminé\n")


def exercice_39():
    """
    📝 EXERCICE 39 : Tronquer / convertir float→int
    
    🎯 Objectif : Montrer la conversion de 12.9 en entier
    💡 Concept : Conversion de types et troncature
    """
    print("=== Exercice 39 : Tronquer / convertir float→int ===")
    
    # ✅ Solution :
    x = float(input("Tapez un nombre décimal: "))
    print(int(x))
    
    # 📖 Explication :
    # - float() convertit la saisie en nombre décimal
    # - int() coupe la partie décimale (troncature, pas arrondi)
    # - 12.9 devient 12 (pas 13 !)
    # - -12.9 devient -12 (troncature vers zéro)
    
    # 🔄 Comparaison avec d'autres méthodes :
    print(f"Valeur originale : {x}")
    print(f"int(x) - troncature : {int(x)}")
    print(f"round(x) - arrondi : {round(x)}")
    
    import math
    print(f"math.floor(x) - arrondi inférieur : {math.floor(x)}")
    print(f"math.ceil(x) - arrondi supérieur : {math.ceil(x)}")
    
    print("✅ Exercice 39 terminé\n")


def exercice_40():
    """
    📝 EXERCICE 40 : Compter jusqu'à dépasser 100
    
    🎯 Objectif : Additionner des nombres jusqu'à ce que la somme dépasse 100
    💡 Concept : Boucle while avec accumulation
    """
    print("=== Exercice 40 : Compter jusqu'à dépasser 100 ===")
    
    # ✅ Solution :
    s = 0
    while s <= 100:
        nombre = int(input(f"Somme actuelle: {s}. Ajoutez un nombre: "))
        s += nombre
    print(f"Somme finale : {s} (dépasse 100)")
    
    # 📖 Explication :
    # - s = 0 : initialisation de la somme
    # - while s <= 100 : continue tant que la somme ne dépasse pas 100
    # - s += nombre : ajoute le nombre saisi à la somme
    # - La boucle s'arrête dès que s > 100
    
    # 🔄 Version avec historique :
    nombres_ajoutes = []
    s = 0
    while s <= 100:
        nombre = int(input(f"Somme: {s}. Nombre: "))
        nombres_ajoutes.append(nombre)
        s += nombre
    
    print(f"Nombres ajoutés : {nombres_ajoutes}")
    print(f"Somme finale : {s}")
    
    print("✅ Exercice 40 terminé\n")


# ============================================================================
# 🧠 SECTION 5 : ALGORITHMES ET STRUCTURES (Exercices 41-50)
# ============================================================================

def exercice_41():
    """
    📝 EXERCICE 41 : Mot palindrome (simple)
    
    🎯 Objectif : Dire si un mot est identique à son inverse
    💡 Concept : Slicing et comparaison de chaînes
    """
    print("=== Exercice 41 : Mot palindrome (simple) ===")
    
    # ✅ Solution :
    mot = input("Tapez un mot: ")
    if mot == mot[::-1]:
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")
    
    # 📖 Explication :
    # - mot[::-1] : slicing avec pas de -1 = inverse la chaîne
    # - [start:stop:step] où step=-1 parcourt de la fin vers le début
    # - "kayak" inversé = "kayak" → palindrome
    # - "python" inversé = "nohtyp" → pas palindrome
    
    # 🔄 Version avec affichage de l'inverse :
    inverse = mot[::-1]
    print(f"Mot original : {mot}")
    print(f"Mot inversé : {inverse}")
    print(f"Palindrome : {mot == inverse}")
    
    # 🔄 Version insensible à la casse :
    mot_clean = mot.lower()
    if mot_clean == mot_clean[::-1]:
        print("Palindrome (insensible à la casse)")
    
    print("✅ Exercice 41 terminé\n")


def exercice_42():
    """
    📝 EXERCICE 42 : Compter lettres spécifiques
    
    🎯 Objectif : Compter le nombre de "e" dans une phrase
    💡 Concept : Méthode .count() des chaînes
    """
    print("=== Exercice 42 : Compter lettres spécifiques ===")
    
    # ✅ Solution :
    phrase = input("Tapez une phrase: ")
    print(phrase.count("e"))
    
    # 📖 Explication :
    # - .count(caractère) compte le nombre d'occurrences
    # - Sensible à la casse : "e" ≠ "E"
    # - Retourne un entier (0 si aucune occurrence)
    # - "Je mange des cerises" : 4 occurrences de "e"
    
    # 🔄 Version insensible à la casse :
    total_e = phrase.lower().count("e")
    print(f"Nombre de 'e' (insensible casse) : {total_e}")
    
    # 🔄 Compter plusieurs caractères :
    voyelles = "aeiou"
    total_voyelles = sum(phrase.lower().count(v) for v in voyelles)
    print(f"Total voyelles : {total_voyelles}")
    
    print("✅ Exercice 42 terminé\n")


def exercice_43():
    """
    📝 EXERCICE 43 : Trouver le max dans une liste
    
    🎯 Objectif : Lire N nombres et trouver le maximum
    💡 Concept : Construction de liste et fonction max()
    """
    print("=== Exercice 43 : Trouver le max dans une liste ===")
    
    # ✅ Solution :
    N = int(input("Combien de nombres? "))
    liste = []
    
    for i in range(N):
        nombre = int(input(f"Nombre {i+1}: "))
        liste.append(nombre)
    
    m = max(liste)
    print(f"Le maximum est : {m}")
    
    # 📖 Explication :
    # - Construction progressive de la liste avec append()
    # - max(liste) trouve automatiquement la plus grande valeur
    # - Alternative : parcourir la liste et comparer manuellement
    
    # 🔄 Version avec compréhension de liste :
    # liste = [int(input(f"Nombre {i+1}: ")) for i in range(N)]
    
    # 🔄 Informations supplémentaires :
    print(f"Liste complète : {liste}")
    print(f"Minimum : {min(liste)}")
    print(f"Somme : {sum(liste)}")
    print(f"Moyenne : {sum(liste)/len(liste):.2f}")
    
    print("✅ Exercice 43 terminé\n")


def exercice_44():
    """
    📝 EXERCICE 44 : Tri simple
    
    🎯 Objectif : Trier une liste de prénoms par ordre alphabétique
    💡 Concept : Méthode .sort() des listes
    """
    print("=== Exercice 44 : Tri simple ===")
    
    # ✅ Solution :
    noms = ["Zoe", "Ali", "Mina", "Bob"]
    print("Liste avant tri :", noms)
    
    noms.sort()
    print("Liste après tri :", noms)
    
    # 📖 Explication :
    # - .sort() modifie la liste sur place (tri en place)
    # - Ordre alphabétique par défaut
    # - Pour les chaînes : ordre lexicographique (dictionnaire)
    # - ⚠️ Attention : .sort() ne retourne rien (None)
    
    # 🔄 Autres options de tri :
    noms_copy = ["Zoe", "Ali", "Mina", "Bob"]
    
    # Tri inverse :
    noms_copy.sort(reverse=True)
    print("Tri inverse :", noms_copy)
    
    # Tri par longueur :
    noms_copy.sort(key=len)
    print("Tri par longueur :", noms_copy)
    
    # sorted() : crée une nouvelle liste triée
    noms_original = ["Zoe", "Ali", "Mina", "Bob"]
    noms_tries = sorted(noms_original)
    print("Original inchangé :", noms_original)
    print("Nouvelle liste triée :", noms_tries)
    
    print("✅ Exercice 44 terminé\n")


def exercice_45():
    """
    📝 EXERCICE 45 : Dictionnaire très basique
    
    🎯 Objectif : Créer un dictionnaire personne et afficher le nom
    💡 Concept : Dictionnaires et accès par clé
    """
    print("=== Exercice 45 : Dictionnaire très basique ===")
    
    # ✅ Solution :
    perso = {"nom": "Ali", "age": 20}
    print(perso["nom"])
    
    # 📖 Explication :
    # - Les dictionnaires utilisent des accolades {}
    # - Format : {"clé": "valeur", "clé2": "valeur2"}
    # - perso["nom"] accède à la valeur associée à la clé "nom"
    # - Les clés sont généralement des chaînes ou des nombres
    
    # 🔄 Affichage complet du dictionnaire :
    print("Dictionnaire complet :", perso)
    print("Toutes les clés :", list(perso.keys()))
    print("Toutes les valeurs :", list(perso.values()))
    
    # 🔄 Parcours du dictionnaire :
    for cle, valeur in perso.items():
        print(f"{cle}: {valeur}")
    
    print("✅ Exercice 45 terminé\n")


def exercice_46():
    """
    📝 EXERCICE 46 : Ajouter une clé au dictionnaire
    
    🎯 Objectif : Ajouter perso["ville"] = "Montréal"
    💡 Concept : Modification de dictionnaires
    """
    print("=== Exercice 46 : Ajouter une clé au dictionnaire ===")
    
    # ✅ Solution :
    perso = {"nom": "Ali", "age": 20}
    print("Avant ajout :", perso)
    
    perso["ville"] = "Montréal"
    print("Après ajout :", perso)
    
    # 📖 Explication :
    # - perso["ville"] = "Montréal" ajoute une nouvelle paire clé-valeur
    # - Si la clé existe déjà, sa valeur est mise à jour
    # - Si la clé n'existe pas, elle est créée
    # - Les dictionnaires sont mutables (modifiables)
    
    # 🔄 Autres opérations sur dictionnaires :
    perso["age"] = 21  # Modifier une valeur existante
    print("Après modification age :", perso)
    
    # Ajouter plusieurs clés :
    perso.update({"profession": "Étudiant", "pays": "Canada"})
    print("Après update() :", perso)
    
    print("✅ Exercice 46 terminé\n")


def exercice_47():
    """
    📝 EXERCICE 47 : Vérifier la présence d'une clé
    
    🎯 Objectif : Tester si "age" est dans le dictionnaire
    💡 Concept : Opérateur in avec dictionnaires
    """
    print("=== Exercice 47 : Vérifier la présence d'une clé ===")
    
    # ✅ Solution :
    perso = {"nom": "Ali", "age": 20, "ville": "Montréal"}
    
    if "age" in perso:
        print("Clé 'age' trouvée !")
        print(f"Âge : {perso['age']} ans")
    else:
        print("Clé 'age' non trouvée")
    
    # 📖 Explication :
    # - "age" in perso vérifie si la clé "age" existe
    # - L'opérateur in avec un dictionnaire teste les clés, pas les valeurs
    # - Très utile pour éviter les erreurs KeyError
    # - Plus sûr que d'accéder directement à perso["age"]
    
    # 🔄 Méthode alternative avec .get() :
    age = perso.get("age", "Non spécifié")
    print(f"Âge avec .get() : {age}")
    
    # Test d'une clé inexistante :
    if "telephone" in perso:
        print("Téléphone trouvé")
    else:
        print("Pas de téléphone dans le dictionnaire")
    
    print("✅ Exercice 47 terminé\n")


def exercice_48():
    """
    📝 EXERCICE 48 : Lire un fichier (optionnel si Colab)
    
    🎯 Objectif : Lire le contenu d'un fichier texte
    💡 Concept : Gestion de fichiers avec open()
    """
    print("=== Exercice 48 : Lire un fichier ===")
    
    # Créer d'abord un fichier de test
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("Bonjour Python !\nCeci est un test.\nFin du fichier.")
    
    # ✅ Solution :
    with open("data.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
    
    # 📖 Explication :
    # - with open() : gestionnaire de contexte (ferme automatiquement le fichier)
    # - "r" : mode lecture (read)
    # - encoding="utf-8" : pour les caractères accentués
    # - .read() lit tout le contenu du fichier
    
    # 🔄 Lecture ligne par ligne :
    print("\nLecture ligne par ligne :")
    with open("data.txt", "r", encoding="utf-8") as f:
        for numero, ligne in enumerate(f, 1):
            print(f"Ligne {numero}: {ligne.strip()}")  # .strip() enlève \n
    
    print("✅ Exercice 48 terminé\n")


def exercice_49():
    """
    📝 EXERCICE 49 : Écrire un fichier
    
    🎯 Objectif : Écrire "Bonjour" dans un fichier out.txt
    💡 Concept : Écriture de fichiers
    """
    print("=== Exercice 49 : Écrire un fichier ===")
    
    # ✅ Solution :
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write("Bonjour")
    
    print("Fichier 'out.txt' créé avec succès !")
    
    # Vérification en relisant le fichier :
    with open("out.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        print(f"Contenu du fichier : '{contenu}'")
    
    # 📖 Explication :
    # - "w" : mode écriture (write) - écrase le fichier s'il existe
    # - .write() écrit une chaîne dans le fichier
    # - Pas de saut de ligne automatique (contrairement à print)
    # - Le fichier est fermé automatiquement avec with
    
    # 🔄 Écriture de plusieurs lignes :
    with open("out_multi.txt", "w", encoding="utf-8") as f:
        f.write("Première ligne\n")
        f.write("Deuxième ligne\n")
        f.write("Troisième ligne")
    
    # 🔄 Avec print() dans un fichier :
    with open("out_print.txt", "w", encoding="utf-8") as f:
        print("Bonjour", file=f)
        print("Python", file=f)
    
    print("✅ Exercice 49 terminé\n")


def exercice_50():
    """
    📝 EXERCICE 50 : Petite fonction
    
    🎯 Objectif : Créer une fonction double(n) qui renvoie 2*n
    💡 Concept : Définition et appel de fonctions
    """
    print("=== Exercice 50 : Petite fonction ===")
    
    # ✅ Solution :
    def double(n):
        """Retourne le double du nombre donné."""
        return 2 * n
    
    # Test de la fonction :
    print(double(5))   # 10
    print(double(3.5)) # 7.0
    print(double(-4))  # -8
    
    # 📖 Explication :
    # - def double(n): définit une fonction nommée 'double'
    # - n est le paramètre de la fonction
    # - return 2 * n retourne le résultat du calcul
    # - La fonction peut être appelée plusieurs fois avec différents arguments
    
    # 🔄 Version avec documentation complète :
    def double_doc(n):
        """
        Calcule le double d'un nombre.
        
        Args:
            n (int ou float): Le nombre à doubler
            
        Returns:
            int ou float: Le double du nombre
            
        Exemples:
            >>> double_doc(5)
            10
            >>> double_doc(3.5)
            7.0
        """
        return 2 * n
    
    # Test avec différents types :
    print(f"double(5) = {double(5)}")
    print(f"double(3.14) = {double(3.14)}")
    
    # 🔄 Fonction interactive :
    nombre = float(input("Nombre à doubler: "))
    resultat = double(nombre)
    print(f"Le double de {nombre} est {resultat}")
    
    print("✅ Exercice 50 terminé\n")


# ============================================================================
# 🚀 FONCTION PRINCIPALE - EXÉCUTION DE TOUS LES EXERCICES
# ============================================================================

def executer_tous_exercices():
    """
    Exécute tous les exercices dans l'ordre.
    Utile pour tester ou démontrer toutes les solutions.
    """
    print("🐍" + "="*60)
    print("   50 EXERCICES PYTHON - CORRECTIONS COMPLÈTES")
    print("="*63)
    print()
    
    # Liste de toutes les fonctions d'exercices
    exercices = [
        exercice_1, exercice_2, exercice_3, exercice_4, exercice_5,
        exercice_6, exercice_7, exercice_8, exercice_9, exercice_10,
        exercice_11, exercice_12, exercice_13, exercice_14, exercice_15,
        exercice_16, exercice_17, exercice_18, exercice_19, exercice_20,
        exercice_21, exercice_22, exercice_23, exercice_24, exercice_25,
        exercice_26, exercice_27, exercice_28, exercice_29, exercice_30,
        exercice_31, exercice_32, exercice_33, exercice_34, exercice_35,
        exercice_36, exercice_37, exercice_38, exercice_39, exercice_40,
        exercice_41, exercice_42, exercice_43, exercice_44, exercice_45,
        exercice_46, exercice_47, exercice_48, exercice_49, exercice_50
    ]
    
    # Exécution avec gestion d'erreurs
    for i, exercice in enumerate(exercices, 1):
        try:
            print(f"🔄 Exécution de l'exercice {i}...")
            exercice()
        except KeyboardInterrupt:
            print(f"\n⏹️ Arrêt demandé à l'exercice {i}")
            break
        except Exception as e:
            print(f"❌ Erreur dans l'exercice {i}: {e}")
            continue
    
    print("🎉 Tous les exercices terminés !")
    print("="*63)


def menu_exercices():
    """
    Menu interactif pour choisir quel exercice exécuter.
    """
    while True:
        print("\n" + "="*50)
        print("🐍 MENU DES EXERCICES PYTHON")
        print("="*50)
        print("1-10  : Bases (print, variables, input)")
        print("11-20 : Manipulation texte et calculs")
        print("21-30 : Conditions et boucles")
        print("31-40 : Structures de données")
        print("41-50 : Concepts avancés")
        print("0     : Quitter")
        print("all   : Exécuter tous les exercices")
        print("="*50)
        
        choix = input("Choisissez un exercice (1-50, 'all', ou 0): ").strip()
        
        if choix == "0":
            print("👋 Au revoir !")
            break
        elif choix.lower() == "all":
            executer_tous_exercices()
        elif choix.isdigit() and 1 <= int(choix) <= 50:
            num = int(choix)
            try:
                # Exécuter l'exercice spécifique
                globals()[f"exercice_{num}"]()
            except KeyError:
                print(f"❌ Exercice {num} non trouvé")
            except Exception as e:
                print(f"❌ Erreur : {e}")
        else:
            print("❌ Choix invalide. Tapez un nombre entre 1 et 50.")


# ============================================================================
# 🎯 POINT D'ENTRÉE DU PROGRAMME
# ============================================================================

if __name__ == "__main__":
    """
    Point d'entrée principal du programme.
    Exécute le menu interactif ou tous les exercices selon le choix.
    """
    print("🐍 Bienvenue dans les 50 Exercices Python !")
    print("Ce fichier contient toutes les corrections avec explications.")
    print()
    
    choix = input("Voulez-vous le menu interactif? (o/n): ").lower()
    
    if choix in ["o", "oui", "y", "yes"]:
        menu_exercices()
    else:
        print("Exécution de tous les exercices...")
        executer_tous_exercices()


# ============================================================================
# 📚 DOCUMENTATION SUPPLÉMENTAIRE
# ============================================================================

"""
🎓 CONCEPTS PYTHON COUVERTS DANS CES EXERCICES :

1. BASES :
   - print() : affichage
   - Variables et assignation
   - Types de données (int, float, str)
   - input() : saisie utilisateur

2. OPÉRATIONS :
   - Opérateurs arithmétiques (+, -, *, /, %)
   - Opérateurs de comparaison (==, !=, <, >, <=, >=)
   - Opérateurs logiques (and, or, not)

3. CHAÎNES DE CARACTÈRES :
   - Indexation et slicing
   - Méthodes : .upper(), .lower(), .replace(), .count()
   - Concaténation et formatage (f-strings)

4. STRUCTURES DE CONTRÔLE :
   - Conditions : if, elif, else
   - Boucles : for, while
   - Contrôle de flux : break, continue

5. STRUCTURES DE DONNÉES :
   - Listes : création, indexation, .append(), .sort()
   - Dictionnaires : création, accès par clé, .keys(), .values(), .items()

6. FONCTIONS :
   - Définition avec def
   - Paramètres et return
   - Documentation avec docstrings

7. FICHIERS :
   - Lecture et écriture avec open()
   - Gestionnaire de contexte with

8. BONNES PRATIQUES :
   - Noms de variables explicites
   - Commentaires et documentation
   - Gestion d'erreurs de base
   - Code lisible et structuré

🎯 OBJECTIFS PÉDAGOGIQUES ATTEINTS :
- Maîtrise de la syntaxe Python de base
- Compréhension des concepts fondamentaux
- Capacité à résoudre des problèmes simples
- Préparation aux concepts avancés (IA, data science)
- Bonnes pratiques de programmation

📈 PROGRESSION RECOMMANDÉE :
1. Faire tous les exercices dans l'ordre
2. Comprendre chaque explication
3. Tester les variantes proposées
4. Modifier les exemples pour expérimenter
5. Passer aux bibliothèques spécialisées (NumPy, Pandas, etc.)
"""
