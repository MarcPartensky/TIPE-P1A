from fenetre import Fenetre
import couleurs

import pygame

class Panneau(Fenetre):
    def __init__(self,nom="Fenetre",taille=None,text_font="monospace",text_size=65,text_color=couleurs.BLANC,background_color=couleurs.NOIR,fullscreen=False,set=True,decoupages=[]):
        """Créer un panneau qui est une fenetre."""
        super().__init__(nom,taille,text_font,text_size,text_color,background_color,fullscreen,set)
        self.decoupages=[] #(px,py,psx,psy),(bx,by,bsx,bsy)


    def coller(self,surface,compartiment):
        """Pose une surface dans le compartiment."""
        sx,sy=surface.get_size()
        dx,dy,dsx,dsy=self.decoupages[compartiment]
        self.screen.blit(surface,(dx,dy))

    def pointer(self):
        pass

    def afficher(self):
        """Affiche les éléments spécifiques au panneau, c'est à dire par exemple
        la marge entre les différents compartiments."""
        self.afficherCadres()


    def afficherCadres(self):
        """Affiche la marge sur l'écran du panneau qui sépare les zones de découpages."""
        for compartiment in range(len(self.decoupages)):
            self.afficherCadre(compartiment)

    def afficherCadre(self,compartiment,couleur=couleurs.NOIR,l=3):
        """Affiche un cadre autour d'un compartiment."""
        dx,dy,dsx,dsy=self.decoupages[compartiment]
        p1=(dx,dy)
        p2=(dx,dy+dsy)
        p3=(dx+dsx,dy+dsy)
        p4=(dx+dsx,dy)
        pygame.draw.line(self.screen,couleur,p1,p2,l)
        pygame.draw.line(self.screen,couleur,p2,p3,l)
        pygame.draw.line(self.screen,couleur,p3,p4,l)
        pygame.draw.line(self.screen,couleur,p4,p1,l)


    def positionRelative(self):
        """Renvoie la position relative au compartiment dans lequel la souris se place."""
        print("position relative")
        px,py=pygame.mouse.get_pos()
        wsx,wsy=self.taille
        for decoupage in self.decoupages:
            dx,dy,dsx,dsy=decoupage
            if dx<=px<=dx+dsx and dy<=py<=dy+dsy:
                return (dsx*px/wsx+dx,dsy*py/wsy+dy)



if __name__=="__main__":
    panneau=Panneau(taille=[1000,800])
    x,y=panneau.taille
    panneau.decoupages=[(0,0,800,800),(800,0,200,800)]
    s2=pygame.image.load('othelloimage.png')
    #s1=panneau.rect(self.ecran,couleurs.ROUGE,(0,0,80,50),fill=0)
    #s2=panneau.rect(panneau.ecran,couleurs.BLEU,(0,0,50,80),fill=0)
    #panneau.rect(couleurs.BLEU,(0,0,50,50),0)
    s1=s2
    panneau.coller(s1,0)
    panneau.coller(s2,1)
    panneau.flip()
    panneau()
