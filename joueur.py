"""
################################################################################
#
#              Institut Supérieur d'électronique de Paris (ISEP)
#
#                               SUJET DE TIPE:
#                     Othello et Intelligence Artificielle
#
#    Première année  --  MPSI
#
#    Créateurs : Marc  PARTENSKY
#                Valentin  COLIN
#                Alexandre BIGOT
#
#    Version : 2019
#
###############################################################################
#
#                     SOMMAIRE des classes de joueurs
#
#    1.    class Joueur:  ........................................... ligne
#    1.1   ------> __init__ (self,nom_du_joueur=None)  .............. ligne
#    1.2   ------> attribuerCote (self,cote)  ....................... ligne
#    1.3   ------> __str__ (self)  .................................. ligne
#
#    2.    class Humain (joueur):  .................................. ligne
#    2.1   ------> __init__ (self,nom=None)  ........................ ligne
#    2.2   ------> jouer (self,plateau,fenetre)  .................... ligne
#    2.3   ------> __str__ (self)  .................................. ligne
#
#    3.    class Robot (Joueur):  ................................... ligne
#    3.1   ------> __init__ (self,nom=None)  ........................ ligne
#    3.2   ------> main (self, plateau)  ............................ ligne
#    3.3   ------> jouer (self,plateau,fenetre)  .................... ligne
#    3.4   ------> jouerAleatoire (self,plateau)  ................... ligne
#    3.5   ------> __str__ (self)  .................................. ligne
#
#    4.   class Developpeur (Joueur):  .............................. ligne
#    4.1  ------> __init__ (self,nom=None)  ......................... ligne
#    4.2  ------> jouer (self,plateau,fenetre)  ..................... ligne
#
###############################################################################
"""
# --coding:utf-8--

import time
import random
import math
import json
import config as cfg
import pygame
import couleurs



class Joueur:
    def __init__(self,nom_du_joueur=None):
        """Cree un joueur et défini son choix à rien. Il s'agit de la classe de base de tous les joueurs."""
        self.choix=None
        self.nom=str(nom_du_joueur)

    def attribuerCote(self,cote):
        """Défini le côté d'un joueur, celui-ci peut varier d'une partie à une autre."""
        self.cote=cote
        self.cote_oppose=1-self.cote

    def reinitialiser(self, plateau): # ne sera pas dans le sommaire tant qu'elle ne sera pas défini
        #A compléter par Alexandre
        pass

    def __str__(self):
        """Renvoie une représentation du joueur en string."""
        #Habituellement le joueur ne connait pas sa couleur et ne possede pas de nom
        #mais ce celui-ci connait toujours son coté.
        #Effectivement c'est le plateau qui affiche une couleur prédéfinie dans le thème.
        if "nom" in self.__dict__: #Vérifie si le joueur possede un attribut nom
            text="Joueur"+str(self.nom)
        elif "couleur" in self.__dict__: #Vérifie si le joueur possede un attribut couleur
            #Pourrait fonctionner si l'on créer une classe de couleur
            #mais c'est un peu exagéré.
            text="Joueur"+str(self.couleur)
        else: #Sinon dans la plupart des cas on affiche uniquement son côté.
            text="Joueur"+str(self.cote)
        return text

class Humain(Joueur):
    """classe qui hérite de le classe Joueur"""

    def __init__(self,nom=None):
        """Crée un humain qui hérite de joueur."""
        Joueur.__init__(self,nom)  #Compatibilité avec python2.7 avec cette écriture théoriquement.

    def jouer(self,plateau,fenetre):
        """Le joueur choisi un coup parmi ceux que le plateau lui propose et peux le sélectionner a l'aide de la fenêtre."""
        while fenetre.open:
            fenetre.check()
            curseur=fenetre.point()#Renvoie les coordonnees du curseur
            position=plateau.obtenirPositionPlateau(curseur,fenetre) #Transforme les coordonnees du curseur dans le systeme de coordonnees du plan
            #plateau.afficher(fenetre)
            #plateau.colorerCase(position,couleurs.BLEU,fenetre)
            fenetre.flip()
            click=fenetre.click()
            #print(click,position,plateau.mouvements)
            if click:
                if plateau.estDansGrille(position):
                    if position in plateau.mouvements: #On regarde si le clique est une possibilité propose par le plateau
                        self.choix=position
                        break
        return self.choix

    def __str__(self):
        """Renvoie une représentation du joueur en string."""
        #Habituellement le joueur ne connait pas sa couleur et ne possede pas de nom
        #mais ce celui-ci connait toujours son coté.
        #Effectivement c'est le plateau qui affiche une couleur prédéfinie dans le thème.
        if "nom" in self.__dict__: #Vérifie si le joueur possede un attribut nom
            text="Joueur"+str(self.nom)
        elif "couleur" in self.__dict__: #Vérifie si le joueur possede un attribut couleur
            #Pourrait fonctionner si l'on créer une classe de couleur
            #mais c'est un peu exagéré.
            text="Joueur"+str(self.couleur)
        else: #Sinon dans la plupart des cas on affiche uniquement son type.
            text="Joueur Humain"
        return text


class Robot(Joueur):
    """classe qui hérite de le classe Joueur"""

    def __init__(self,nom=None):
        """Cree un joueur robot qui hérite de joueur. Il s'agit de la classe de base de tous les robots."""
        Joueur.__init__(self,nom) #Compatibilité avec python2.7 avec cette écriture théoriquement.

    def main(self, plateau):
        """"Methode à surcharger"""
        cfg.debug("Random actif, Robot.main n'a pas ete surcharge")
        return self.jouerAleatoire(plateau)

    def jouer(self,plateau,fenetre):
        """Le joueur renvoie un mouvement parmi les mouvements possibles a l'aide du plateau et de la fenetre."""
        return self.main(plateau)#todo verif si c'est bien possible

    def jouerAleatoire(self,plateau):
        """Le joueur choisi un des mouvements possibles aléatoirement."""
        mouvements=plateau.obtenirMouvementsValides(self.cote)
        self.choix=random.choice(mouvements)
        return self.choix

    def __str__(self):
        """Renvoie une représentation du joueur en string."""
        #Habituellement le joueur ne connait pas sa couleur et ne possede pas de nom
        #mais ce celui-ci connait toujours son coté.
        #Effectivement c'est le plateau qui affiche une couleur prédéfinie dans le thème.
        if "nom" in self.__dict__: #Vérifie si le joueur possede un attribut nom
            text="Joueur"+str(self.nom)
        elif "couleur" in self.__dict__: #Vérifie si le joueur possede un attribut couleur
            #Pourrait fonctionner si l'on créer une classe de couleur
            #mais c'est un peu exagéré.
            text="Joueur"+str(self.couleur)
        else: #Sinon dans la plupart des cas on affiche uniquement son type.
            text="Joueur Robot"
        return text

    def distance(self,p1,p2):
        """Renvoie la distance entre les positions p1 et p2."""
        x1,y1=p1
        x2,y2=p2
        return math.sqrt((x1-x2)**2+(y1-y2)**2)

    def distanceDuCentre(self,position,plateau):
        """Renvoie la distance d'une position par rapport au centre."""
        tx,ty=plateau.taille
        centre=(tx/2,ty/2)
        return self.distance(position,centre)

    def distanceTotale(self,pions):
        """Renvoie la somme des distances entre tous les pions 2 à 2."""
        somme=0
        l=len(pions)
        for i in range(l):
            for j in range(i+1,l):
                somme+=self.distance(pions[i],pions[j])
        return somme

    def distanceMoyenne(self,pions):
        """Renvoie la distance moyenne entre tous les pions 2 à 2."""
        nombre_de_distances_calculees=(len(pions)+1)*len(pions)/2
        return self.distanceTotale(pions)/nombre_de_distances_calculees





class Developpeur(Humain):
    """classe qui hérite de le classe Humain"""

    def __init__(self,nom=None):
        Joueur.__init__(self,nom)

    def jouer(self,plateau,panneau):
        """Le joueur choisi un coup parmi ceux que le plateau lui propose et peux le sélectionner a l'aide de la fenêtre."""
        while panneau.open:
            panneau.check()
            #curseur=panneau.point()#Renvoie les coordonnees du curseur
            position=plateau.obtenirPositionPlateau(panneau)
            #position=plateau.obtenirPositionPlateau(curseur,panneau) #Transforme les coordonnees du curseur dans le systeme de coordonnees du plan
            #self.afficher(panneau,plateau,bordure)
            click=panneau.click()
            if click:
                if plateau.estDansGrille(position):
                    self.choix=position
                break
        return self.choix

    def afficher(self,panneau,plateau,bordure):
        """Affiche les éléments sur l'écran car le joueur possède la boucle principale ici."""
        panneau.clear()
        panneau.coller(plateau.surface,0)
        panneau.coller(bordure.surface,1)
        plateau.afficher()
        bordure.afficher()
        panneau.afficher()
        panneau.flip()
