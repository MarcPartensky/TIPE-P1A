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
#    Créateurs : Alexandre BIGOT
#                Valentin  COLIN
#                Marc  PARTENSKY
#
#    Version : 2019
#
###############################################################################
#
#                           SOMMAIRE du plateau
#
#    1.    Class Simulateur:  ....................................... ligne 38
#    1.1   ------> __init__ (self,theme=None)  ...................... ligne 41
#    1.2   ------> lancer (self)  ................................... ligne 50
#    1.3   ------> __str__ (self)  .................................. ligne 57
#
###############################################################################
"""
# --coding:utf-8--

from othello import Othello
from joueur import Robot,Humain
import ia
import ias
import config as cfg



class Simulateur:
    """Permet de simuler plusieurs parties."""

    def __init__(self,joueurs,nombre_parties=10,fenetre=None):
        """Cree un simulateur de partie avec :
        une fenetre, des joueurs, un nombre de partie.
        """
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
        """Renvoie une représentation des victoires de chaque joueur
        avec l'historique des victoires du simulateur.
        """
        message = "\n\nResultats de " + str(len(self.gagnants)) + " parties:\n"
        for cote in range(len(self.joueurs)):
            message += "- Joueur " + str(self.joueurs[cote]) + " a gagne " + \
                       str(self.gagnants.count(cote)) + " fois.\n"
        pluriel = int(self.gagnants.count(None)>1)
        message += "- Il y a " + str(self.gagnants.count(None)) + " match" + \
                   "s" * pluriel + " nul" + "s" * pluriel + "."
        return message

if __name__=="__main__":
    #from panneau import Panneau
    #panneau=Panneau(taille=cfg.RESOLUTION_FENETRE)

    # Création des joueur humain et non naïvent
    humain1 = Humain(nom="Humain")
    humain2 = Humain(nom="Humain2")
    developpeur1 = Developpeur(nom="Developpeur")
    developpeur2 = Developpeur(nom="Developpeur2")
    machine1 = ia.Cyrano(nom="Cyrano")
    machine2 = ia.Cyrano(nom="Cyrano2")

    # Création des IAs naïvent
    machine3 = ias.Interieur(nom="Interieur")
    machine4 = ias.Exterieur(nom="Exterieur")
    machine5 = ias.Groupe(nom="Groupe")
    machine6 = ias.Eparpille(nom="Eparpille")
    machine7 = ias.DefinivitementStable(nom="Definivitement Stable")
    machine8 = ias.Aleatoire(nom="Aleatoire")
    machine9 = ias.MaximisationPions(nom="MaximisationPions")

    # puis on  choisit les joueurs ici
    joueur_noir  = machine1
    joueur_blanc = machine6
    nombre_parties=50

    simulation=Simulateur([joueur_noir,joueur_blanc],nombre_parties)
    simulation.lancer()
    print(simulation)
