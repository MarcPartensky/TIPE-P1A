from othello import Othello
from joueur import Robot,Humain
from bruteforce import BruteForce
from ia import IA
import config as cfg

class Simulateur:
    def __init__(self,joueurs,nombre_parties=10,fenetre=None):
        """Cree un simulateur de partie avec une fenetre, des joueurs, un nombre de partie"""
        self.fenetre=fenetre
        self.nombre_parties=nombre_parties
        self.joueurs=joueurs
        self.affichage=affichage
        self.gagnants=[]

    def __call__(self):
        """Boucle 'for' principale du simulateur."""
        for i in range(self.nombre_parties):
            if self.fenetre: jeu=Othello(self.joueurs,self.fenetre)
            else: jeu=Othello(self.joueurs)
            jeu()
            if not jeu.fenetre.open:
                break
            self.gagnants.append(jeu.gagnant)
            if self.display: print(self)

    def __repr__(self):
        """Renvoie une représentation des victoires de chaque joueur avec l'historice des victoires du simulateur."""
        message="Resultats de "+str(len(self.gagnants))+" parties:\n"
        for numeror in range(len(self.joueurs)):
            message+="- Joueur "+str(numero)+" a gagne "+str(self.gagnants.count(numero))+" fois.\n"
        return message



if __name__=="__main__":
    from panneau import Panneau
    panneau=Panneau(taille=cfg.RESOLUTION_FENETRE)
    joueurs=[IA(),BruteForce(3)]
    nombre_parties=2
    affichage=True
    simulation=Simulateur(joueurs,nombre_parties,panneau)
    simulation()
    print(simulation)
