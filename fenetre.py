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
#                Alexandre Bigot
#
#    Version : 2019
#
################################################################################
#
#                           SOMMAIRE de fenetre
#
#    0. class Fenetre   .............................................. ligne
#    1.    ................................................ ligne
#    2.    .............................................. ligne
#    3.    ................................................ ligne
#    4.    ................................................ ligne
#    5.    ............................................... ligne
#
################################################################################
"""
# --coding:utf-8--

from __future__ import division

import couleurs

import pygame
from pygame.locals import *
import time
import json



class Fenetre:
    made=0
    draw=pygame.draw
    def __init__(self,name="Window Name",taille=None,text_font="monospace",text_size=65,text_color=couleurs.BLANC,background_color=couleurs.NOIR,fullscreen=False,set=True):
        """Create a fenetre object using name, taille text_font, text_size, text_color, background and set."""
        Fenetre.made+=1
        self.number=Fenetre.made
        self.name=name
        self.taille=taille
        self.text_font=text_font
        self.taille_du_texte=text_size
        self.text_color=text_color
        self.couleur_de_fond=background_color
        self.fullscreen=fullscreen
        self.load()
        if set:
            self.set()

    def load(self):
        """Load builtins attributs of fenetre object."""
        self.pausing=False
        self.open=False
        self.picture_saved=0
        self.pause_cool_down=1

    def set(self):
        """Creates apparent window."""
        self.infoConsole("Window has been created.")
        pygame.init()
        self.info = pygame.display.Info()
        if not self.taille: self.taille=(self.info.current_w//2,self.info.current_h//2)
        self.font = pygame.font.SysFont(self.text_font, self.taille_du_texte)
        if self.fullscreen:
            self.screen=pygame.display.set_mode(self.taille,FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode(self.taille,RESIZABLE)
        pygame.display.set_caption(self.name)
        self.clear()
        self.flip()
        self.open=True

    def clear(self,color=None):
        """Clear to background color."""
        if not color:
            color=self.couleur_de_fond
        self.screen.fill(color)

    def scale(self,picture,taille):
        """Return scaled picture using picture and taille."""
        return pygame.transform.scale(picture,taille)

    def check(self):
        """Update window's state depending if close buttons are pressed."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.open=False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.open=False
            if event.type == pygame.VIDEORESIZE and not self.fullscreen:
                # There's some code to add back window content here.
                self.size=[event.w,event.h]
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
        """Wait for user to click on space."""
        self.pausing=True
        while self.pausing and self.open:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.pausing=False
        if self.open:
            time.sleep(0.1)

    def attendre(self,temps_maximum=0.5):
        """Wait for user to click on space."""
        self.pausing=True
        temps=time.time()
        while self.pausing and self.open and time.time()-temps<temps_maximum:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.pausing=False


    def select(self):
        """Wait for user to click on screen, then return cursor position."""
        while self.open:
            self.check()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    return (event.pos[0],event.pos[1])

    def point(self):
        """Return cursor position on screen."""
        return pygame.mouse.get_pos()

    def click(self):
        """Return bool value for clicking on screen."""
        return bool(pygame.mouse.get_pressed()[0])

    def press(self):
        """Return bool value for clicking on screen."""
        return pygame.key.get_pressed()

    def flip(self):
        """Refresh screen."""
        pygame.display.flip()

    def screenshot(self):
        """Save picture of the surface."""
        self.picture_saved+=1
        pygame.image.save(self.screen,self.name+"-"+str(self.picture_saved)+".png")

    def getPicture(self,picture_directory):
        """Return picture using picture directory."""
        return pygame.image.load(picture_directory)

    def placePicture(self,picture_directory,coordonnates,color=None):
        """Draw a picture on screen using pygame picture directory and position."""
        x,y,sx,sy=coordonnates
        picture=pygame.image.load(picture_directory)
        picture=pygame.transform.scale(picture,(sx,sy))
        if color is not None:
            picture=colorize(picture,color)
        self.screen.blit(picture, position)

    def centerText(self,message,taille=None):
        """Center the text in the middle of the screen."""
        sx,sy=self.taille
        if not taille: taille=self.taille_du_texte
        l=len(message)
        letter_size=taille/4
        x=sx//2-letter_size*l//2
        y=sy//2-taille/3
        return (int(x),int(y))

    def alert(self,message):
        """Quickly display text on window."""
        position=self.centerText(message)
        self.print(message,position,color=couleurs.NOIR,couleur_de_fond=couleurs.BLANC)
        self.flip()

    def print(self,text,position,taille=None,color=None,couleur_de_fond=None,font=None):
        """Display text on screen using position, taille, color and font."""
        if not taille: taille=self.taille_du_texte
        if not color: color=self.text_color
        if not font: font=self.font
        sx,sy=taille
        x,y=position
        pygame.draw.rect(self.screen,couleurs.inverser(couleur_de_fond),list(position)+list(taille),0)
        pygame.draw.rect(self.screen,couleur_de_fond,(x+1,y+1,sx-2,sy-2),0)
        label=font.render(text,1,color)
        self.screen.blit(label,position)

    def drawText(self,text,position,couleur,taille=20):
        """Display text on screen."""
        font=pygame.font.SysFont(self.text_font,taille)
        label=font.render(text,1,couleur)
        self.screen.blit(label,position)

    def drawRect(self,coordonnates,color):
        """Draw a rectangle on the screen using color and coordonnates relative to window's fiducials."""
        wsx,wsy=self.taille
        wcx,wcy,wcsx,wcsy=self.coordonnates
        rcx,rcy,rcsx,rcsy=coordonnates
        x,y=(rcx-wcx,rcy-wcy)
        w,h=(rcsx*wsx/wcsx,rcsy*wsy/wcsy)
        pygame.draw.rect(self.screen,color,(x,y,w,h),0)

    def place(self,position):
        """Return position relative to window's fiducials."""
        wcx,wcy,wcsx,wcsy=self.coordonnates
        pcx,pcy=position
        x,y=(rcx-wcx,rcy-wcy)
        return (x,y)

    def __str__(self):
        """Donne une représentation en string de la fenêtre."""
        text="Fenêtre créé par Marc Partensky afin de faciliter l'utilisation des fonctions de pygame."
        return text

    __repr__=__str__

    def kill(self):
        """Quit pygame."""
        pygame.quit()

    def infoConsole(self,message):
        """Print message with window mention."""
        text="["+self.name+"] "+message
        print(text)

    def __del__(self):
        """Executed before the window is destroyed."""
        self.infoConsole("Window has been closed.")

    def __call__(self):
        """Refresh and pause."""
        self.flip()
        self.pause()


"""Guide d'utilisation et test de la fenetre."""

if __name__=="__main__":
    w=Fenetre("WINDOW TEST")
    #save(w,"grosse fenetre")
    #w=load("grosse fenetre")
    #print(lighten(BLUE))
    #w.alert("test")
    w.pause()
    w.clear()
    w.alert("test2")
    w.attendre(1)
    w.kill()
