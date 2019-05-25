import config as cfg
import pygame, time, couleurs, outils

class Bordure:
    def __init__(self):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=pygame.Surface(cfg.RESOLUTION_BORDURE)


    def afficherFond(self):
        """Affiche l'arrière plan de la bordure."""
        ftx,fty=self.surface.get_size()
        ftm=max(ftx,fty)
        for y in range(0,fty,10):
            for x in range(0,ftx,10):
                r=int(abs(couleurs.bijection(x,[0,ftx],[0,255])))
                g=int(255-abs(couleurs.bijection((x+y)/2,[0,ftm],[0,255])))
                b=int(abs(couleurs.bijection(y,[0,fty],[0,255])))
                couleur=(r,g,b)
                print(couleur)
                pygame.draw.rect(self.surface,couleur,[x,y,10,10],0)
        self.surface.fill(couleurs.NOIR)

    def clear(self):
        """nettoie la surface en recoloriant celle-ci par son arrière plan"""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTexte(self,texte,position,couleur=None,taille=None):
        """Affiche du texte à l'écran"""
        if not couleur: couleur=cfg.THEME_BORDURE["couleur texte"]
        if not taille: taille=cfg.THEME_BORDURE["taille texte"]
        font=pygame.font.SysFont(cfg.THEME_BORDURE["police"],taille)
        #print("police:",police)
        #font=pygame.font.SysFont(police,taille)
        surface_texte=font.render(texte,1,couleur)
        self.surface.blit(surface_texte,position)

    def afficherTemps(self,position,couleur=None,taille=50):
        """Affiche l'heure à un instant"""
        heure=str(time.localtime()[3])
        minute=str(time.localtime()[4])
        temps=heure+" : "+(2-len(minute))*"0"+minute
        self.afficherTexte(temps,position,couleur,taille)

    def afficherRectangle(self,position,taille,couleur):
        """Affiche un rectangle sur la surface de la bordure avec sa position
        sa taille, et sa couleur."""
        pygame.draw.rect(self.surface,couleur,position+taille,0)

    def error_message(self,message):
        """Permet d'afficher des messages d'erreurs."""
        pass

    def afficher(self):
        """Permet d'afficher la bordure sur sa surface."""
        #self.afficherFond()
        self.afficherRectangle((0,0),(200,70),couleurs.BLEU)
        self.afficherTemps((40,10),couleurs.VERT)



if __name__=="__main__":
    from fenetre import Fenetre
    fenetre=Fenetre()
    surface=pygame.Surface((500,500))
    surface.fill(couleurs.BLEU)
    bordure=Bordure(surface)
    bordure.clear()
    bordure.afficherTemps(0,0,couleurs.VERT)
    bordure.afficherTexte("message",100,100,couleurs.BLEU)
    fenetre.ecran=bordure
    fenetre()
