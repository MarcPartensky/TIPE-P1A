"""
###############################################################################
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
#                           SOMMAIRE de Othello
#
#    1.    class Othello:  ......................................... ligne  46
#    1.1   ------> __init__ (self)  ................................ ligne  55
#    1.2   ------> chargerPanneau (self)  .......................... ligne  75
#    1.3   ------> recreer (self)  ................................. ligne  86
#    1.4   ------> relancer (self) ................................. ligne  91
#    1.3   ------> lancer (self)  .................................. ligne  95
#    1.4   ------> actualiser (self)  .............................. ligne 100
#    1.5   ------> determiner_gagnant (self)  ...................... ligne 123
#    1.6   ------> afficher (self)  ................................ ligne 140
#    1.7   ------> faireTour (self)  ............................... ligne 150
#
###############################################################################
"""
# --coding:utf-8--

from plateau_analysable import PlateauAnalysable as Plateau
from bordure import Bordure

from copy import deepcopy

import couleurs
import time
import config as cfg
import joueur as Joueur


class Othello:
    """Classe de l'Othello.
    Gère la partie du jeu dans sa généralité:
        - initialisation du plateau (où les règles y sont définis)
        - boucle principale du jeu
        - demande au joueur leurs choix à chaque tour
        - demande au plateau et à la bordure de s'afficher dans la fenêtre
        - détermine le gagnant"""

    def __init__(self, joueurs, panneau=None, nom="Othello"):
        """Crée un objet de jeu d'Othello en récupérant
        une liste de joueurs et un panneau (qui est une fenêtre).
        """
        self.nom = nom
        self.joueurs = joueurs
        for compteur in range(len(self.joueurs)):  # Attribut le coté des joueur
            self.joueurs[compteur].attribuerCote(compteur)
        self.rang = 0  # Indique le numéro du tour dans la partie
        self.gagnant = None
        self.historique = []
        self.plateau = Plateau()
        self.bordure = Bordure()
        self.noms = [joueur.nom for joueur in self.joueurs]
        self.bordure.recupererNomDesJoueurs(self.noms)
        self.ouvert = True
        self.fini = False
        self.panneau = panneau
        if self.panneau:
            self.chargerPanneau()

    def chargerPanneau(self):
        """Permet de charger la panneau"""
        self.panneau.nom = self.nom  # Donne un nom a la fenêtre.
        self.panneau.set()  # Charge la fenêtre créée.
        self.panneau.couleur_de_fond = couleurs.BLANC  # Charge le fond par défaut.
        prx, pry = cfg.RESOLUTION_PLATEAU
        brx, bry = cfg.RESOLUTION_BORDURE
        decoupage1 = (0, 0, prx, pry)
        decoupage2 = (prx, 0, prx + brx, bry)
        self.panneau.decoupages = [decoupage1, decoupage2]

    def relancer(self):
        """Relance une partie."""
        self.recreer()
        self.lancer()

    def recreer(self):
        """Recrée la partie."""
        self.__dict__ = Othello(self.joueurs, self.panneau, self.nom).__dict__

    def lancer(self):
        """Boucle principale du jeu Othello."""
        while self.ouvert:
            self.actualiser()

    def actualiser(self):
        """Actualise le jeu."""
        self.bordure.actualiser(
            self.rang, self.plateau.obtenirScores(), self.fini, self.gagnant
        )
        if self.panneau:
            self.panneau.check()
            self.ouvert = self.panneau.open
        if not self.plateau.estFini():
            if self.panneau:
                self.afficher()
            self.faireTour()
        else:
            if not self.fini:
                self.fini = not (self.fini)
                self.determinerGagnant()
                cfg.info(
                    "Fin de partie : Le gagnant est {}".format(repr(self.gagnant)),
                    nom_fichier="othello.py",
                )
            if self.panneau:
                self.afficher()
            else:
                self.ouvert = False

    def determinerGagnant(self):
        """Détermine le gagnant de la partie à la fin du jeu."""
        self.cote_gagnant = self.plateau.obtenirCoteGagnant()
        if self.cote_gagnant != None:
            self.gagnant = self.joueurs[self.cote_gagnant].nom
            cfg.info(
                "Le joueur " + self.gagnant + " a gagne.", nom_fichier="othello.py"
            )
        else:
            cfg.info("Match nul.", nom_fichier="othello.py")
            self.gagnant = None

        # Faire attention au fait que le plateau ne connait que des cotés, et à
        # aucun moment il ne possède les vrais joueurs comme attributs.
        # Effectivement,
        # ce sont les joueurs qui utilise le plateau et non l'inverse.
        return self.gagnant

    def afficher(self):
        """Affiche tout: le plateau et la bordure."""
        self.panneau.clear()
        self.plateau.afficher()
        self.bordure.afficher()
        self.panneau.coller(self.plateau.surface, 0)
        self.panneau.coller(self.bordure.surface, 1)
        self.panneau.afficher()
        self.panneau.flip()

    def faireTour(self):
        """Faire un tour de jeu."""
        self.actions_annulees = []
        self.tour = self.rang % self.plateau.nombre_de_joueurs
        joueur_actif = self.joueurs[self.tour]  # Joueur à qui c'est le tour.
        cfg.debug("C'est au tour du joueur: " + str(joueur_actif))
        self.plateau.charger(self.tour)  # Nécessaire pour tous les joueurs.
        if self.panneau:
            self.afficher()
        self.rang += 1
        if len(self.plateau.mouvements) > 0:  # Si des mouvements sont possibles.
            choix_du_joueur = joueur_actif.jouer(deepcopy(self.plateau), self.panneau)
            if not choix_du_joueur:
                return None
            cfg.debug("Le choix du joueur est {}".format(str(choix_du_joueur)))
            self.plateau.insererPion(choix_du_joueur, joueur_actif.cote)
            self.animer(choix_du_joueur)
            self.plateau.conquerir(choix_du_joueur, joueur_actif.cote)
            # Sauvegarde l'historique du jeu.
            self.historique.append(
                [self.plateau.grille, joueur_actif.cote, choix_du_joueur]
            )
        else:
            # Sinon aucun mouvement n'est possible et on passe au tour suivant.
            pass  # Mot clé Python pour indiquer de ne rien faire.

    def animer(self, choix):
        """Permet d'animer les pions placés."""
        for i in range(3):
            self.plateau.afficher()
            if i % 2 == 0:
                self.plateau.afficherAnimation(choix)
            self.panneau.coller(self.plateau.surface, 0)
            self.panneau.afficher()
            self.panneau.flip()
            self.panneau.attendre(0.1)
