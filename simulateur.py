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
#                           SOMMAIRE du plateau
#
#    1.    Class Simulateur:  ........................................ ligne 38
#    1.1   ------> __init__ (self,theme=None)  ....................... ligne 41
#    1.2   ------> lancer (self)  .................................... ligne 48
#    1.3   ------> __str__ (self)  ................................... ligne 55
#
###############################################################################
"""
# --coding:utf-8--

from othello import Othello
from joueur import Robot,Humain
import ia, ias
import config as cfg



class Simulateur:
    """Permet de simuler plusieurs parties."""

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
    joueurs=[ias.Aleatoire(nom="MaximisationPions"),ia.Cyrano(nom="Cyrano")]
    nombre_parties=10
    simulation=Simulateur(joueurs,nombre_parties)
    simulation.lancer()
    print(simulation)
