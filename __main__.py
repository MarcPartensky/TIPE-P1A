# --coding:utf-8--
from joueur import Robot, Humain, Developpeur
from panneau import Panneau
from othello import Othello

import ia, ias
import config as cfg


############################ CRÉATION DE LA FENETRE ###########################

panneau = Panneau(
    nom="Othello", taille=cfg.RESOLUTION_FENETRE, set=False, plein_ecran=False
)

############################# CRÉATION DES JOUEURS ############################

####### Création des joueur humain et non naïvent #######

# Crée un joueur humain
humain1 = Humain(nom="Humain")
humain2 = Humain(nom="Humain2")

# Crée un joueur humain qui n'obéit pas aux règles de l'Othello
developpeur1 = Developpeur(nom="Developpeur")
developpeur2 = Developpeur(nom="Developpeur2")

# Crée une intelligence artificielle utilisant la notion de stabilite
machine1 = ia.Cyrano(nom="Cyrano")
machine2 = ia.Cyrano(nom="Cyrano2")

######## Création des IAs naïvent ########

# Joue toujours le plus proche possible du centre du plateau
machine3 = ias.Interieur(nom="Interieur")

# Joue toujours le plus loin possible du centre du plateau
machine4 = ias.Exterieur(nom="Exterieur")

# Joue de façon à former des groupes de pions
machine5 = ias.Groupe(nom="Groupe")

# Joue de façon à avoir des pions éparpillés
machine6 = ias.Eparpille(nom="Eparpille")

# Joue les pions définitivement stable si possible sinon joue aleatoirement
machine7 = ias.DefinivitementStable(nom="Definivitement Stable")

# Joue aléatoirement
machine8 = ias.Aleatoire(nom="Aleatoire")

# Joue en essayant de maximiser son nombre de pions sur 1 tour seulement
machine9 = ias.MaximisationPions(nom="MaximisationPions")

############################### CRÉATION DU JEU ###############################

# puis on  choisit les joueurs ici,
joueur_noir = humain1
joueur_blanc = machine1

# et non ici.
# Crée un jeu.
jeu = Othello(joueurs=[joueur_noir, joueur_blanc], panneau=panneau)

############################## LANCEMENT DU JEU ###############################

jeu.lancer()
