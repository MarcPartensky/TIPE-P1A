from fenetre import Fenetre

class Panneau(Fenetre):
    def __init__(self,nom="Fenetre",taille=None,text_font="monospace",text_size=65,text_color=WHITE,background_color=BLACK,fullscreen=False,set=True,decoupages=[]):
        """Créer un panneau qui est une fenetre."""
        super().__init__(nom,taille,text_font,text_size,text_color,background_color,fullscreen,set)
        self.decoupages=[] #(px,py,psx,psy),(bx,by,bsx,bsy)


    def coller(self,surface,i):
        """Pose une surface dans le compartiment."""
        self.screen.blit(picture,self.decoupages[i])

    def pointer(self):
        pass

if __name__=="__main__":
    panneau=Panneau()
    x,y=panneau.taille
    panneau.decoupages=[(0,0,x/2,y),(x/2,0,x/2,y)]
    panneau.coller(s1,0)
    panneau.coller(s2,1)
    panneau.flip()
