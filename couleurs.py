"""
Module de couleurs répertoriant quelques constantes de couleurs RGB/RVB
ainsi que des fonctions simple manipulant ces couleurs RGB/RVB
"""

# CONSTANTE DE COULEURS RGB

BLEU       = (  0,  0,255)
ROUGE      = (255,  0,  0)
VERT       = (  0,255,  0)
VERT_FONCE = (  0,100,  0)
NOIR       = (  0,  0,  0)
BLANC      = (255,255,255)
JAUNE      = (255,255,  0)
VIOLET     = (100,  0,100)
ORANGE     = (255,200,  0)
ROSE       = (255,192,203)
BEIGE      = (199,175,138)


# FONCTIONS SIMPLE MANIPULANT DES COULEURS

inverser = lambda couleur : tuple([ 255-c for c in couleur ])
