import config as cfg
import pygame, time, couleurs, outils

class Bordure:
    def __init__(self):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=pygame.Surface(cfg.RESOLUTION_BORDURE)
        self.texte=""

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
                pygame.draw.rect(self.surface,couleur,[x,y,10,10],0)

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
        heures=str(time.localtime()[3])
        minutes=str(time.localtime()[4])
        secondes=str(time.localtime()[5])
        temps=heures+" : "+(2-len(minutes))*"0"+minutes+" : "+(2-len(secondes))*"0"+secondes
        self.afficherTexte(temps,position,couleur,taille)

    def afficherRectangle(self,position,taille,couleur):
        """Affiche un rectangle sur la surface de la bordure avec sa position
        sa taille, et sa couleur."""
        pygame.draw.rect(self.surface,couleur,position+taille,0)

    def error_message(self,message):
        """Permet d'afficher des messages d'erreurs."""
        pass

    def afficherTempsPropre(self):
        """Affiche le temps en se souciant de la présentation."""
        tx,ty=self.surface.get_size()
        self.afficherRectangle((0,0),(tx,70),couleurs.BLEU)
        self.afficherTemps((20,10),couleurs.VERT)

    def afficherTextePropre(self):
        """Affiche le texte contenu dans la bordure proprement."""
        position=(50,0)
        self.afficherTexte(self.texte,position)

    def afficher(self):
        """Permet d'afficher la bordure sur sa surface."""
        self.afficherFond()
        #self.afficherTempsPropre()
        #self.texte+="test\n"
        self.afficherTextePropre()




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
