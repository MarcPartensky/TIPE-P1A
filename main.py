from joueur  import Robot, Humain, Developpeur
from panneau import Panneau
from othello import Othello
from cyrano  import Cyrano

import ias
import config as cfg


# CRÉATION DE LA FENETRE
panneau = Panneau(nom="Othello", taille=cfg.RESOLUTION_FENETRE, set=False,plein_ecran=False)  # Crée un panneau (qui est une fenêtre)

# CRÉATION DES JOUEURS

# Création des joueur humain et non naïvent
humain1 = Humain(nom="Humain")   # Crée un joueur humain
humain2 = Humain(nom="Humain2")  # Crée un autre joueur humain
developpeur1 = Developpeur(nom="Developpeur")   # Crée un joueur humain qui n'obéit pas aux règles de l'Othello, cela permet de faire des tests
developpeur2 = Developpeur(nom="Developpeur2")  # Même développeur
machine1 = Cyrano(nom="Cyrano")   # Crée une intelligence artificielle utilisant la notion de stabilite
machine2 = Cyrano(nom="Cyrano2")  # Même ia

# Création des IAs naïvent
machine3 = ias.Interieur(nom="Interieur")  # Joue toujours le plus proche possible du centre du plateau
machine4 = ias.Exterieur(nom="Exterieur")  # Joue toujours le plus loin possible du centre du plateau
machine5 = ias.Groupe(nom="Groupe")  # Joue de façon à former des groupes de pions
machine6 = ias.Eparpille(nom="Eparpille")  # Joue de façon à avoir des pions éparpillés
machine7 = ias.DefinivitementStable(nom="Definivitement Stable")  # Joue les pions définitivement stables si possibles sinon joue aleatoirement
machine8 = ias.Aleatoire(nom="Aleatoire")  # Joue aléatoirement
machine9 = ias.MaximisationPions(nom="MaximisationPions")  # Joue en essayant de maximiser son nombre de pions sur 1 tour seulement

# puis on  choisit les joueurs ici
joueur_noir  = humain1
joueur_blanc = machine1

# et non ici
jeu = Othello(joueurs=[joueur_noir, joueur_blanc],panneau=panneau)  # Crée un jeu. # à noter que le joueur placer en premier dans la liste est le joueur noir
jeu.lancer()  # Lance le jeu.
