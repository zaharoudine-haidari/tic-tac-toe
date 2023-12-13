import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR, HAUTEUR = 300, 300
TAILLE_CASE = LARGEUR // 3
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
LIGNE = 15

# Initialisation de l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tic-Tac-Toe")

# Grille représentant le morpion
grille = [['' for _ in range(3)] for _ in range(3)]

# Boucle principale du jeu
def main():
    joueur_actuel = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                colonne, ligne = event.pos[0] // TAILLE_CASE, event.pos[1] // TAILLE_CASE

                if grille[ligne][colonne] == '':
                    grille[ligne][colonne] = joueur_actuel
                    gagnant = any(all(grille[i][j] == joueur_actuel for j in range(3)) for i in range(3)) or \
                              any(all(grille[i][j] == joueur_actuel for i in range(3)) for j in range(3)) or \
                              all(grille[i][i] == joueur_actuel for i in range(3)) or \
                              all(grille[i][2 - i] == joueur_actuel for i in range(3))

                    if gagnant:
                        print(f"Le joueur {joueur_actuel} a gagné !")
                        pygame.quit()
                        sys.exit()
                    elif all(cellule for ligne in grille for cellule in ligne):
                        print("Match nul !")
                        pygame.quit()
                        sys.exit()
                    else:
                        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

        # Dessiner le plateau
        ecran.fill(BLANC)
        for ligne in range(1, 3):
            pygame.draw.line(ecran, NOIR, (TAILLE_CASE * ligne, 0), (TAILLE_CASE * ligne, HAUTEUR), LIGNE)
            pygame.draw.line(ecran, NOIR, (0, TAILLE_CASE * ligne), (LARGEUR, TAILLE_CASE * ligne), LIGNE)

        for ligne in range(3):
            for colonne in range(3):
                if grille[ligne][colonne] == 'X':
                    pygame.draw.line(ecran, NOIR, (colonne * TAILLE_CASE, ligne * TAILLE_CASE),
                                     ((colonne + 1) * TAILLE_CASE, (ligne + 1) * TAILLE_CASE), LIGNE)
                    pygame.draw.line(ecran, NOIR, ((colonne + 1) * TAILLE_CASE, ligne * TAILLE_CASE),
                                     (colonne * TAILLE_CASE, (ligne + 1) * TAILLE_CASE), LIGNE)
                elif grille[ligne][colonne] == 'O':
                    centre = (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2)
                    rayon = TAILLE_CASE // 2 - LIGNE // 2
                    pygame.draw.circle(ecran, NOIR, centre, rayon, LIGNE)

        # Mettre à jour l'affichage
        pygame.display.flip()

# Exécuter le jeu
if __name__ == "__main__":
    main()
