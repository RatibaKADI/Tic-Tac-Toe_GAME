# Définir une fonction pour afficher la grille
def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne))
        print("-----")

# Définir une fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille, symbole):
    # Vérifier les lignes
    for ligne in grille:
        if all(case == symbole for case in ligne):
            return True
    
    # Vérifier les colonnes
    for i in range(3):
        if all(grille[j][i] == symbole for j in range(3)):
            return True
    
    # Vérifier les diagonales
    if all(grille[i][i] == symbole for i in range(3)) or \
       all(grille[i][2-i] == symbole for i in range(3)):
        return True
    
    return False

# Définir une fonction pour vérifier si la grille est pleine
def grille_pleine(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

# Fonction principale pour jouer au jeu de morpion
def jouer_morpion():
    grille = [[" "]*3 for _ in range(3)]  # Initialiser la grille vide
    joueur = "X"  # Définir le premier joueur
    
    while True:
        afficher_grille(grille)
        print("Tour du joueur", joueur)
        
        # Demander au joueur de saisir la ligne et la colonne
        while True:
            ligne = int(input("Entrez le numéro de ligne (0, 1, 2): "))
            colonne = int(input("Entrez le numéro de colonne (0, 1, 2): "))
            if 0 <= ligne < 3 and 0 <= colonne < 3 and grille[ligne][colonne] == " ":
                break
            else:
                print("Mouvement invalide. Réessayez.")
        
        # Mettre à jour la grille avec le mouvement du joueur
        grille[ligne][colonne] = joueur
        
        # Vérifier si le joueur a gagné
        if verifier_victoire(grille, joueur):
            print("Le joueur", joueur, "a gagné !")
            afficher_grille(grille)
            break
        
        # Vérifier si la grille est pleine (match nul)
        if grille_pleine(grille):
            print("Match nul !")
            afficher_grille(grille)
            break
        
        # Passer au prochain joueur
        joueur = "O" if joueur == "X" else "X"

# Appeler la fonction principale pour jouer au jeu
jouer_morpion()
