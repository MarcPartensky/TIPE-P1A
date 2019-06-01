import config as cfg
import pygame, time, couleurs, outils

class Bordure:
    def __init__(self,nombre_de_lignes=20,espacement=40):
        """Créer une bordure en utilisant une surface et un thème."""
        self.surface=pygame.Surface(cfg.RESOLUTION_BORDURE)
        self.espacement=espacement # espace entre deux lignes de texte
        self.lignes=["" for i in range(nombre_de_lignes)]

    def recupererNomDesJoueurs(self,noms_des_joueurs):
        """Permet à la bordure de récupérer le nom des joueurs qu'elle doit afficher."""
        self.noms_des_joueurs=noms_des_joueurs

    def actualiser(self,rang,scores,fini,gagnant):
        """Actualise la bordure."""
        self.rang=rang
        self.tour=rang%2
        self.scores=scores
        self.fini=fini
        self.gagnant=gagnant

    def afficherTexte(self,texte,position,taille=None,couleur=None):
        """Affiche du texte à l'écran."""
        if not couleur: couleur=cfg.THEME_BORDURE["couleur texte"]
        if not taille: taille=cfg.THEME_BORDURE["taille texte"]
        font=pygame.font.SysFont(cfg.THEME_BORDURE["police"],taille)
        surface_texte=font.render(texte,1,couleur)
        self.surface.blit(surface_texte,position)

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
        """Nettoie la surface en recoloriant celle-ci par son arrière plan."""
        self.surface.fill(cfg.THEME_BORDURE["arriere plan"])

    def afficherTemps(self,position,taille=30,couleur=couleurs.BLANC):
        """Affiche l'heure à un instant."""
        heures   = str(time.localtime()[3])
        minutes  = str(time.localtime()[4])
        secondes = str(time.localtime()[5])
        temps=heures+" : "+(2-len(minutes))*"0"+minutes+" : "+(2-len(secondes))*"0"+secondes
        self.afficherTexte(temps,position,taille,couleur)

    def afficherRectangle(self,position,taille,couleur):
        """Affiche un rectangle sur la surface de la bordure avec sa position
        sa taille, et sa couleur."""
        pygame.draw.rect(self.surface,couleur,position+taille,0)

    def afficherTempsPropre(self):
        """Affiche le temps en se souciant de la présentation."""
        #Ne peut pas être utilisé car le temps n'est pas actualisé lorsque les joueurs jouent
        tx,ty=self.surface.get_size()
        self.afficherRectangle((0,0),(tx,70),couleurs.BLEU)
        self.afficherTemps((20,10),couleurs.VERT)

    def afficher(self):
        """Permet d'afficher la bordure sur sa surface."""
        self.afficherFond()
        self.ecrireTitre(0)
        self.ecrireTour(2) # écrit le nom du joueur qui doit jouer à la ligne 1 (prend 2 ligne)
        self.ecrireScore(5) # écrit les scores des joueurs à la ligne 3 (prend 3 lignes)
        if self.fini: self.ecrireGagnants(9)
        self.afficherLignes() # affiche chaque ligne à l'écran

    def ecrireTitre(self,n):
        """Ecrit le titre."""
        self.lignes[n]="                           Othello"

    def ecrireTour(self,n):
        """Ecrit le tour du joueur, utilise 1 ligne"""
        self.lignes[n]="Tour du joueur:"
        self.lignes[n+1]=str(self.noms_des_joueurs[self.tour])

    def ecrireScore(self,n):
        """Ecrit le score à la ligne 'n', utilise 3 lignes"""
        self.lignes[n]="Scores :"
        self.lignes[n+1]=str(self.noms_des_joueurs[0])+" : "+str(self.scores[0])
        self.lignes[n+2]=str(self.noms_des_joueurs[1])+" : "+str(self.scores[1])

    def ecrireGagnants(self,n):
        """Ecrit si la partie est finie ou pas."""
        self.lignes[n]="La partie est finie."
        self.lignes[n+1]="Le gagnant est : "+self.gagnant

    def afficherLignes(self,x=10,y=10):
        """Affiche les lignes du texte sur la surface de la bordure."""
        taille=len(self.lignes)
        for i in range(taille):
            self.afficherTexte(self.lignes[i],(x,y+i*self.espacement))


if __name__=="__main__":
    from panneau import Panneau
    panneau=Panneau()
    bordure=Bordure()
    panneau.decoupages=[(0,0,100,100),(100,0,100,100)]
    while panneau.open:
        panneau.check()
        bordure.surface.fill(couleurs.BLEU)
        bordure.afficherTemps((0,0),40,couleurs.VERT)
        bordure.afficherTexte("message",(10,10),10,couleurs.BLEU)
        panneau.coller(bordure.surface,0)
        panneau.coller(bordure.surface,1)
        panneau.afficher()
        panneau.flip()
