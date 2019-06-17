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
#                             SOMMAIRE de Panneau
#
#    1.    class Panneau:  ......................................... ligne  42
#    1.1   ----> __init__ (self,(etc).)  ........................... ligne  45
#    1.2   ----> coller (self,surface,compartiment)  ............... ligne  59
#    1.3   ----> pointer (self)  ................................... ligne  68
#    1.4   ----> obtenirNumeroCompartiment (self,position)  ........ ligne  77
#    1.5   ----> obtenirPositionDansCompartiment (self,position,n) . ligne  87
#    1.6   ----> afficher (self)  .................................. ligne  98
#    1.7   ----> afficherCadres (self)  ............................ ligne 105
#    1.8   ----> afficherCadre(self,compartiment,couleur,l)  ....... ligne 112
#    1.9   ----> positionRelative(self)  ........................... ligne 124
#
###############################################################################
"""
# --coding:utf-8--

from fenetre import Fenetre
import couleurs
import pygame



class Panneau(Fenetre):
    """Classe héritant de la fenêtre permettant de gérer des découpages."""

    def __init__(self,  nom              = "fenetre",
                        taille           = None,
                        police_du_texte  = "monospace",
                        taille_du_texte  = 65,
                        couleur_du_texte = couleurs.BLANC,
                        couleur_du_fond  = couleurs.NOIR,
                        plein_ecran      = False,
                        set              = True,
                        decoupages=[]):
        """Crée un panneau qui est une fenetre organisée en compartiments."""
        super().__init__(nom, taille, police_du_texte, taille_du_texte,
                         couleur_du_texte, couleur_du_fond, plein_ecran, set)
        self.decoupages = decoupages

    def coller(self,surface,compartiment):
        """Pose une surface dans le compartiment."""
        sx,sy = surface.get_size() # on récupère la taille de la surface
        dx,dy,dsx,dsy = self.decoupages[compartiment]
        self.screen.blit(surface,(dx,dy))
        # blit permet de placer les surface à l'écran
        # mais ne les montre pas encore à l'utilisateur
        # (il faut pour cela appeler la méthode flip())

    def pointer(self):
        """Renvoie la position du curseur
        dans le système de coordonnées du compartiment.
        """
        position = pygame.mouse.get_pos()
        n = self.obtenirNumeroCompartiment(position)
        position = self.obtenirPositionDansCompartiment(position,n)
        return position

    def obtenirNumeroCompartiment(self,position):
        """Renvoie le numéro du compartiment qui contient la position donnée"""
        x,y = position
        for compartiment in range(len(self.decoupages)):
            dx,dy,dsx,dsy = self.decoupages[compartiment]
            if dx <= x <= (dx+dsx) and dy <= y <= (dy+dsy):
                resultat=compartiment
                break
        return resultat

    def obtenirPositionDansCompartiment(self,position,n):
        """Renvoie la position relative
        au système de coordonnées du compartiment n.
        """
        x,y = position
        dx,dy,dsx,dsy = self.decoupages[compartiment]
        tx,ty = self.taille
        nx = x * dsx / tx+dx
        ny = y * dsy / ty+dy
        return (nx,ny)

    def afficher(self):
        """Affiche les éléments spécifiques au panneau,
        c'est à dire par exemple
        la marge entre les différents compartiments.
        """
        self.afficherCadres()

    def afficherCadres(self):
        """Décoration graphique pour bien visualiser
        la séparation entre les découpages.
        """
        for compartiment in range(len(self.decoupages)):
            self.afficherCadre(compartiment)

    def afficherCadre(self,compartiment,couleur=couleurs.NOIR,l=3):
        """Affiche un cadre autour d'un compartiment."""
        dx,dy,dsx,dsy=self.decoupages[compartiment]
        p1 = (    dx,     dy)
        p2 = (    dx, dy+dsy)
        p3 = (dx+dsx, dy+dsy)
        p4 = (dx+dsx,     dy)
        pygame.draw.line(self.screen,couleur,p1,p2,l)
        pygame.draw.line(self.screen,couleur,p2,p3,l)
        pygame.draw.line(self.screen,couleur,p3,p4,l)
        pygame.draw.line(self.screen,couleur,p4,p1,l)

    def positionRelative(self):
        """Renvoie la position relative au compartiment
        dans lequel la souris se place.
        """
        px,py = pygame.mouse.get_pos()
        wsx,wsy = self.taille
        for decoupage in self.decoupages:
            dx,dy,dsx,dsy = decoupage
            if dx <= px <= (dx+dsx) and dy <= py <= (dy+dsy):
                return (dsx*px/wsx+dx,dsy*py/wsy+dy)
