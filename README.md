Initialisation de la grille :

Une grille 3x3 est créée, initialement vide, représentée sous forme d'une liste de listes.
Affichage de la grille :

Une fonction afficher_grille() est définie pour afficher la grille actuelle dans la console.
La fonction parcourt chaque ligne de la grille et affiche les symboles "|" entre les cases et des tirets pour séparer les lignes.
Vérification de la victoire :

Une fonction verifier_victoire() vérifie si un joueur a gagné en parcourant les lignes, les colonnes et les diagonales de la grille.
Si une ligne, une colonne ou une diagonale est remplie par un seul symbole (X ou O), alors le joueur correspondant a gagné.
Vérification de la grille pleine :

Une fonction grille_pleine() vérifie si la grille est pleine, c'est-à-dire s'il n'y a plus de cases vides.
Si toutes les cases sont remplies et aucun joueur n'a gagné, alors le jeu se termine en match nul.

Boucle principale du jeu :

La fonction jouer_morpion() gère le jeu complet.
Le jeu continue tant qu'il n'y a ni gagnant ni match nul.
À chaque tour :
La grille est affichée.
Le joueur en cours est invité à saisir une ligne et une colonne pour placer son symbole.
La saisie est vérifiée pour s'assurer qu'elle est valide (dans les limites de la grille et la case n'est pas déjà occupée).
Une fois le mouvement effectué, le programme vérifie s'il y a un gagnant ou un match nul.
Si aucune de ces conditions n'est remplie, le jeu passe au joueur suivant.

Fin du jeu :

Une fois qu'un joueur a gagné ou qu'il y a un match nul, le jeu affiche le résultat final et la grille finale.
Ce code est une implémentation simple et directe du jeu de X/O en Python, utilisant principalement des boucles, des conditions et des fonctions pour gérer le flux du jeu.
