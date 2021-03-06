"""
###############################################################################
#
#              Institut Supérieur d'électronique de Paris (ISEP)
#
#                               SUJET DE TIPE:
#                     Othello et Intelligence Artificielle
#
#    Première année  --  MPSI
#
#    Créateurs : Alexandre BIGOT
#                Valentin  COLIN
#                Marc  PARTENSKY
#
#    Version : 2019
#
###############################################################################
#
#                             SOMMAIRE de Bordure
#
#    1.    class Bordure:  ......................................... ligne  47
#    1.1   ----> __init__ (self,nombre_de_lignes,espacement)  ...... ligne  50
#    1.2   ----> recupererNomDesJoueurs (self,noms_des_joueurs)  ... ligne  56
#    1.3   ----> actualiser (self,rang,scores,fini,gagnant)  ....... ligne  60
#    1.4   ----> afficherTexte(self,texte,position,taille,couleur) . ligne  68
#    1.5   ----> afficherFond (self)  .............................. ligne  76
#    1.6   ----> clear (self)  ..................................... ligne  88
#    1.7   ----> afficherTemps (self,position,taille,couleur)  ..... ligne  92
#    1.8   ----> afficherRectangle (self,position,taille,couleur) .. ligne 101
#    1.9   ----> afficherTempsPropre (self)  ....................... ligne 106
#    1.10  ----> afficher (self)  .................................. ligne 112
#    1.11  ----> ecrireTitre (self,n)  ............................. ligne 122
#    1.12  ----> ecrireTour (self,n)  .............................. ligne 126
#    1.13  ----> crireScore (self,n)  .............................. ligne 131
#    1.14  ----> ecrireGagnants (self,n)  .......................... ligne 142
#    1.15  ----> afficherLignes (self,x=10,y=10)  .................. ligne 147
#
###############################################################################
"""
# --coding:utf-8--

import config as cfg
import pygame, time, couleurs, outils


class Bordure:
    """Classe permettant d'afficher des informations en temps réel"""

    def __init__(self, nombre_de_lignes=20, espacement=40):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface = pygame.Surface(cfg.RESOLUTION_BORDURE)
        self.espacement = espacement  # espace entre deux lignes de texte
        self.lignes = ["" for i in range(nombre_de_lignes)]

    def recupererNomDesJoueurs(self, noms_des_joueurs):
        """Récupère le nom des joueurs pour les afficher plus tard."""
        self.noms_des_joueurs = noms_des_joueurs

    def actualiser(self, rang, scores, fini, gagnant):
        """Actualise la bordure."""
        self.rang = rang
        self.tour = rang % 2
        self.scores = scores
        self.fini = fini
        self.gagnant = gagnant

    def afficherTexte(self, texte, position, taille=None, couleur=None):
        """Affiche du texte à l'écran."""
        if not couleur:
            couleur = cfg.THEME_BORDURE["couleur texte"]
        if not taille:
            taille = cfg.THEME_BORDURE["taille texte"]
        font = pygame.font.SysFont(cfg.THEME_BORDURE["police"], taille)
        surface_texte = font.render(texte, 1, couleur)
        self.surface.blit(surface_texte, position)

    def afficherFond(self):
        """Affiche l'arrière plan de la bordure."""
        ftx, fty = self.surface.get_size()
        ftm = max(ftx, fty)
        for y in range(0, fty, 10):
            for x in range(0, ftx, 10):
                r = int(abs(outils.bijection(x, [0, ftx], [0, 255])))
                g = int(255 - abs(outils.bijection((x + y) / 2, [0, ftm], [0, 255])))
                b = int(abs(outils.bijection(y, [0, fty], [0, 255])))
                couleur = (r, g, b)
                pygame.draw.rect(self.surface, couleur, [x, y, 10, 10], 0)

    def clear(self):
        """Nettoie la surface en recoloriant celle-ci par son arrière plan."""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTemps(self, position, taille=30, couleur=couleurs.BLANC):
        """Affiche l'heure à un instant."""
        heures = str(time.localtime()[3])
        minutes = str(time.localtime()[4])
        secondes = str(time.localtime()[5])
        temps = (
            heures
            + " : "
            + (2 - len(minutes)) * "0"
            + minutes
            + " : "
            + (2 - len(secondes)) * "0"
            + secondes
        )
        self.afficherTexte(temps, position, taille, couleur)

    def afficherRectangle(self, position, taille, couleur):
        """Affiche un rectangle sur la surface de la bordure avec sa position
        sa taille, et sa couleur."""
        pygame.draw.rect(self.surface, couleur, position + taille, 0)

    def afficherTempsPropre(self):  # n'est pas actualiser donc non-utilisable
        """Affiche le temps en se souciant de la présentation."""
        tx, ty = self.surface.get_size()
        self.afficherRectangle((0, 0), (tx, 70), couleurs.BLEU)
        self.afficherTemps((20, 10), couleurs.VERT)

    def afficher(self):
        """Permet d'afficher la bordure sur sa surface."""
        self.afficherFond()
        self.ecrireTitre(n=0)
        self.ecrireTour(n=2)
        self.ecrireScore(n=5)
        if self.fini:
            self.ecrireGagnants(n=9)
        self.afficherLignes()  # affiche chaque ligne à l'écran

    # n'est absolument pas rigoureux,
    # mais nécessaire tant que l'on à pas implémenter de technique efficace pour centrer du texte
    def ecrireTitre(self, n):
        """Ecrit le titre dans la bordure."""
        self.lignes[n] = "                           Othello"

    def ecrireTour(self, n):
        """Ecrit le tour du joueur, utilise 1 ligne."""
        self.lignes[n] = "Tour du joueur:"
        self.lignes[n + 1] = str(self.noms_des_joueurs[self.tour])

    def ecrireScore(self, n):
        """Ecrit le score à la ligne 'n',
        utilise autant de ligne qu'il y a de joueurs + 1 ligne.
        """
        self.lignes[n] = "Score :"
        nombre_de_joueurs = len(self.noms_des_joueurs)
        for i in range(nombre_de_joueurs):
            couleur_joueur = cfg.THEME_PLATEAU["nom couleur pion"][i]
            self.lignes[n + i] = (
                str(self.noms_des_joueurs[i])
                + " ("
                + couleur_joueur
                + ")"
                + " : "
                + str(self.scores[i])
            )

    def ecrireGagnants(self, n):
        """Ecrit si la partie est finie ou pas."""
        self.lignes[n] = "La partie est finie."
        if self.gagnant:
            self.lignes[n + 1] = "Le gagnant est : " + str(self.gagnant)
        else:
            self.lignes[n + 1] = "ÉGALITÉ"

    def afficherLignes(self, x=10, y=10):
        """Affiche les lignes du texte sur la surface de la bordure."""
        taille = len(self.lignes)
        for i in range(taille):
            self.afficherTexte(self.lignes[i], (x, y + i * self.espacement))
