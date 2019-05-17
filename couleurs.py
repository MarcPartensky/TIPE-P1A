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


def randomColor():
    """Génère une couleur RGB aléatoire """
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return (r,g,b)

def reverseColor(color):
    """renvoie la couleur inversée"""
    r,g,b=color
    r=255-r
    g=255-g
    b=255-b
    return (r,g,b)

def lighten(self,color,luminosity=80):
    """Renvoie la couleurs donné en modifiant sa luminosité"""
    r,g,b=color
    if luminosity>=50:
        r+=(255-r)*luminosity/100
        g+=(255-g)*luminosity/100
        b+=(255-b)*luminosity/100
    else:
        r*=luminosity/50
        g*=luminosity/50
        b*=luminosity/50
    color=int(r),int(g),int(b)
    return color

def wavelengthToRGB(self,wavelength):
    """Convertie une longueur d'onde en couleur RGB"""
    gamma,max_intensity=0.80,255
    def adjust(color, factor):
        if color==0: return 0
        else: return round(max_intensity*pow(color*factor,gamma))
    if   380<=wavelength<=440: r,g,b=-(wavelength-440)/(440-380),0,1
    elif 440<=wavelength<=490: r,g,b=0,(wavelength-440)/(490-440),1
    elif 490<=wavelength<=510: r,g,b=0,1,-(wavelength-510)/(510-490)
    elif 510<=wavelength<=580: r,g,b=(wavelength-510)/(580-510),1,0
    elif 580<=wavelength<=645: r,g,b=1,-(wavelength-645)/(645-580),0
    elif 645<=wavelength<=780: r,g,b=1,0,0
    else: r,g,b=0,0,0
    if 380<=wavelength<=420: factor=0.3+0.7*(wavelength-380)/(420-380)
    elif 420<=wavelength<=701: factor=1
    elif 701<=wavelength<=780: factor=0.3+0.7*(780-wavelength)/(780-700)
    else: factor=0
    r,g,b=adjust(r,factor),adjust(g,factor),adjust(b,factor)
    return (r,g,b)


print("mycolors imported")
