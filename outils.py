"""
Module d'outils basique
"""
# --coding:utf-8--

import random

# QUELQUES FONCTIONS UTILE DANS LE CAS GÉNÉRALES


def bijection(x, ensemble_entree, ensemble_sortie):
    """Renvoie la valeur de f(x) par la bijection de l'ensemble_entree
    et l'ensemble_sortie en gardant la même distance aux bornes.
    Exemple:    on a un segment [0,10] et
                on veut la valeur de x=3 dans le segment [0,100].
                Nous obtiendrons f(x)=30
    """
    min1, max1 = ensemble_entree
    min2, max2 = ensemble_sortie
    return (x - min1) / (max1 - min1) * (max2 - min2) + min2


def est_superieur(liste1, liste2):
    """Cette fonction permet de comparer deux liste d'integer.
    Elle retourne True si la list1 est supérieur à la list2
    Les premiers entiers de la liste1 et liste2 sont comparés,
    si un des deux entiers est plus grand, la liste dont il
    est issu est considéré comme supérieur à l'autre.
    Si les premiers entiers de la liste1 et la liste2 sont égaux,
    on compare le deuxième entier de la liste1 avec le
    deuxième entier de la liste2,
    si ils sont encore égaux on regarde les nombre en troisième place etc.
    Si les liste 1 et 2 contiennent les mêmes nombres,
    ont retourne au hasard vrai ou faux
    """
    ajouter_coeff_alea(liste1, liste2)
    return liste1 >= liste2


def ajouter_coeff_alea(liste1, liste2):
    """Prend un prametre deux listes.
    ajouter_coeff_alea prend une liste au hasard parmi les deux listes,
    lui ajoute 1 et ajoute 0 à l'autre.
    """
    alea_coeff = [0, 1]
    random.shuffle(alea_coeff)
    liste1.append(alea_coeff[0])
    liste2.append(alea_coeff[1])


def intersection(*args):
    """intersection prend en paramatre un nombre fini de listes.
    intersection fait l'intersection de listes python au sens des ensembles.
    exemple :
        intersection( [1,2,3], [2,3], [5,3,4]) == [3] #True
        intersection( [ (1,2), (3,4) ], [ (1,2), (2,2)] ) == [(1,2)] #True
    """

    # On utilise les fonctions intersection et intersection_de_2 récursivement
    # pour faire faire l'intersection des n listes
    def intersection_de_2(l1, l2):
        """Fait l'intersection de deux listes python au sens des ensembles."""
        resultat = []
        for i in l1:
            if i in l2:
                resultat.append(i)
        return resultat

    if len(args) == 1:
        return args[0]
    elif len(args) == 2:
        return intersection_de_2(args[0], args[1])

    return intersection(intersection_de_2(args[0], args[1]), *args[2:])
