from othello import Othello
from joueur import Robot,Humain
from ia import IA
from ias import Aleatoire
import config as cfg

class Simulateur:
    def __init__(self,joueurs,nombre_parties=10,fenetre=None):
        """Cree un simulateur de partie avec une fenetre, des joueurs, un nombre de partie"""
        self.fenetre=fenetre
        self.nombre_parties=nombre_parties
        self.joueurs=joueurs
        self.gagnants=[]

    def lancer(self):
        """Boucle 'for' principale du simulateur."""
        jeu=Othello(self.joueurs,self.fenetre)
        for i in range(self.nombre_parties):
            jeu.relancer()
            self.gagnants.append(jeu.cote_gagnant)

    def __str__(self):
        """Renvoie une représentation des victoires de chaque joueur avec l'historice des victoires du simulateur."""
        message="\n\nResultats de "+str(len(self.gagnants))+" parties:\n"
        for cote in range(len(self.joueurs)):
            message+="- Joueur "+str(self.joueurs[cote])+" a gagne "+str(self.gagnants.count(cote))+" fois.\n"
        pluriel=int(self.gagnants.count(None)>1)
        message+="- Il y a "+str(self.gagnants.count(None))+" match"+"s"*pluriel+" nul"+"s"*pluriel+"."
        return message



if __name__=="__main__":
    from panneau import Panneau
    #panneau=Panneau(taille=cfg.RESOLUTION_FENETRE)
    joueurs=[IA(nom="Cyrano"),Aleatoire(nom="Aleatoire")]
    nombre_parties=10
    simulation=Simulateur(joueurs,nombre_parties)
    simulation.lancer()
    print(simulation)
