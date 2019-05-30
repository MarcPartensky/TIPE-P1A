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
#    1.10  ------> direction (self,temps_maximum=0.5)  ............... ligne
#    1.11  ------> select (self)  .................................... ligne
#    1.12  ------> point (self)  ..................................... ligne
#    1.13  ------> click (self)  ..................................... ligne
#    1.14  ------> press (self)  ..................................... ligne
#    1.15  ------> flip (self)  ...................................... ligne
#    1.16  ------> getPicture (self,picture_directory)  .............. ligne
#    1.17  ------> placePicture (self,picture_directory,coord,..)  ... ligne
#    1.18  ------> centerText (self)  ................................ ligne
#    1.19  ------> alert (self)  ..................................... ligne
#    1.20  ------> print (self,text,position,(etc).)  ................ ligne
#    1.21  ------> drawText (self,text,position,couleur,taille=20)  .. ligne
#    1.22  ------> drawRect (self,coordonnates,color)  ............... ligne
#    1.23  ------> place (self,position)  ............................ ligne
#    1.23  ------> infoConsole (self,message)  ....................... ligne
#    1.23  ------> kill (self)  ...................................... ligne
#    1.23  ------> __str__ (self)  ................................... ligne
#    1.23  ------> __call__ (self)  .................................. ligne
#    1.23  ------> __del__ (self)  ................................... ligne
#
################################################################################
"""
# --coding:utf-8--

import pygame
from pygame.locals import RESIZABLE,KEYDOWN,K_ESCAPE,FULLSCREEN,K_SPACE # CONSTANTES de pygame
import couleurs
import time


class Fenetre:
    draw=pygame.draw # permet juste d'écrire un peu moins dans le code

    def __init__(self,name="fenetre",taille=None,text_font="monospace",text_size=65,text_color=couleurs.BLANC,background_color=couleurs.NOIR,fullscreen=False,set=True):
        """Create a fenetre object using name, taille text_font, text_size, text_color, background and set."""
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
        self.info=pygame.display.Info()
        if not self.taille: self.taille=(self.info.current_w//2,self.info.current_h//2)
        self.font=pygame.font.SysFont(self.text_font, self.taille_du_texte)
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
        if not color: color=self.couleur_de_fond
        self.screen.fill(color)

    def scale(self,picture,taille):
        """Permet de changer la taille d'une surface pygame
        utile pour correctement afficher des objet/image dans
        une surface de dimmension plus petite que la surface par exemple"""
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
                #Ne fonctionne pas je pense
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
        """Permet de mettre le programme en pause
        jusqu'a ce que l'utisateur appuie sur la barre d'espace"""
        self.pausing=True
        while self.pausing and self.open:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.pausing=False
        if self.open:
            time.sleep(0.1)

    def attendre(self,temps_maximum=0.5):
        """Permet de mettre le programme en pause pendant une durée déterminé
        mais si l'utisateur appuie sur la barre d'espace la pause se termine prématurément"""
        self.pausing=True
        temps=time.time()
        while self.pausing and self.open and time.time()-temps<temps_maximum:
            self.check()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.pausing=False

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

    """    un peu inutile pour le TIPE mais permet juste de faire des capture d'écran
    def screenshot(self):
        ""Save picture of the surface.""
        self.picture_saved+=1
        pygame.image.save(self.screen,self.name+"-"+str(self.picture_saved)+".png")
    """

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

    def drawRect(self,coordonnates,color): # inutile ? de plus utilise un attribut self.coordonnates qui n'existe pas !!!!
        """Draw a rectangle on the screen using color and coordonnates relative to window's fiducials."""
        wsx,wsy=self.taille
        wcx,wcy,wcsx,wcsy=self.coordonnates
        rcx,rcy,rcsx,rcsy=coordonnates
        x,y=(rcx-wcx,rcy-wcy)
        w,h=(rcsx*wsx/wcsx,rcsy*wsy/wcsy)
        pygame.draw.rect(self.screen,color,(x,y,w,h),0)

    def infoConsole(self,message):
        """Print message with window mention."""
        text="["+self.name+"] "+message
        print(text)

    def __str__(self):
        """Donne une représentation en string de la fenêtre."""
        text="Fenêtre créé par Marc Partensky afin de faciliter l'utilisation des fonctions de pygame."
        return text

    __repr__=__str__

    def __call__(self):
        """Refresh and pause."""
        self.flip()
        self.pause()

    def __del__(self):
        """Executed before the window is destroyed."""
        self.infoConsole("Window has been closed.")



"""Guide d'utilisation et test de la fenetre."""

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
