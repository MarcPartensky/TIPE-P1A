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
#                           SOMMAIRE de Fenetre
#
#    1.    class DefinivitementStable (joueur.Robot): .............. ligne  65
#    1.1   ------> __init__ (self,(etc).)  ......................... ligne  68
#    1.2   ------> jouer (self,plateau,panneau=None)  .............. ligne  72
#
#    2.    class Aleatoire (joueur.Robot):  ........................ ligne  87
#    2.1   ------> __init__ (self,etc)  ............................ ligne  91
#    2.2   ------> jouer (self,plateau,panneau=None)  .............. ligne  95
#
#    3.    class Interieur (joueur.Robot):  ........................ ligne 100
#    3.1   ------> __init__ (self,etc)  ............................ ligne 103
#    3.2   ------> jouer (self,plateau,panneau=None)  .............. ligne 107
#    3.3   ------> plusProcheDuCentre (self,p1,p2,plateau)  ........ ligne 115
#
#    4.    class Exterieur (joueur.Robot):  ........................ ligne 126
#    4.1   ------> __init__ (self,etc)  ............................ ligne 129
#    4.2   ------> jouer (self,plateau,panneau=None)  .............. ligne 133
#    4.3   ------> plusLoinDuCentre (self,p1,p2,plateau)  .......... ligne 141
#
#    5.    class Groupe (joueur.Robot):  ........................... ligne 152
#    5.1   ------> __init__ (self,etc)  ............................ ligne 155
#    5.2   ------> jouer (self,plateau,panneau=None)  .............. ligne 159
#    5.3   ------> plusProcheDUnGroupe (self,p1,p2,plateau)  ....... ligne 168
#
#    6.    class Eparpille (joueur.Robot):  ........................ ligne 180
#    6.1   ------> __init__ (self,etc)  ............................ ligne 183
#    6.2   ------> jouer (self,plateau,panneau=None)  .............. ligne 187
#    6.3   ------> plusLoinDUnGroupe (self,p1,p2,plateau)  ......... ligne 196
#
#    7.    class MaximisationPions (joueur.Robot):   ............... ligne 208
#    7.1   ------> __init__ (self,etc)  ............................ ligne 211
#    7.2   ------> jouer (self,plateau,panneau=None)  .............. ligne 215
#    7.3   ------> meilleurCoup (self,p1,p2,plateau)  .............. ligne 223
#
###############################################################################
"""
# --coding:utf-8--

import config as cfg
import joueur, outils
import math, copy, random


class DefinivitementStable(joueur.Robot):
    """Robot qui essaie seulement de maximiser ses pions définitivement stables."""

    def __init__(self, *args, **kwargs):
        """Crée un robot."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue en maximisant les pions définivitement stables."""
        coups_possibles = plateau.mouvements
        stables = []
        for coup in coups_possibles:
            plateau.insererPion(coup, self.cote)
            if plateau.estUnPionDefinitivementStable(coup, panneau):
                stables.append(coup)
            plateau.insererPion(coup, cfg.CASE_VIDE)
        if len(stables) > 0:
            choix = random.choice(stables)
            return choix
        else:
            return self.jouerAleatoire(plateau)


class Aleatoire(joueur.Robot):
    """Robot qui joue aléatoirement."""

    def __init__(self, *args, **kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue aléatoirement."""
        return self.jouerAleatoire(plateau)


class Interieur(joueur.Robot):
    """Robot qui essaie de jouer ses pions le plus au centre que possible."""

    def __init__(self, *args, **kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles = plateau.mouvements
        self.choix = coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix = self.plusProcheDuCentre(self.choix, coup, plateau)
        return self.choix

    def plusProcheDuCentre(self, p1, p2, plateau):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1 = self.distanceDuCentre(p1, plateau)
        d2 = self.distanceDuCentre(p2, plateau)
        if d1 < d2:
            resultat = p1
        else:
            resultat = p2
        return resultat


class Exterieur(joueur.Robot):
    """Robot qui essaie de joueur le plus loin du centre que possible."""

    def __init__(self, *args, **kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles = plateau.mouvements
        self.choix = coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix = self.plusLoinDuCentre(self.choix, coup, plateau)
        return self.choix

    def plusLoinDuCentre(self, p1, p2, plateau):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1 = self.distanceDuCentre(p1, plateau)
        d2 = self.distanceDuCentre(p2, plateau)
        if d1 < d2:
            resultat = p2
        else:
            resultat = p1
        return resultat


class Groupe(joueur.Robot):
    """Robot qui essaie de placer ses pions en groupes les plus larges possibles."""

    def __init__(self, *args, **kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue en plaçant ses pions en groupes si possible."""
        mes_pions = plateau.obtenirPions(self.cote)
        coups_possibles = plateau.mouvements
        self.choix = coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix = self.plusProcheDUnGroupe(coup, self.choix, coups_possibles)
        return self.choix

    def plusProcheDUnGroupe(self, p1, p2, mes_pions):
        """Renvoie l'une des positions p1 ou p2 pour laquelle
        la distance totale par rapport aux autres pions est la plus faible."""
        d1 = self.distanceTotale(mes_pions + [p1])
        d2 = self.distanceTotale(mes_pions + [p2])
        if d1 > d2:
            resultat = p1
        else:
            resultat = p2
        return resultat


class Eparpille(joueur.Robot):
    """Robot qui essaie de placer ses pions de la façon la plus éparpillé possible."""

    def __init__(self, *args, **kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue en plaçant ses pions de façon éparpillé si possible."""
        mes_pions = plateau.obtenirPions(self.cote)
        coups_possibles = plateau.mouvements
        self.choix = coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix = self.plusLoinDUnGroupe(coup, self.choix, coups_possibles)
        return self.choix

    def plusLoinDUnGroupe(self, p1, p2, mes_pions):
        """Renvoie l'une des positions p1 ou p2 pour laquelle la distance totale
        par rapport aux autres pions est la plus faible."""
        d1 = self.distanceTotale(mes_pions + [p1])
        d2 = self.distanceTotale(mes_pions + [p2])
        if d1 > d2:
            resultat = p2
        else:
            resultat = p1
        return resultat


class MaximisationPions(joueur.Robot):
    """Robot qui joue de façon à avoir le plus de pions possibles sur le tour actuel."""

    def __init__(self, *args, **kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args, **kwargs)

    def jouer(self, plateau, panneau=None):
        """Joue de façon à avoir le plus de pions possibles sur le tour actuel."""
        coups_possibles = plateau.mouvements
        self.choix = coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix = self.meilleurCoup(coup, self.choix, plateau)
        return self.choix

    def meilleurCoup(self, p1, p2, plateau):
        """Renvoie le coup qui permet de récupérer le plus de pions."""
        pl1 = copy.deepcopy(plateau)
        pl2 = copy.deepcopy(plateau)
        pl1.placerPion(p1, self.cote)
        pl2.placerPion(p2, self.cote)
        n1 = pl1.compterPions(self.cote)
        n2 = pl2.compterPions(self.cote)
        if n1 > n2:
            resultat = p1
        else:
            resultat = p2
        return resultat
