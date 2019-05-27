from panneau import Panneau
from othello import Othello
from joueur import Robot,Humain,Developpeur

import ia
import ia2
import ias
import bruteforce as bf
import config as cfg

"""
A faire:

FAire API pour IA avec des fonctions 'basique' comme :
Replacer les grille[y][x] par des grille[x][y]

Faire la methode  colorer_case dans board.py

faire ia basique : gestion des priorites : structure

Penser à faire une class "Coup" ou "Mouvement" qui prend un parametre une pos, une couleur

La plupart des methode de board.py qui retourne une liste de coo, retourne une liste de liste : autrement dit, les coo sont dans des liste et non des tuples => il faut chager ca et mettre les coo dans des tuples


Pour marc :9
Indiquer dans la fenetre à qui c'est le tour
La fonction board.conquerir doit renvoyer le nombre de pion retourne

Ajouter les 4 points noirs sur le plateau.
Ajouter un menu très basique => nouvelle class est nouveau fichier .py

Pour dossier :
expliquer demarche dans cahier de bord
Faire mini schema des heritage de classe
"""


if __name__=="__main__": #Ceci est exécuté uniquement si le fichier est exécuté directement depuis ce fichier et non depuis un autre fichier.

    panneau=Panneau(nom="Othello",taille=cfg.RESOLUTION_FENETRE,set=False,fullscreen=False) # Crée une fenêtre

    #On crée des joueurs ici

    humain1=Humain(nom="Humain1") #Crée un joueur humain.
    humain2=Humain(nom="Humain2") #Même humain
    developpeur1=Developpeur(nom="Developpeur1") #Crée un joueur humain qui n'obéit pas aux règles de l'Othello, cela permet de faire des tests
    developpeur2=Developpeur(nom="Developpeur2") #Même développeur
    machine1=ia.IA(nom="Stable1") #Crée une intelligence artificielle utilisant la notion de stabilite
    machine2=ia.IA(nom="Stable2") #Même ia
    machine3=ias.Interieur(nom="Interieur") #Joue toujours le plus proche possible du centre du plateau
    machine4=ias.Exterieur(nom="Exterieur") #Joue toujours le plus loin possible du centre du plateau
    machine5=ias.Groupe(nom="Groupe") #Joue de façon à former des groupes de pions
    machine6=ias.Eparpille(nom="Eparpille") #Joue de façon à avoir des pions éparpillés
    machine7=ias.DefinivitementStable(nom="Definivitement Stable") #Joue les pions définitivement stables si possibles sinon joue aleatoirement
    machine8=ias.Aleatoire(nom="Aleatoire") #Joue aléatoirement
    machine9=ias.PremierCoup(nom="Premier Coup") #Joue toujours le premier coup parmi ceux proposé
    machine10=ias.Direct(nom="Direct") #Joue en essayant de maximiser son nombre de pions sur 1 tour seulement
    bruteforce1=bf.BruteForce(nom="Brute Force niveau 1", level=1) #Crée une machine utilisant la force de calcul de la machine, cela est utile pour les tests de niveau des nouvelles intelligences artificielles.
    bruteforce2=bf.BruteForce(nom="Brute Force niveau 2", level=2) #Joue en pensant 2 coups à l'avance
    bruteforce3=bf.BruteForce(nom="Brute Force niveau 3",level=3)  #Joue en pensant 3 coups à l'avance

    #puis on  choisit les joueurs ici
    joueur_blanc = developpeur1
    joueur_noir  = bruteforce1

    #et non ici
    jeu=Othello(joueurs=[joueur_blanc,joueur_noir],panneau=panneau) #Crée un jeu. # à noter que le joueur placer en premier dans la liste est le joueur blanc
    jeu() #Lance le jeu.
