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
#                           SOMMAIRE de Fenetre
#
#    1.    class Fenetre:  ........................................... ligne
#    1.1   ------> __init__ (self,(etc).)  ........................... ligne
#    1.2   ------> load (self)  ...................................... ligne
#    1.3   ------> set (self)  ....................................... ligne
#    1.4   ------> clear (self,color=None)  .......................... ligne
#    1.5   ------> scale (self,picture)  ............................. ligne
#    1.6   ------> check (self)  ..................................... ligne
#    1.7   ------> update (self)  .................................... ligne
#    1.8   ------> pause (self)  ..................................... ligne
#    1.9   ------> attendre (self)  .................................. ligne
#    1.10  ------> point (self)  ..................................... ligne
#    1.11  ------> click (self)  ..................................... ligne
#    1.12  ------> press (self)  ..................................... ligne
#    1.13  ------> flip (self)  ...................................... ligne
#    1.14  ------> afficherTexte (self,text,position,(etc).)  ........ ligne
#    1.15  ------> placerImage (self,position)  ...................... ligne
#    1.16  ------> infoConsole (self,message)  ....................... ligne
#    1.17  ------> __call__ (self)  .................................. ligne
#    1.18  ------> __del__ (self)  ................................... ligne
#
################################################################################
"""
# --coding:utf-8--

import pygame
from pygame.locals import RESIZABLE,KEYDOWN,K_ESCAPE,FULLSCREEN,K_SPACE # CONSTANTES de pygame
import couleurs
import time


class Fenetre:
    def __init__(self,nom="fenetre",
                      taille=None,
                      police_du_texte="monospace",
                      taille_du_texte=65,
                      text_color=couleurs.BLANC,
                      background_color=couleurs.NOIR,
                      plein_ecran=False,
                      set=True):
        """Crée un objet de fenêtre avec son nom, sa taille, sa police de texte,
        sa taille de texte, sa couleur de texte, sa couleur de fond, l'affichage
        en plein écran, et l'affichage sur l'écran dès sa création."""
        self.name=nom
        self.taille=taille
        self.text_font=police_du_texte
        self.taille_du_texte=taille_du_texte
        self.text_color=text_color
        self.couleur_de_fond=background_color
        self.plein_ecran=plein_ecran
        self.load()
        if set:
            self.set()

    def load(self):
        """Crée les attributs par défaut de la fenêtre."""
        self.pausing=False
        self.open=False
        self.picture_saved=0
        self.pause_cool_down=1

    def set(self):
        """Charge la fenêtre sur l'écran."""
        self.infoConsole("Window has been created.")
        pygame.init()
        self.info=pygame.display.Info()
        if not self.taille: self.taille=(self.info.current_w//2,self.info.current_h//2)
        self.font=pygame.font.SysFont(self.text_font, self.taille_du_texte)
        if self.plein_ecran:
            self.screen=pygame.display.set_mode(self.taille,FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode(self.taille,RESIZABLE)
        pygame.display.set_caption(self.name)
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
                self.screen=pygame.display.set_mode(self.size,pygame.RESIZABLE)
                self.flip()

    def update(self):
        """Updates all window's main attributs."""
        self.mouse_click=bool(pygame.mouse.get_pressed()[0])
        self.mouse_position=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.open=False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.open=False

    def pause(self):
        """Permet de mettre le programme en pause jusqu'a ce que l'utilisateur
        appuie sur la barre d'espace"""
        self.pausing=True
        while self.pausing and self.open:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
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

    def press(self):
        """Renvoie la liste des touches avec leurs états:
        0: si la touche n'est pas pressée, 1: sinon."""
        return pygame.key.get_pressed()

    def flip(self):
        """Rafraichie l'écran"""
        pygame.display.flip()

    def placerImage(self,picture_directory,coordonnates,color=None):
        """Permet de placer une image aux coordonnées indiqués."""
        x,y,sx,sy=coordonnates
        picture=pygame.image.load(picture_directory)
        picture=pygame.transform.scale(picture,(sx,sy))
        if color: picture=colorize(picture,color)
        self.screen.blit(picture,(x,y))

    def obtenirTailleTexteAbsolue(self):
        """Renvoie la taille du texte en coordonnées en pixels avec la taille
        du texte de pygame en faisant un calcul arbitraire."""
        return self.taille_du_texte/4

    def afficherTexte(self,text,position,taille=None,couleur=None,couleur_de_fond=None,font=None,marge=1):
        """Affiche du texte à l'écran avec la position les optionnels: taille,
        couleur, couleur de fond, police d'écriture et marge."""
        if not taille: taille=self.taille_du_texte
        if not couleur: couleur=self.text_color
        if not font: font=self.font
        sx,sy=taille
        x,y=position
        pygame.draw.rect(self.screen,couleurs.inverser(couleur_de_fond),list(position)+list(taille),0)
        pygame.draw.rect(self.screen,couleur_de_fond,(x+marge,y+marge,sx-2*marge,sy-2*marge),0)
        label=font.render(text,1,couleur)
        self.screen.blit(label,position)

    def infoConsole(self,message):
        """Print message with window mention."""
        text="["+self.name+"] "+message
        print(text)

    def __call__(self):
        """Rafraîchie la fenêtre et fait la met en pause."""
        self.flip()
        self.pause()

    def __del__(self):
        """Executed before the window is destroyed."""
        self.infoConsole("Window has been closed.")



"""Test d'utilisation et test de la fenetre."""

if __name__=="__main__":
    w=Fenetre("FENETRE TEST")
    #save(w,"grosse fenetre")
    #w=load("grosse fenetre")
    #print(lighten(BLUE))
    #w.alert("test")
    w.pause()
    w.clear()
    w.alert("test2")
    w.attendre(1)
    w.kill()
