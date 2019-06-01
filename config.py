"""
Module de configuration du script et déclaration de variables constantes nécéssaire
"""
import couleurs

# CONSTANTES

CASE_VIDE =   -1   # Ne pas mettre 0 ou 1
DEBUGING  = False
INFO      = True

TEMPS_ANIMATION_PION = 0.15

TAILLE_FENETRE = (1200, 800)
TAILLE_PLATEAU = ( 800, 800)
TAILLE_BORDURE = ( 400, 800)


RESOLUTION_FENETRE=TAILLE_FENETRE
RESOLUTION_PLATEAU=TAILLE_PLATEAU # les dimensions des arriere_plan comme celle-ci n'ont pas d'importance vu qu'elle seront redimensionnées
RESOLUTION_BORDURE=TAILLE_BORDURE

THEME_BORDURE = {   "police"             :  "monospace",
                    "couleur texte"      :  couleurs.BLANC,
                    "taille texte"       :  30                }

THEME_PLATEAU = {   "couleur pions"      :  [couleurs.BLANC,couleurs.NOIR],
                    "nom couleur pion"   :  ["BLANC","NOIR"],
                    "couleur grille"     :  couleurs.NOIR,
                    "couleur mouvement"  :  couleurs.ROUGE,
                    "couleur points"     :  couleurs.NOIR     }

THEME_FENETRE = {}


# FONCTION D'AFFICHAGE CONSOLE

def debug(*txt):
    """Fonction de debug, cette fonction n'est qu'un print personaliser."""
    if DEBUGING:
        print("[DEBUG]:",*txt)

def info(*txt,nom_fichier="NO_NAME"):
    """Fonction donnant des information en direct sur l'état du programme,
    Cette fonction n'est qu'un print personaliser.
    Ne pas oublier de donner le nom du fichier dans le quelle la fonction est appeler"""
    if INFO:
        print("[INFOS]["+nom_fichier+"]",*txt)
