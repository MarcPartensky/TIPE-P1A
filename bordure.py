import config as cfg
import pygame, time, couleurs

class Bordure:
    def __init__(self,surface):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=surface

    def clear(self):
        """nettoie la surface en recoloriant celle-ci par son arrière plan"""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTexte(self,texte,position,couleur=None,taille=None):
        """Affiche du texte à l'écran"""
        if couleur == None: couleur=cfg.THEME_BORDURE["couleur texte"]
        if taille  == None: taille=cfg.THEME_BORDURE["taille texte"]
        police=pygame.font.SysFont(cfg.THEME_BORDURE["police"],taille)
        surface_texte=font.render(texte,1,couleur)
        self.surface.blit(surface_texte,position)

    def afficherTemps(self,position,couleurs=None,taille=None):
        """Affiche l'heure à un instant"""
        heure=str(time.localtime()[3])
        minute=str(time.localtime()[4])
        temps=heure+" : "+minute
        self.afficherTexte(temps,position,couleurs,taille)

    def error_message(self,message):
        pass


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
