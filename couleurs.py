"""
Module de couleurs répertoriant quelques constantes de couleurs RGB/RVB
ainsi que des fonctions simple manipulant ces couleurs RGB/RVB
"""

from random import randint
from math import exp,log


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

# FONCTION MATHÉMATIQUE UTILISER PAR LES FONCTIONS SUIVANT CELLES-CI

sigmoid   = s   = lambda x:1/(1+math.exp(-x))
reverse_sigmoid = lambda x:log(x/(1-x))
bijection       = lambda x,e,s:(x-e[0])/(e[1]-e[0])*(s[1]-s[0])+s[0]

# FONCTIONS SIMPLE MANIPULANT DES COULEURS

random       = lambda :              tuple([randint(0,255)                 for i in range(3)])
inverser     = lambda couleur:       tuple([255-c                          for c in couleur])
assombrir    = lambda couleur,n=0:   tuple([int(c*sigmoid(n/10))           for c in couleur])
eclairer     = lambda couleur,n=0:   tuple([int(255-(255-c)*sigmoid(n/10)) for c in couleur])
melanger     = lambda coul1,coul2:   tuple([(c1+c2)//2                     for (c1,c2) in zip(coul1,coul2)])
soustraction = lambda coul1,coul2:   tuple([max(min(2*c1-c2,255),0)        for (c1,c2) in zip(coul1,coul2)])
augmenter    = lambda couleur,n=2:   tuple([int(255*exp(n*log(c/255)))     for c in couleur])




#Ceci est exécuté uniquement si ce fichier est directement exécuté seul sans passer par "import couleurs" ou "from couleurs import ..."
if __name__=="__main__":
    #Quelques fonctions de test du module
    print(assombrir(RED,10))
    print(melanger(YELLOW,RED))
    print(inverser(LIGHTBROWN))
    print(soustraction(LIGHTBROWN,ORANGE))
    print(augmenter(LIGHTBROWN))
