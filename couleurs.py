"""
Module de variable de couleurs répertoriant des triplet de de valeurs RGB/RVB usuels
couleurs écrites en majuscule, et en français/anglais

possède également quelque fonctions utile
"""
from random import randint

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

BLUE       = (  0,  0,255)
RED        = (255,  0,  0)
GREEN      = (  0,255,  0)
YELLOW     = (255,255,  0)
BLACK      = (  0,  0,  0)
WHITE      = (255,255,255)
GREY       = (100,100,100)
PURPLE     = (100,  0,100)
HALFGREY   = ( 50, 50, 50)
DARKGREY   = ( 20, 20, 20)
DARKRED    = ( 10, 10, 10)
DARKGREEN  = ( 10, 10, 10)
DARKBLUE   = ( 10, 10, 10)
LIGHTBROWN = (229,219,222)
LIGHTGREY  = (200,200,200)
BEIGE      = (199,175,138)

def reverseColor(color):
    """renvoie la couleur inversée"""
    r,g,b=color
    r=255-r
    g=255-g
    b=255-b
    return (r,g,b)

print("mycolors imported")
