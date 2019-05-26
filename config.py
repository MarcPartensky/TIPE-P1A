"""
Module de configuration du script et déclaration de variables constantes nécéssaire
"""
import couleurs
import pygame

CASE_VIDE =   -1   #Ne pas mettre 0 ou 1
DEBUGING  = True
INFO      = True
PLACER    = True

TEMPS_ANIMATION_PION = 0.15

TAILLE_FENETRE=(1200,800)
TAILLE_PLATEAU=(800,800)
TAILLE_BORDURE=(400,800)

RESOLUTION_FENETRE=TAILLE_FENETRE
RESOLUTION_PLATEAU=TAILLE_PLATEAU # les dimensions des arriere_plan comme celle-ci n'ont pas d'importance vu qu'elle seront redimensionnées
RESOLUTION_BORDURE=TAILLE_BORDURE

def bijection(x,ensemble_entree,ensemble_sortie):
    """Renvoie la valeur de f(x) par la bijection de l'ensemble_entree et l'ensemble_sortie."""
    min1,max1=ensemble_entree
    min2,max2=ensemble_sortie
    return (x-min1)/(max1-min1)*(max2-min2)+min2


THEME_BORDURE={
                    "police"          :   "monospace",
                    "couleur texte"   :   couleurs.BLANC,
                    "taille texte"    :   50             }

THEME_PLATEAU={
                    "couleur pieces"       :  [couleurs.BLANC,couleurs.NOIR],
                    "couleur grille"      :   couleurs.NOIR,
                    "couleur mouvement"  :    couleurs.ROUGE,
                    "couleur points"      :   couleurs.NOIR}

THEME_FENETRE={

}





"""
n=min(RESOLUTION_FENETRE)
m=max(RESOLUTION_FENETRE)

RESOLUTION_PLATEAU=(n,n)
RESOLUTION_BORDURE=(m-n,m)
"""

def debug(*txt):
    """Fonction de debug,
    cette fonction est équivalente à un print"""
    if DEBUGING:
        print("[DEBUG]:",*txt)

def info(*txt,nom_fichier="NO_NAME"):
    """Fonction donnant des information en direct sur l'état du programme,
    cette fonction est équivalente à un print.
    Ne pas oublier de donner le nom du fichier dans le quelle la fonction est appeler"""
    if INFO:
        print("[INFO]["+nom_fichier+"]",*txt)
