"""
Module de configuration du script et déclaration de variables constantes nécéssaire
"""

CASE_VIDE =   -1   #Ne pas mettre 0 ou 1
DEBUGING  = True
INFO      = True

TEMPS_ANIMATION_PION=0.15

def debug(*txt):
    """fonction de debug,
    cet fonction est équivalente à un print"""
    if DEBUGING:
        print("[DEBUG]:",*txt)

def info(*txt,nom_fichier="NO_NAME"):
    """Fonction donnant des information en direct sur l'état du programme,
    cet fonction est équivalente à un print.
    Ne pas oublier de donner le nom du fichier dans le quelle la fonction est appeler"""
    if INFO:
        print("[INFO]["+nom_fichier+"]",*txt)
