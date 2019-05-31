import config as cfg
import pygame, time, couleurs, outils

class Bordure:
    def __init__(self):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=pygame.Surface(cfg.RESOLUTION_BORDURE)
        self.texte=""

    def recupererNomDesJoueurs(self,noms_des_joueurs):
        """Permet à la bordure de récupérer le nom des joueurs qu'elle doit afficher."""
        self.noms_des_joueurs=noms_des_joueurs

    def actualiser(self,tour):
        """Actualise la bordure."""
        self.tour=tour

    def afficherFond(self):
        """Affiche l'arrière plan de la bordure."""
        ftx,fty=self.surface.get_size()
        ftm=max(ftx,fty)
        for y in range(0,fty,10):
            for x in range(0,ftx,10):
                r=int(abs(outils.bijection(x,[0,ftx],[0,255])))
                g=int(255-abs(outils.bijection((x+y)/2,[0,ftm],[0,255])))
                b=int(abs(outils.bijection(y,[0,fty],[0,255])))
                couleur=(r,g,b)
                pygame.draw.rect(self.surface,couleur,[x,y,10,10],0)

    def clear(self):
        """nettoie la surface en recoloriant celle-ci par son arrière plan"""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTexte(self,texte,position,taille=None,couleur=None):
        """Affiche du texte à l'écran"""
        if not couleur: couleur=cfg.THEME_BORDURE["couleur texte"]
        if not taille: taille=cfg.THEME_BORDURE["taille texte"]
        font=pygame.font.SysFont(cfg.THEME_BORDURE["police"],taille)
        #print("police:",police)
        #font=pygame.font.SysFont(police,taille)
        surface_texte=font.render(texte,1,couleur)
        self.surface.blit(surface_texte,position)

    def afficherTemps(self,position,taille=30,couleur=couleurs.BLANC):
        """Affiche l'heure à un instant"""
        heures=str(time.localtime()[3])
        minutes=str(time.localtime()[4])
        secondes=str(time.localtime()[5])
        temps=heures+" : "+(2-len(minutes))*"0"+minutes+" : "+(2-len(secondes))*"0"+secondes
        self.afficherTexte(temps,position,taille,couleur)

    def afficherRectangle(self,position,taille,couleur):
        """Affiche un rectangle sur la surface de la bordure avec sa position
        sa taille, et sa couleur."""
        pygame.draw.rect(self.surface,couleur,position+taille,0)

    def error_message(self,message):
        """Permet d'afficher des messages d'erreurs."""
        raise NotImplementedError

    def afficherTempsPropre(self):
        """Affiche le temps en se souciant de la présentation."""
        #Ne peut pas être utilisé car le temps n'est pas actualisé lorsque les joueurs jouent
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
        #self.afficherTempsPropre() #Pas utilisable
        self.afficherTextePropre()
        self.afficherTourPropre()

    def afficherTourPropre(self):
        """Affiche qui est le joueur qui doit jouer."""
        self.afficherTour((10,10))

    def afficherTour(self,position,taille=30,couleur=couleurs.BLANC):
        """Affiche le tour et la personne qui doit joueur."""
        texte="Tour du joueur: "+str(self.noms_des_joueurs[self.tour])
        self.afficherTexte(texte,position,taille,couleur)




if __name__=="__main__":
    from panneau import Panneau
    panneau=Panneau()
    #surface=pygame.Surface((500,500))
    #surface.fill(couleurs.BLEU)
    bordure=Bordure()
    panneau.decoupages=[(0,0,100,100),(100,0,100,100)]
    #bordure.clear()
    bordure.surface.fill(couleurs.BLEU)
    bordure.afficherTemps((0,0),40,couleurs.VERT)
    bordure.afficherTexte("message",(10,10),10,couleurs.BLEU)
    panneau.coller(bordure.surface,0)
    panneau.coller(bordure.surface,1)
    panneau.afficher()
    panneau.flip()
    panneau()
