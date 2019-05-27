from joueur import Robot

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
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
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
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
        self.choix=coups_possibles[0]
        return self.choix


class Interieur(Robot):
    """Robot qui essaie de jouer ses pions le plus au centre que possible."""
    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue le coup le plus au centre que possible."""
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
        print(coups_possibles)
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            print(self.choix,coup)
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
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
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
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
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
        coups_possibles=plateau.obtenirMouvementsValides(self.cote)
        self.choix=coups_possibles[0]
        for coup in coups_possibles[1:]:
            self.choix=self.plusLoinDUnGroupe(coup,self.choix,coups_possibles)
        return self.choix

    def plusProcheDUnGroupe(self,p1,p2,mes_pions):
        """Renvoie l'une des positions p1 ou p2 pour laquelle la distance totale
        par rapport aux autres pions est la plus faible."""
        d1=self.distanceTotale(mes_pions+[p1])
        d2=self.distanceTotale(mes_pions+[p2])
        if d1>d2:
            resultat=p2
        else:
            resultat=p1
        return resultat

class Ligne(Robot):
    """Robot qui essaie de maximiser le nombre de lignes formées par ses pions."""

    def __init__(self,*args,**kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue de façon à maximiser le nombre de lignes formées par ses pions."""
        pass

    def estEnLigne(self,ligne):
        """Renvoie si une position est."""

class Direct(Robot):
    """Robot qui joue de façon à avoir le plus de pions possibles sur le tour actuel."""
    def __init__(self,*args,**kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue de façon à avoir le plus de pions possibles sur le tour actuel."""
        coups_possibles=self.obtenirMouvementsValides(self.cote)
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
