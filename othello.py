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
#                Alexandre Bigot
#
#    Version : 2019
#              1.1
#
###############################################################################
#
#                           SOMMAIRE de Othello
#
#    note : commenter le script correctement
#
#    0. __init__   ................................................ ligne
#    1. __call__   ................................................ ligne
#    2. finalScene   .............................................. ligne
#    3. getInput   ................................................ ligne
#    4. afficher   ................................................ ligne
#    5. faireTour   ............................................... ligne
#    6. actualiser ................................................ ligne
#    7. chargerPanneau (self,panneau) ............................. ligne
#    8. determinerGagnant (self)
#
###############################################################################
"""
# --coding:utf-8--

from plateau_analysable import PlateauAnalysable as Plateau
from bordure import Bordure

import couleurs
import joueur as Joueur
import time
import pygame
from pygame.locals import *
import config as cfg

from copy import deepcopy

class Othello:
    def __init__(self,joueurs,panneau=None,nom="Othello"):
        """Crée un objet de jeu d'Othello en utilisant sa liste de joueurs, sa panneau et son theme."""
        self.nom=nom
        self.joueurs=joueurs
        for compteur in range(len(self.joueurs)):
            self.joueurs[compteur].attribuerCote(compteur)# i.e. : self.joueurs[compteur].cote=compteur
        self.rang=0
        self.gagnant=None
        self.historique=[]
        self.plateau=Plateau()
        self.bordure=Bordure()
        self.ouvert=True
        self.fini=False
        self.chargerPanneau(panneau)

    def chargerPanneau(self,panneau):
        """Permet de charger la panneau en supposant qu'elle ne soit pas None."""
        self.panneau=panneau
        self.panneau.nom=self.nom #Donne un nom a la fenêtre.
        self.panneau.set() #Charge la fenêtre créée.
        self.panneau.couleur_de_fond=couleurs.BLANC #Charge la couleur de fond par défaut.
        prx,pry=cfg.RESOLUTION_PLATEAU
        brx,bry=cfg.RESOLUTION_BORDURE
        decoupage1=(0,0,prx,pry)
        decoupage2=(prx,0,prx+brx,bry)
        #cfg.
        self.panneau.decoupages=[decoupage1,decoupage2]

    def __call__(self): #Utilisation de la méthode spécial call qui permet de lancer la boucle principale
        """Boucle principale du jeu Othello."""
        if self.panneau: self.afficher()
        while self.ouvert:
            self.actualiser()

    def actualiser(self):
        """Actualise le jeu."""
        if not self.plateau.estFini():
            self.faireTour()
        else:
            if not self.fini:
                self.fini=not(self.fini)
                self.determinerGagnant()
                cfg.info("Fin de partie :",nom_fichier="othello.py")
                cfg.info("le gagnant : {}".format(repr(self.gagnant)),nom_fichier="othello.py")
        if self.panneau:
            self.panneau.check()
            self.ouvert=self.panneau.open
            self.afficher()
            if self.fini:
                self.afficherSceneFinale()


    def determinerGagnant(self):
        """Determine le gagnant de la partie a la fin du jeu."""
        cote_gagnant=self.plateau.obtenirCoteGagnant()
        if cote_gagnant!=None:
            cfg.info("Le joueur "+self.joueurs[cote_gagnant].nom+" a gagne.",nom_fichier="othello.py")
            self.gagnant=self.joueurs[cote_gagnant].nom
        else:
            cfg.info("Match nul.",nom_fichier="othello.py")
            self.gagnant=None
        #Faire attention au fait que le plateau ne connait que des cotés, et à
        #aucun moment il ne possède les vrais joueurs comme attributs.
        #Effectivement, ce sont les joueurs qui utilise le plateau et non l'inverse.
        return self.gagnant

    def afficherSceneFinale(self):
        """Afficher le resultat de la partie une fois qu'elle est terminee.
        Ne peut être exécutée que si la panneau existe."""
        if self.gagnant: #Si il existe un gagnant, l'afficher.
            message=repr(self.gagnant)+" gagne!"
        else: #Sinon, afficher match nul.
            message="Match Nul"
        position=list(self.panneau.centerText(message)) #Centre la position du message, ne fonctionne pas correctement.
        position[0]-=50 #Recentre correctement le message.
        taille=[int(len(message)*self.panneau.taille_du_texte/2.7),70] #Choisie la taille du message.
        self.panneau.print(message,position,taille,color=couleurs.NOIR,couleur_de_fond=couleurs.BLANC) #Affiche le message.
        self.panneau.flip() #Rafraîchie la fenêtre.

    def afficher(self):
        """Affiche tout : le plateau"""
        self.panneau.clear()
        self.panneau.coller(self.plateau.surface,0)
        self.panneau.coller(self.bordure.surface,1)
        self.plateau.afficher()
        self.bordure.afficher()
        self.panneau.afficher()
        self.panneau.flip()

    def faireTour(self) :
        """Faire un tour de jeu"""
        self.tour = self.rang % self.plateau.nombre_de_joueurs
        joueur_actif=self.joueurs[self.tour]#joueur a qui c'est le tour
        self.plateau.charger(self.tour) #Necessaire pour tous les joueurs
        #self.plateau.chargerAnalyse(self.panneau) #Economise du temps de calcul pour les ias qui s'en servent, et peut être affichée pour une démonstration
        self.rang+=1
        if len(self.plateau.mouvements)>=1:#Si des moves sont possibles
            choix_du_joueur=joueur_actif.jouer(deepcopy(self.plateau),self.panneau)
            if not choix_du_joueur:
                return None
            cfg.info("Le choix du joueur est {}".format(repr(choix_du_joueur)),nom_fichier="othello.py")
            if cfg.PLACER: self.plateau.placerPion(choix_du_joueur,joueur_actif.cote)
            self.plateau.afficherAnimationPion(choix_du_joueur)
            self.historique.append([self.plateau.grille,joueur_actif.cote,choix_du_joueur]) #Permet en théorie au joueur de retourner en arrière.
        else :
            #Sinon aucun mouvement n'est possible et on passe uniquement au tour suivant
            pass
