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
################################################################################
#
#                           SOMMAIRE de Fenetre
#
#    1.    class Fenetre:  .......................................... ligne  48
#    1.1   ------> __init__ (self,(etc).)  .......................... ligne  51
#    1.2   ------> load (self)  ..................................... ligne  73
#    1.3   ------> set (self)  ...................................... ligne  78
#    1.4   ------> clear (self,color=None)  ......................... ligne  95
#    1.5   ------> check (self)  .................................... ligne 100
#    1.6   ------> pause (self)  .................................... ligne 117
#    1.7   ------> attendre (self)  ................................. ligne 129
#    1.8   ------> point (self)  .................................... ligne 141
#    1.9   ------> click (self)  .................................... ligne 145
#    1.10  ------> flip (self)  ..................................... ligne 149
#    1.11  ------> infoConsole (self,message)  ...................... ligne 153
#    1.12  ------> __del__ (self)  .................................. ligne 158
#
################################################################################
"""
# --coding:utf-8--

from pygame.locals import RESIZABLE,KEYDOWN,KEYUP,K_r,K_ESCAPE,K_SPACE,FULLSCREEN
# CONSTANTES de pygame

import pygame
import couleurs
import time



class Fenetre:
    """Crée une classe de fenêtre afin de simplifier l'utilisation de pygame."""

    def __init__(self,  nom              = "fenetre",
                        taille           = None,
                        police_du_texte  = "monospace",
                        taille_du_texte  = 65,
                        text_color       = couleurs.BLANC,
                        background_color = couleurs.NOIR,
                        plein_ecran      = False,
                        set              = True):
        """Crée un objet de fenêtre avec son nom, sa taille, sa police de texte,
        sa taille de texte, sa couleur de texte, sa couleur de fond, l'affichage
        en plein écran, et l'affichage sur l'écran dès sa création."""
        self.name            = nom
        self.taille          = taille
        self.police_du_texte = police_du_texte
        self.taille_du_texte = taille_du_texte
        self.text_color      = text_color
        self.couleur_de_fond = background_color
        self.plein_ecran     = plein_ecran
        self.load()
        if set:
            self.set()

    def load(self):
        """Crée les attributs par défaut de la fenêtre."""
        self.pausing         = False
        self.open            = False

    def set(self):
        """Charge la fenêtre sur l'écran."""
        pygame.init() # On initialise la module pygame afin de pouvoir l'utiliser.
        self.info=pygame.display.Info() # On s'en sert pour récupérer la taille de l'écran de l'utilisateur.
        if not self.taille:
            self.taille=(self.info.current_w//2,self.info.current_h//2)
        if self.plein_ecran:
            self.screen=pygame.display.set_mode(self.taille,FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode(self.taille,RESIZABLE)
        self.infoConsole("La fenetre a ete ouverte.")
        self.font=pygame.font.SysFont(self.police_du_texte,self.taille_du_texte) # On charge une police de caractère
        pygame.display.set_caption(self.name) # nom de la fenêtre dans l'en-tête de celle-ci
        self.clear()
        self.flip()
        self.open=True

    def clear(self,color=None):
        """Colorie l'écran de la fenêtre avec la couleur du fond d'écran."""
        if not color: color=self.couleur_de_fond
        self.screen.fill(color)

    def check(self):
        """Mets à jour l'état de la fenêtre en fonction des touches pressés par
        l'utilisateur. Si ce dernier clique sur 'Echap' ou le bouton pour quitter,
         la fenêtre se met dans l'état fermé automatiquement. De même si
         l'utilisateur change la taille de la fenêtre lors de utilisation, sa
         taille est automatiquement redéfinie."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.open=False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.open=False
            if event.type == pygame.VIDEORESIZE and not self.plein_ecran:
                self.taille=[event.w,event.h]
                self.screen=pygame.display.set_mode(self.taille,pygame.RESIZABLE)
                self.flip()

    def pause(self):
        """Permet de mettre le programme en pause jusqu'à ce que l'utilisateur
        appuie sur la barre d'espace."""
        self.pausing=True
        while self.pausing and self.open:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]: # Si on appuie sur la barre d'espace..
                self.pausing=False
        if self.open:
            time.sleep(0.1)

    def attendre(self,temps_maximum=0.5):
        """Permet de mettre le programme en pause pendant une durée déterminée
        mais si l'utilisateur appuie sur la barre d'espace la pause se termine
        prématurément."""
        self.pausing=True
        temps=time.time()
        while self.pausing and self.open and time.time()-temps<temps_maximum:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.pausing=False

    def point(self):
        """Retourne la position du curseur dans le système de coordonnées de la fenêtre."""
        return pygame.mouse.get_pos()

    def click(self):
        """Détermine si l'utilisateur à cliqué sur sa souris."""
        return bool(pygame.mouse.get_pressed()[0])

    def flip(self):
        """Rafraichie l'écran"""
        pygame.display.flip()

    def infoConsole(self,message):
        """Affiche un message depuis la fenêtre."""
        text="["+self.name+"] "+message
        print(text)

    def __del__(self):
        """Affiche que la fenêtre a été fermée à la fermeture de la fenêtre."""
        self.infoConsole("La fenetre a ete fermee.")
