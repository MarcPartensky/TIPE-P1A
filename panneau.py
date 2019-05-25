from fenetre import Fenetre
import couleurs

import pygame

class Panneau(Fenetre):
    def __init__(self,nom="Fenetre",taille=None,text_font="monospace",text_size=65,text_color=couleurs.BLANC,background_color=couleurs.NOIR,fullscreen=False,set=True,decoupages=[]):
        """Créer un panneau qui est une fenetre."""
        super().__init__(nom,taille,text_font,text_size,text_color,background_color,fullscreen,set)
        self.decoupages=[] #(px,py,psx,psy),(bx,by,bsx,bsy)


    def coller(self,surface,i):
        """Pose une surface dans le compartiment."""
        sx,sy=surface.get_size()
        dx,dy,dsx,dsy=self.decoupages[i]
        self.screen.blit(surface,(dx,dy))

    def pointer(self):
        pass

    def rect(self,couleurs,dim=(0,0,200,200),fill=0):
        """a suppr..."""
        pygame.draw.rect(self.ecran,couleurs.ROUGE,dim,fill)

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
