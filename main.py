from panneau import Panneau
from othello import Othello

from joueur  import Robot, Humain, Developpeur
import ia, ias

import config as cfg

# CRÉATION DE LA FENETRE
panneau=Panneau(nom="Othello",taille=cfg.RESOLUTION_FENETRE,set=False,plein_ecran=False) # Crée un panneau (qui est une fenêtre)


# CRÉATION DES JOUEURS

# Création des joueur humain et non naïvent
humain1=Humain(nom="Humain1") #Crée un joueur humain.
humain2=Humain(nom="Humain2") #Même humain
developpeur1=Developpeur(nom="Developpeur1") #Crée un joueur humain qui n'obéit pas aux règles de l'Othello, cela permet de faire des tests
developpeur2=Developpeur(nom="Developpeur2") #Même développeur
machine1=ia.IA(nom="Stable1") #Crée une intelligence artificielle utilisant la notion de stabilite
machine2=ia.IA(nom="Stable2") #Même ia

# Création des IAs naïvent
machine3=ias.Interieur(nom="Interieur") #Joue toujours le plus proche possible du centre du plateau
machine4=ias.Exterieur(nom="Exterieur") #Joue toujours le plus loin possible du centre du plateau
machine5=ias.Groupe(nom="Groupe") #Joue de façon à former des groupes de pions
machine6=ias.Eparpille(nom="Eparpille") #Joue de façon à avoir des pions éparpillés
machine7=ias.DefinivitementStable(nom="Definivitement Stable") #Joue les pions définitivement stables si possibles sinon joue aleatoirement
machine8=ias.Aleatoire(nom="Aleatoire1") #Joue aléatoirement
machine9=ias.Aleatoire(nom="Aleatoire2")
machine10=ias.MaximisationPions(nom="Direct") #Joue en essayant de maximiser son nombre de pions sur 1 tour seulement

#puis on  choisit les joueurs ici
joueur_blanc = machine1
joueur_noir  = machine7

#et non ici
jeu=Othello(joueurs=[joueur_blanc,joueur_noir],panneau=panneau) #Crée un jeu. # à noter que le joueur placer en premier dans la liste est le joueur blanc
jeu.lancer() #Lance le jeu.
