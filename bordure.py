import pygame, time, couleurs
import config as cfg

class Bordure:
    def __init__(self,surface):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=surface

    def clear(self):
        """nettoie la surface en recoloriant celle-ci par son arrière plan"""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTexte(self,texte,position,couleur=None,taille=None):
        """affiche du texte à l'écran"""
        if couleur == None: couleur=cfg.THEME_BORDURE["couleur texte"]
        if taille  == None: taille=cfg.THEME_BORDURE["taille texte"]
        police=pygame.font.SysFont(cfg.THEME_BORDURE["police"],taille)
        surface_texte=font.render(texte,1,couleur)
        self.surface.blit(surface_texte,position)
    """
    def afficherTemps(self,position,couleurs=None,taille=None):
        ""affiche l'heure à un instant""
        heure=str(time.tm_hour)
        minute=str(time.tm_min)
        temps=heure+" : "+minute
        self.afficherTexte(temps,position,couleurs,taille)

    def error_message(self,message):
        pass
    """

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
