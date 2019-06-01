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
################################################################################
#
#                           SOMMAIRE de Othello
#
#    1.    class Othello:  .......................................... ligne  46
#    1.1   ------> __init__ (self)  ................................. ligne  55
#    1.2   ------> chargerPanneau (self)  ........................... ligne  73
#    1.3   ------> __call__ (self)  ................................. ligne  84
#    1.4   ------> actualiser (self)  ............................... ligne  89
#    1.5   ------> derterminer_gagnant (self)  ...................... ligne 109
#    1.6   ------> afficher (self)  ................................. ligne 123
#    1.7   ------> faireTour (self)  ................................ ligne 133
#
################################################################################
"""
# --coding:utf-8--


from plateau_analysable import PlateauAnalysable as Plateau
from bordure import Bordure

from copy import deepcopy

import couleurs
import config as cfg
import joueur as Joueur


class Othello:
    """Classe de l'Othello.
       Gère la partie du jeu dans sa généralité:
           - initialisation du plateau (où les règles y sont définis)
           - boucle principale du jeu
           - demande au joueur leurs choix à chaque tour
           - demande au plateau et à la bordure de s'afficher dans la fenêtre
           - détermine le gagnant """

    def __init__(self,joueurs,panneau=None,nom="Othello"):
        """Crée un objet de jeu d'Othello en récupérant une liste de joueurs et un panneau (qui est une fenêtre)."""
        self.nom=nom
        self.joueurs=joueurs
        for compteur in range(len(self.joueurs)): # atribut le coté des joueur
            self.joueurs[compteur].attribuerCote(compteur) # i.e. : self.joueurs[compteur].cote=compteur
        self.rang=0 # indique le moment dans la partie. exemple: rang =10 signifie que l'on est au 10ème tours
        self.gagnant=None
        self.historique=[]
        self.plateau=Plateau()
        self.bordure=Bordure()
        self.noms=[joueur.nom for joueur in self.joueurs]
        self.bordure.recupererNomDesJoueurs(self.noms)
        self.ouvert=True
        self.fini=False
        self.panneau=panneau
        if self.panneau: self.chargerPanneau()

    def chargerPanneau(self):
        """Permet de charger la panneau en supposant qu'elle ne soit pas None."""
        self.panneau.nom=self.nom #Donne un nom a la fenêtre.
        self.panneau.set() #Charge la fenêtre créée.
        self.panneau.couleur_de_fond=couleurs.BLANC #Charge la couleur de fond par défaut.
        prx,pry=cfg.RESOLUTION_PLATEAU
        brx,bry=cfg.RESOLUTION_BORDURE
        decoupage1=(0,0,prx,pry)
        decoupage2=(prx,0,prx+brx,bry)
        self.panneau.decoupages=[decoupage1,decoupage2]

    def relancer(self):
        """Relance une  partie."""
        self.recreer()
        self.lancer()

    def recreer(self):
        """Recrée la partie."""
        self.__dict__=Othello(self.joueurs,self.panneau,self.nom).__dict__

    def lancer(self): #Utilisation de la méthode spécial call, executée lorsqu'on appelle une instance de classe comme si c'étais une fonction
        """Boucle principale du jeu Othello."""
        while self.ouvert:
            self.actualiser()

    def actualiser(self):
        """Actualise le jeu."""
        self.bordure.actualiser(self.rang,self.plateau.obtenirScores(),self.fini,self.gagnant)
        if self.panneau:
            self.panneau.check()
            self.ouvert=self.panneau.open
        if not self.plateau.estFini():
            if self.panneau:
                self.afficher()
            self.faireTour()
        else:
            if self.panneau:
                self.afficher()
            else:
                self.ouvert=False
            if not self.fini:
                self.fini=not(self.fini)
                self.determinerGagnant()
                cfg.info("Fin de partie :",nom_fichier="othello.py")
                cfg.info("le gagnant est {}".format(repr(self.gagnant)),nom_fichier="othello.py")

    def determinerGagnant(self):
        """Determine le gagnant de la partie a la fin du jeu."""
        self.cote_gagnant=self.plateau.obtenirCoteGagnant()
        if self.cote_gagnant!=None:
            self.gagnant = self.joueurs[self.cote_gagnant].nom
            cfg.info("Le joueur "+self.gagnant+" a gagne.",nom_fichier="othello.py")

        else:
            cfg.info("Match nul.",nom_fichier="othello.py")
            self.gagnant=None
        #Faire attention au fait que le plateau ne connait que des cotés, et à
        #aucun moment il ne possède les vrais joueurs comme attributs.
        #Effectivement, ce sont les joueurs qui utilise le plateau et non l'inverse.
        return self.gagnant

    def afficher(self):
        """Affiche tout : le plateau et la bordure."""
        self.panneau.clear()
        self.plateau.afficher()
        self.bordure.afficher()
        self.panneau.coller(self.plateau.surface,0)
        self.panneau.coller(self.bordure.surface,1)
        self.panneau.afficher()
        self.panneau.flip()

    def faireTour(self) :
        """Faire un tour de jeu"""
        self.actions_annulees=[]
        self.tour=self.rang%self.plateau.nombre_de_joueurs
        joueur_actif=self.joueurs[self.tour]#joueur a qui c'est le tour
        cfg.debug("C'est au tour du joueur: "+str(joueur_actif))
        self.plateau.charger(self.tour) #Nécessaire pour tous les joueurs
        if self.panneau: self.afficher()
        self.rang+=1
        if len(self.plateau.mouvements)>0:#Si des mouvements sont possibles
            choix_du_joueur=joueur_actif.jouer(deepcopy(self.plateau),self.panneau)
            if not choix_du_joueur:
                return None
            cfg.debug("Le choix du joueur est {}".format(repr(choix_du_joueur)))
            self.plateau.placerPion(choix_du_joueur,joueur_actif.cote)
            self.plateau.afficherAnimationPion(choix_du_joueur)

            #Permet en théorie au joueur de retourner en arrière. Mais n'est pas encore implémenter
            self.historique.append([self.plateau.grille,joueur_actif.cote,choix_du_joueur])
        else :
            #Sinon aucun mouvement n'est possible et on passe au tour suivant
            pass#mot clé python pour indiquer de ne rien faire
