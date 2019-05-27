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
    """Classe mère de robot qui fournit des fonctions supplémentaires pour
    l'analyse des positions et des distances."""

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



class Groupe(RobotPosition):
    """Robot qui essaie de placer ses pions en groupes les plus larges possibles."""

    def __init__(self,*args,**kwargs):
        """Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en plaçant ses pions en groupes si possible."""
        mes_pions=plateau.obtenirPions(self.cote)
        coups_possibles=plateau.obtenirMouvementsValides()
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
        coups_possibles=plateau.obtenirMouvementsValides()
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

class Ligne(RobotPosition):
    """Robot qui essaie de maximiser le nombre de lignes formées par ses pions."""

    def __init__(self,*args,**kwargs):
        """"Crée le robot avec les arguments de la classe mère 'Robot'."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue de façon à maximiser le nombre de lignes formées par ses pions."""
        pass

    def estEnLigne(self,position,ligne):
        """Renvoie si une position est."""
