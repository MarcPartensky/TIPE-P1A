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
################################################################################
#
#                           SOMMAIRE de Fenetre
#    1.    class DefinivitementStable (Robot):  ..................... ligne  64
#    1.1   ------> __init__ (self,(etc).)  .......................... ligne  67
#    1.2   ------> jouer (self,plateau,panneau=None)  ............... ligne  71
#
#    2.    class Aleatoire (Robot):  ................................ ligne  87
#    2.1   ------> __init__ (self,etc)  ............................. ligne  90
#    2.2   ------> jouer (self,plateau,panneau=None)  ............... ligne  94
#
#    3.    class Interieur (Robot):  ................................ ligne  99
#    3.1   ------> __init__ (self,etc)  ............................. ligne 102
#    3.2   ------> jouer (self,plateau,panneau=None)  ............... ligne 106
#    3.3   ------> plusProcheDuCentre (self,p1,p2,plateau)  ......... ligne 114
#
#    4.    class Exterieur (Robot):  ................................ ligne 125
#    4.1   ------> __init__ (self,etc)  ............................. ligne 128
#    4.2   ------> jouer (self,plateau,panneau=None)  ............... ligne 132
#    4.3   ------> plusLoinDuCentre (self,p1,p2,plateau)  ........... ligne 140
#
#    5.    class Groupe (Robot):  ................................... ligne 151
#    5.1   ------> __init__ (self,etc)  ............................. ligne 154
#    5.2   ------> jouer (self,plateau,panneau=None)  ............... ligne 158
#    5.3   ------> plusProcheDUnGroupe (self,p1,p2,plateau)  ........ ligne 167
#
#    6.    class Eparpille (Robot):  ................................ ligne 179
#    6.1   ------> __init__ (self,etc)  ............................. ligne 182
#    6.2   ------> jouer (self,plateau,panneau=None)  ............... ligne 186
#    6.3   ------> plusLoinDUnGroupe (self,p1,p2,plateau)  .......... ligne 195
#
#    7.    class MaximisationPions (Robot):   ....................... ligne 207
#    7.1   ------> __init__ (self,etc)  ............................. ligne 210
#    7.2   ------> jouer (self,plateau,panneau=None)  ............... ligne 214
#    7.3   ------> meilleurCoup (self,p1,p2,plateau)  ............... ligne 222
#
################################################################################
"""

from joueur import Robot

import config as cfg
import outils
import math
import copy
import random

class DefinivitementStable(Robot):
    """Robot qui essaie seulement de maximiser ses pions définitivement stables."""

    def __init__(self,*args,**kwargs):
        """Crée un robot."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en maximisant les pions définivitement stables."""
        coups_possibles=plateau.mouvements
        stables=[]
        for coup in coups_possibles:
            plateau.insererPion(coup,self.cote)
            if plateau.estUnPionDefinitivementStable(coup,panneau):
                stables.append(coup)
            plateau.insererPion(coup,cfg.CASE_VIDE)
        if len(stables)>0:
            choix=random.choice(stables)
            return choix
        else:
            return self.jouerAleatoire(plateau)


class Aleatoire(Robot):
    """Robot qui joue aléatoirement."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue aléatoirement."""
        return self.jouerAleatoire(plateau)


class Interieur(Robot):
    """Robot qui essaie de jouer ses pions le plus au centre que possible."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles=plateau.mouvements
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusProcheDuCentre(self.choix,coup,plateau)
        return self.choix

    def plusProcheDuCentre(self,p1,p2,plateau):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1=self.distanceDuCentre(p1,plateau)
        d2=self.distanceDuCentre(p2,plateau)
        if d1<d2:
            resultat=p1
        else:
            resultat=p2
        return resultat


class Exterieur(Robot):
    """Robot qui essaie de joueur le plus loin du centre que possible."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles=plateau.mouvements
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusLoinDuCentre(self.choix,coup,plateau)
        return self.choix

    def plusLoinDuCentre(self,p1,p2,plateau):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1=self.distanceDuCentre(p1,plateau)
        d2=self.distanceDuCentre(p2,plateau)
        if d1<d2:
            resultat=p2
        else:
            resultat=p1
        return resultat


class Groupe(Robot):
    """Robot qui essaie de placer ses pions en groupes les plus larges possibles."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en plaçant ses pions en groupes si possible."""
        mes_pions=plateau.obtenirPions(self.cote)
        coups_possibles=plateau.mouvements
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusProcheDUnGroupe(coup,self.choix,coups_possibles)
        return self.choix

    def plusProcheDUnGroupe(self,p1,p2,mes_pions):
        """Renvoie l'une des positions p1 ou p2 pour laquelle la distance totale
        par rapport aux autres pions est la plus faible."""
        d1=self.distanceTotale(mes_pions+[p1])
        d2=self.distanceTotale(mes_pions+[p2])
        if d1>d2:
            resultat=p1
        else:
            resultat=p2
        return resultat


class Eparpille(Robot):
    """Robot qui essaie de placer ses pions de la façon la plus éparpillé possible."""

    def __init__(self,*args,**kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en plaçant ses pions de façon éparpillé si possible."""
        mes_pions=plateau.obtenirPions(self.cote)
        coups_possibles=plateau.mouvements
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusLoinDUnGroupe(coup,self.choix,coups_possibles)
        return self.choix

    def plusLoinDUnGroupe(self,p1,p2,mes_pions):
        """Renvoie l'une des positions p1 ou p2 pour laquelle la distance totale
        par rapport aux autres pions est la plus faible."""
        d1=self.distanceTotale(mes_pions+[p1])
        d2=self.distanceTotale(mes_pions+[p2])
        if d1>d2:
            resultat=p2
        else:
            resultat=p1
        return resultat


class MaximisationPions(Robot):
    """Robot qui joue de façon à avoir le plus de pions possibles sur le tour actuel."""

    def __init__(self,*args,**kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue de façon à avoir le plus de pions possibles sur le tour actuel."""
        coups_possibles=plateau.mouvements
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.meilleurCoup(coup,self.choix,plateau)
        return self.choix

    def meilleurCoup(self,p1,p2,plateau):
        """Renvoie le coup qui permet de récupérer le plus de pions."""
        pl1=copy.deepcopy(plateau)
        pl2=copy.deepcopy(plateau)
        pl1.placerPion(p1,self.cote)
        pl2.placerPion(p2,self.cote)
        n1=pl1.compterPions(self.cote)
        n2=pl2.compterPions(self.cote)
        if n1>n2:
            resultat=p1
        else:
            resultat=p2
        return resultat
