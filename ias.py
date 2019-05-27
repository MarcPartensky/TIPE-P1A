#J'essaie de faires des ias naives vite fait ...

import outils
import math

class DefinivitementStable(Robot):
    """Robot qui essaie seulement de maximiser ses pions définitivement stables."""
    def __init__(self,*args,**kwargs):
        """Crée un robot."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en maximisant les pions définivitement stables."""
        stables=plateau.obtenirTousLesPionsDefinitivementStables()
        coups_possibles=plateau.obtenirMouvementsValides()
        intersection=outils.intersection(stables,coups_possibles)
        if intersections:
            choix=intersections[0]
            return choix
        else:
            self.jouerAleatoire(plateau)


class Aleatoire(Robot):
    """Robot qui joue aléatoirement."""
    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue aléatoirement."""
        self.jouerAleatoire(plateau)

class PremierCoup(Robot):
    """Robot qui joue toujours le premier coup parmi les coups proposés."""
    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)
    def jouer(self,plateau,panneau=None):
        """Joue le premier coup proposé."""
        coups_possibles=plateau.obtenirMouvementsValides()
        self.choix=coups_possibles[0]
        return self.choix


class RobotPosition(Robot):
    """Classe mère des robots 'Interieur' et 'Exterieur' qui fournit des fonctions
    supplémentaires pour l'analyse des positions."""

    def distance(self,p1,p2):
        """Renvoie la distance entre les positions p1 et p2."""
        x1,y1=p1
        x2,y2=p2
        return math.sqrt((x1-x2)**2+(y1-y2)**2)

    def distanceDuCentre(self,position):
        """Renvoie la distance d'une position par rapport au centre."""
        tx,ty=plateau.taille
        centre=(tx/2,ty/2)
        return self.distance(position,centre)


class Interieur(RobotPosition):
    """Robot qui essaie de jouer ses pions le plus au centre que possible."""
    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles=plateau.obtenirMouvementsValides()
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusProcheDuCentre(choix,coup)
        return self.choix

    def plusProcheDuCentre(self,p1,p2):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1=self.distanceDuCentre(p1)
        d2=self.distanceDuCentre(p2)
        if d1<d2:
            resultat=d1
        else:
            resultat=d2
        return resultat


class Exterieur(Robot):
    """Robot qui essaie de joueur le plus loin du centre que possible."""
    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles=plateau.obtenirMouvementsValides()
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusLoinDuCentre(choix,coup)
        return self.choix

    def plusLoinDuCentre(self,p1,p2):
        """Renvoie la position la plus proche du centre entre les positions p1 et p2."""
        d1=self.distanceDuCentre(p1)
        d2=self.distanceDuCentre(p2)
        if d1<d2:
            resultat=d2
        else:
            resultat=d1
        return resultat



class Groupe(Robot):
    """Robot qui essaie d'obtenir de placer ses pions en groupes les plus larges possibles."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en plaçant ses pions en groupes si possible."""
        mes_pions=plateau.obtenirPions(self.cote)
        coups_possibles=plateau.obtenirMouvementsValides()

        for coup in coups_possibles:
            pass

    def procheDUnGroupe(self,coup,mes_pions):
        """Renvoie un nombre qui est correspond a la proximité d'un coup 'coup' par rapport
        a un groupe de formé par les pions 'mes_pions'."""
        pass
