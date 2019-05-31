import random,time

# FONCTION MATHÉMATIQUE (utiliser pour les couleurs et notamment afficher un fond d'écran plus agréable)
sigmoid = lambda x : 1/(1+math.exp(-x))

# QUELQUES FONCTIONS UTILE DANS LE CAS GÉNÉRALES

def bijection(x,ensemble_entree,ensemble_sortie):
    """Renvoie la valeur de f(x) par la bijection de l'ensemble_entree
    et l'ensemble_sortie en gardant la même distance aux bornes.
    Exemple:    on a un segment [0,10] et on veut la valeur de x=3 dans le segment [0,100].
                Nous obtiendrons f(x)=30"""
    min1,max1=ensemble_entree
    min2,max2=ensemble_sortie
    return (x-min1)/(max1-min1)*(max2-min2)+min2

def est_superieur(liste1, liste2) :
    """"demander alex"""
    ajouter_coeff_alea(liste1,liste2)
    return liste1>=liste2

def ajouter_coeff_alea(liste1,liste2) :
    """Prend un prametre deux listes.
    ajouter_coeff_alea prend une liste au hasard parmi les deux listes, lui ajoute 1 et ajoute 0 à l'autre."""
    alea_coeff = [0, 1]
    random.shuffle(alea_coeff)
    liste1.append(alea_coeff[0])
    liste2.append(alea_coeff[1])

def intersection(*args) :
    """intersection prend en paramatre un nombre fini de listes.
    intersection fait l'intersection de listes python au sens des ensembles.
    exemple :
        intersection( [1,2,3], [2,3], [5,3,4]) == [3] #True
        intersection( [ (1,2), (3,4) ], [ (1,2), (2,2)] ) == [(1,2)] #True
    """

    #On utilise les fonctions intersection et intersection_de_2 récursivement pour faire faire l'intersection des n listes
    def intersection_de_2(l1, l2):
        """Fait l'intersection de deux listes python au sens des ensembles."""
        resultat = []
        for i in l1:
            if i in l2:
                resultat.append(i)
        return resultat
    if len(args)==1:
        return args[0]
    elif len(args)==2:
        return intersection_de_2(args[0], args[1])

    return intersection(intersection_de_2(args[0], args[1]), *args[2:])

def liste_liste_vers_liste_tuple(liste_liste):
    """Transforme une liste de liste en liste de tuple"""
    return [tuple(l) for l in liste_liste]

# NON UTILISER
def liste_tuple_vers_liste_liste(liste_de_tuple):
    """Transforme une liste de tuple en liste de liste"""
    return [list(elem) for elem in liste_de_tuple]

# NON UTILISER
def arrangementsConsecutifs(liste,n): #todo mieux expliciter ce que fait cette fonction (ajouter des exemples)
    """Renvoie la liste des arrangements consécutifs de taille n."""
    arrangements=[]
    for i in range(len(liste)):
        arrangement=[]
        for j in range(n):
            arrangement.append(liste[(i+j)%n])
        arrangements.append(arrangement)
    return arrangements

# NON UTILISER
def estRemplie(ligne,composante):
    """Determine si une ligne est remplie d'une même composante."""
    resultat=True
    for element in ligne:
        if element!=composante:
            resultat=False
            break
    return resultat

# NON UTILISER
def vecteur(arrivee,depart):
    """Renvoie le vecteur obtenu par les 2 positions"""
    vecteur=tuple([a-d for (a,d) in zip(arrivee,depart)])
    return vecteur

# NON UTILISER
def extremiter(ligne):
    """Renvoie les extrémités d'une ligne."""
    ligne=[ligne[0],ligne[-1]]
    return ligne


# DECORATEUR DE FONCTION

def deco_timer(fonction):
    """Décorateur qui permet de calculer le temps d'exécution d'une fonction."""
    def nouvelleFonction(*args,**kwargs):
        """Fonction à tester."""
        ti=time.time()
        resultat=fonction(*args,**kwargs)
        tf=time.time()
        dt=tf-ti
        print("[TIMER]: La fonction "+str(fonction.__name__)+" a pris "+str(dt)+" secondes.")
        return resultat
    return nouvelleFonction
