"""
################################################################################
#
#              Institut Supérieur d'électronique de Paris (ISEP)
#
#                               SUJET DE TIPE:
#                     Othello et Intelligence Artificielle
#
#    Première année  --  MPSI
#
#    Créateurs : Marc  PARTENSKY
#                Valentin  COLIN
#                Alexandre BIGOT
#
#    Version : 2019
#
###############################################################################
#
#                           SOMMAIRE du plateau
#
#    1.    Class Plateau:  ........................................... ligne  83
#    1.1   ------> __init__ (self,theme=None)  ....................... ligne  85
#    1.2   ------> creerGrille (self)  ............................... ligne
#    1.3   ------> est_dans_grille (self,position)  .................. ligne
#    1.4   ------> est_un_coin (self,position)  ...................... ligne
#    1.5   ------> obtenirPositionBrute (self,(etc).)  ............... ligne
#    1.6   ------> obtenirPositionPlateau (self,(etc).) .............. ligne
#    1.7   ------> estComplet (self)  ................................ ligne
#    1.8   ------> estJouable (self)  ................................ ligne
#    1.9   ------> estFini (self)  ................................... ligne
#    1.10  ------> obtenirCoteGagnant (self)  ........................ ligne
#    1.11  ------> testVictoire (self)  ......  (obsolète)   ......... ligne
#    1.12  ------> charger (self,cote)  .............................. ligne
#    1.13  ------> obtenirCase (self,coordonnees)  ................... ligne
#    1.14  ------> obtenirCases (self,coordonnees)  .................. ligne
#    1.15  ------> obtenirPions (self,cotes)  ........................ ligne
#    1.16  ------> __contains__ (self,pion)  ......................... ligne
#    1.17  ------> obtenirNombrePionsJoueur (self,cote)  ............. ligne
#    1.18  ------> obtenirNombrePionsRestant (self)  ................. ligne
#    1.19  ------> obtenirEnvironnement (self,positions)  ............ ligne
#    1.20  ------> obtenirAlentours (self,positions)  ................ ligne
#    1.21  ------> obtenirLignesAlentours (self,position)  ........... ligne
#    1.22  ------> insererPion (self,positions,cote)  ................ ligne
#    1.23  ------> placer_pion (self,position,cote)  ................. ligne
#    1.24  ------> estCaseVide (self,position)  ...................... ligne
#    1.25  ------> estCaseJoueur (self,position,cote)  ............... ligne
#    1.26  ------> obtenirCoteOppose (self,cote_joueur)  ............. ligne
#    1.27  ------> obtenirMouvementsValides (self,joueur_cote)  ...... ligne
#    1.28  ------> estMouvementValide (self,mouvement,cote)  ......... ligne
#    1.29  ------> estMouvementValideDansLigne (self,cote,ligne)  .... ligne
#    1.30  ------> obtenirLigneInclus (self,position,vecteur,taille) . ligne
#    1.31  ------> obtenirLigneExclus (self,position,vecteur,taille) . ligne
#    1.32  ------> obtenirDirections (self)  ......................... ligne
#    1.33  ------> conquerir (self,position,p_cote)  ................. ligne
#    1.34  ------> conquerirLigne (self,cote,ligne)  ................. ligne
#    1.35  ------> manger (self,mangeables,personne)  ................ ligne
#    1.36  ------> afficher (self,fenetre)  .......................... ligne
#    1.37  ------> presenter (self, (etc).)  ......................... ligne
#    1.38  ------> afficherMessage(self,(etc).)  ..................... ligne
#    1.39  ------> colorerCase (self,positions,couleur,fenetre)  ..... ligne
#    1.40  ------> colorerLigne (self,ligne,couleur,fenetre)  ........ ligne
#    1.41  ------> afficherFond (self,fenetre)  ...................... ligne
#    1.42  ------> afficherDecorationGrille (self,fenetre)  .......... ligne
#    1.43  ------> afficherMouvements (self,(etc).)  ................. ligne
#    1.44  ------> afficherGrille (self,fenetre)  .................... ligne
#    1.45  ------> afficherPions (self,fenetre)  ..................... ligne
#    1.46  ------> afficherAnimationPion(self,(etc).)  ............... ligne
#
###############################################################################
"""
# --coding:utf-8--

from outils import intersection
from outils import linearBijection as bijection
import outils
import couleurs
import config as cfg
import time #pour les animations
import pygame



class Plateau:
    """Représentation en classe de l'othellier"""

    def __init__(self,theme=None): # la taille doit forcément être un carré de coté paire
        """Cree un plateau."""
        self.taille=[8,8] # taille du plateau 8 lignes et 8 colonnes
        self.creerGrille()
        self.mouvements=[]
        self.gagne=False
        self.taille_x,self.taille_y=self.taille
        self.nombre_de_joueurs=2
        self.demonstration=True
        if theme: self.couleur_grille,self.pieces_couleur,self.mouvements_couleur=theme

    def creerGrille(self):
        """Cree une grille."""
        sx,sy=self.taille
        self.grille=[[cfg.CASE_VIDE for x in range(sx)] for y in range(sy)]

        ####### marche dans le cas d'une grille [8,8] comme ici mais peu rigoureux
        #self.insererPion([(3,3),(4,4)],0) #Place les pions du joueur de côté 0.
        #self.insererPion([(3,4),(4,3)],1) #Place les pions du joueur de côté 1.

        ####### marche quelque soit la taille de la grille
        self.insererPion([(sx//2-1,sx//2-1),(sx//2,  sx//2)],0) #Place les pions du joueur de côté 0.
        self.insererPion([(sx//2-1,sx//2  ),(sx//2,sx//2-1)],1) #Place les pions du joueur de côté 1.

    def estDansGrille(self,position):
        """Verifie si la position est dans la grille"""
        sx,sy=self.taille
        x,y=position
        return (0<=x<sx and 0<=y<sy)

    def estCoin(self, position):
        """Determine si une position correspond a un coin."""
        x,y=position
        sx,sy=self.taille
        x_=x%(sx-1)
        y_=y%(sy-1)
        return (x_,y_)==(0,0)

    def obtenirPositionBrute(self,position_plateau,fenetre):
        """Renvoie la position brute en pixel a l'aide d'une position dans le systeme de coordonnees du plateau."""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        px,py=position_plateau
        return (int((px+1/2)*wsx/sx),int((py+1/2)*wsy/sy))

    def obtenirPositionPlateau(self,position_brute,fenetre):
        """Renvoie la position dans le systeme de coordonnees du plateau a l'aide d'une position brute de la fenetre en pixels."""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        rx,ry=position_brute
        return (int(rx*sx/wsx),int(ry*sy/wsy))

    def estComplet(self):
        """Renvoie si le plateau est complet ou non."""
        compteur=0
        for colonne in self.grille:
            compteur+=colonne.count(cfg.CASE_VIDE)
        return bool(compteur==0) #Le bool met en évidence le type...

    def estJouable(self):
        """Renvoie si le plateau est jouable."""
        #Lorsqu'on utilise cette fonction il est inutile de vérifier si le plateau est complet, celle-ci se comportera comme attendue.
        jouable=False
        for i in range(self.nombre_de_joueurs):
            coups=self.obtenirMouvementsValides(i)
            if len(coups)>0:
                jouable=True
                break
        return jouable

    def estFini(self):
        """Renvoie si le plateau est fini, la seule nuance avec jouable c'est
        que si le plateau est complet il n'est pas nécessaire de recalculer
        l'ensemble des coups qui sont possibles. Cela permet plus d'efficacité
        dans l'exécution du code."""
        complet=self.estComplet() #Détermine si le plateau est complet
        if complet: #S'il est complet alors la partie est finie
            return True
        else: #Sinon on peut vérifier si celui-ci est jouable.
            jouable=self.estJouable() #Détermine si le plateau est jouable
            return not(jouable) #Si le plateau n'est pas jouable alors la partie est finie

    def obtenirCoteGagnant(self):
        """Renvoie le gagnant de la partie au stade actuel."""
        pions0=self.obtenirPions(0) #Récupère les positions (x,y) pions du joueur0
        pions1=self.obtenirPions(1) #Récupère les positions (x,y) pions du joueur1
        compte_des_pions=(len(pions0),len(pions1))
        if len(pions0)!=len(pions1):
            cote_gagnant=compte_des_pions.index(max(compte_des_pions)) #Détermine un gagnant meme si la partie n'est pas encore finie
        else:
            cote_gagnant=None
        return cote_gagnant

    def testVictoire(self): #Ancien test de victoire obselète
        """Test la victoire et vérifie si au moins l'un des joueurs possède un coup ."""
        compteur=0
        for colonne in self.grille:
            compteur+=colonne.count(cfg.CASE_VIDE) # compte le nombre d'occurence de case vide dans la colonne
        if compteur==0: #Verifie si il reste encore des cases vides
            self.gagne=True
            return self.gagne
        else: #S'il en reste, verifie si au moins un joueur peut joueur
            self.gagne=True
            for i in range(self.nombre_de_joueurs):
                coups=self.obtenirMouvementsValides(i)
                if len(coups)>0:
                    self.gagne=False
                    break
        return self.gagne

    def charger(self,cote):
        """Charge les attributs du plateau afin d'être préchargé pour les ias et ainsi économiser le temps de calcul."""
        self.mouvements=self.obtenirMouvementsValides(cote)

    def obtenirCase(self,coordonnees):
        """Retourne le contenu d'une case"""
        x,y=coordonnees
        return self.grille[y][x]

    def obtenirCases(self,coordonnees):
        """Renvoie une liste de contenu de cases avec les coordonnees de celles-ci."""
        if type(coordonnees)==list:
            cases=[]
            for position in coordonnees:
                cases.append(self.obtenirCases(position))
            return cases
        else:
            x,y=coordonnees
            return self.grille[y][x]

    def obtenirPions(self,cotes):
        """Obtenir toute les position de toutes les pieces de cotes de joueurs"""
        if not isinstance(cotes,list): cotes=[cotes]
        positions=[]
        for cote in cotes:
            sx,sy=self.taille
            for y in range(sy):
                for x in range(sx):
                    case=self.obtenirCase((x,y))
                    if self.estCaseJoueur((x,y),cote):
                        positions.append((x,y))
        return positions

    def __contains__(self,pion):
        """Determine si le plateau contient un pion.
        Méthode spécial permèttant d'utiliser le mot clé 'in' """
        case=self.obtenirCase(pion)
        return bool(case!=cfg.CASE_VIDE)

    def obtenirNombrePionsJoueur(self, cote):#Todo à optimiser
        """Determine le nombre de pions d'un joueur en utilisant son cote."""
        nombre=0
        sx, sy = self.taille
        for y in range(sy):
            for x in range(sx):
                if self.estCaseJoueur((x,y), cote) :
                    nombre+=1
        return nombre

    def obtenirNombrePionsRestant(self):
        """Determine le nombre de cases restantes"""
        return self.taille[0]*self.taille[1]-self.obtenirNombrePionsJoueur(0)-self.obtenirNombrePionsJoueur(1)

    def obtenirEnvironnement(self,positions):
        """Prend en parametre une liste de position de case et retourne la liste des postions des cases vide se trouvant juste à cote"""
        if type(positions)!=list: positions=[positions]
        environnement=[]
        directions=self.obtenirDirections()
        for position in positions:
            px,py=position
            for pas in directions:
                stx,sty=pas
                x,y=(px+stx,py+sty)
                if self.estDansGrille((x,y)):
                    if self.estCaseVide((x,y)) :
                        environnement.append((x,y))
        environnement=list(set(environnement))
        return environnement

    def obtenirAlentours(self,positions):
        """Prend en parametre une liste de position de case et retourne la liste des postions des cases vide se trouvant juste à cote"""
        if type(positions)!=list: positions=[positions]
        environnement=[]
        directions=self.obtenirDirections()
        for position in positions:
            px,py=position
            for pas in directions:
                stx,sty=pas
                x,y=(px+stx,py+sty)
                if self.estDansGrille((x,y)):
                    environnement.append((x,y))
        environnement=list(set(environnement))
        return environnement


    def obtenirLignesAlentours(self,position):
        """Renvoie les lignes partant du pion de position 'position' et en partant dans toutes les directions dans le sens trigonométrique."""
        directions=self.obtenirDirections()
        lignes=[self.obtenirLigneExclus(position,direction) for direction in directions]
        return lignes

    def insererPion(self,positions,cote):
        """insererPion insere un pion dans la grille sans se soucier de conquerir le territoire"""
        if type(positions)!=list: positions=[positions]
        for position in positions:
            x,y=position
            self.grille[y][x]=cote

    def placerPion(self,position,cote):
        """Place un pion sur le plateau et modifie celui-ci
        en conséquence selon les règle de l'othello"""
        self.insererPion(position,cote)
        return self.conquerir(position,cote)

    def estCaseVide(self, position):
        """Determine si la case a la position donnee est une case vide."""
        return self.obtenirCase(position)==cfg.CASE_VIDE

    def estCaseJoueur(self,position,cote):
        """Determine si la case a la position donnee contient un pion du joueur cote."""
        return self.obtenirCase(position)==cote

    def obtenirCoteOppose(self,cote_joueur):
        """Renvoie le cote oppose en fonction du cote donné."""
        cote_oppose=1-cote_joueur #Utilise simplement la technique du complémentaire a 1.
        return cote_oppose

    def obtenirMouvementsValides(self,joueur_cote): #yavait fenetre dans les parametres
        """Retourne une liste de tuple qui correspondent aux coordonnees des mouvements possibles pour le joueur_cote"""
        cote=self.obtenirCoteOppose(joueur_cote)
        positions=self.obtenirPions(cote)
        positions_possibles=self.obtenirEnvironnement(positions)
        mouvements_valides=[]
        for position_possible in positions_possibles:
            if self.estMouvementValide(position_possible,joueur_cote):
                mouvements_valides.append(position_possible)
        return mouvements_valides

    def estMouvementValide(self,mouvement,cote):
        """Permet de verifier si un mouvement est valide."""
        directions=self.obtenirDirections()
        resultat=False
        for direction in directions:
            ligne=self.obtenirLigneExclus(mouvement,direction)
            validite=self.estMouvementValideDansLigne(cote,ligne)
            if validite:
                resultat=True
                break
        return resultat

    def estMouvementValideDansLigne(self,cote,ligne):
        """Permet de verifier si un mouvement est valide dans une ligne."""
        valide=False
        possible=False
        cote_oppose=self.obtenirCoteOppose(cote)
        #Regarde si une ligne peut etre prise.
        for position in ligne: #Regarde chaque pion de la ligne dans l'ordre.
            if not self.estDansGrille(position): #Si on sort de la ligne, celle-ci ne peut pas être prise
                break #On arrete la vérification
            else:
                case=self.obtenirCase(position) #Sinon on récupère la case
                if case==cote: #Si la case est a nous
                    if possible: #et que l'on a déja rencontré des pions ennemis on peut prendre cette ligne.
                        valide=True
                    break #On arrete la vérification
                elif case==cote_oppose: #Si la case contient un pion ennemi alors on peut possiblement le prendre
                        possible=True
                else: #Sinon la case est vide et on arrete la vérification
                    break
        return valide

    def obtenirLigneInclus(self,position,vecteur,taille=None):
        """Recupere la ligne des valeurs obtenue avec une position et un vecteur."""
        if not taille: taille=max(self.taille)
        vx,vy=vecteur
        x,y=position
        n=0
        ligne=[]
        while self.estDansGrille((x,y)) and n<taille:
            ligne.append((x,y))
            x+=vx
            y+=vy
            n+=1
        return ligne

    def obtenirLigneExclus(self,position,vecteur,taille=None):
        """Recupere la ligne des valeurs obtenue avec une position et un vecteur."""
        if not taille: taille=max(self.taille)
        vx,vy=vecteur
        x,y=position
        n=0
        x+=vx
        y+=vy
        ligne=[]
        while self.estDansGrille((x,y)) and n<taille:
            ligne.append((x,y))
            x+=vx
            y+=vy
            n+=1
        return ligne

    def obtenirDirections(self):
        """Recupere les directions avec les vecteurs orientés selon chaque axe,
        ranger dans un ordre afin de tourner dans le sens trigo (important)"""
        #directions=[(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y)!=(0,0)]
        directions=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        return directions

    def conquerir(self,position,p_cote):
        """Permet au nouveau pion à la position 'position' de couleur 'cote' de
        retouner les autres pions"""
        directions=self.obtenirDirections()
        for direction in directions:
            ligne=self.obtenirLigneExclus(position,direction)
            self.conquerirLigne(p_cote,ligne)
        return True

    def conquerirLigne(self,cote,ligne):
        """Permet au nouveau pion a la position position de couleur cote de
        retouner les autres pions dans une ligne"""
        mangeables=[]
        for position in ligne:
            if not self.estDansGrille(position):
                break
            case=self.obtenirCase(position)
            if case!=cote and case!=cfg.CASE_VIDE:
                mangeables.append(position)
            elif case==cote:
                self.manger(mangeables,cote)
                break
            else: #Dans ce case la case est vide
                break

    def manger(self,mangeables,personne):
        """Assigne aux cases mangeables la valeur de pion de la personne"""
        self.insererPion(mangeables,personne)

    def afficher(self,fenetre):
        """Affiche l'ensemble des éléments du plateau."""
        self.afficherFond(fenetre)
        self.afficherGrille(fenetre)
        self.afficherDecorationGrille(fenetre)
        self.afficherPions(fenetre)
        self.afficherMouvements(fenetre)

    def presenter(self,positions,couleur,fenetre,message=None,clear=True,pause=True,couleur_texte=couleurs.NOIR):
        """Permet de debuger en 1 commande."""
        if self.demonstration:
            if not type(positions)==list: positions=[positions]
            if clear:
                fenetre.clear()
                self.afficher(fenetre)
            if positions:
                self.colorerCase(positions,couleur,fenetre)
                if message:
                    self.afficherMessage(message,positions[0],couleur_texte,fenetre)
            fenetre.flip()
            if pause:
                fenetre.pause()

    def afficherMessage(self,message,position,couleur,fenetre):
        """Affiche un message en utilisant une position plateau, une couleur, et une fenetre."""
        x,y=position
        position=(x-3/7,y-2/5) #Déplacement arbitraire
        position=self.obtenirPositionBrute(position,fenetre)
        fenetre.drawText(message,position,couleur)

    def colorerCase(self,positions,couleur,fenetre):
        """Colorie une case du plateau d'une certaine couleur en affichant les contours d'un carre de couleur.
        Cette fonction est utile pour debug.
        Utilise la position dans le systeme de coordonnees du plateau, une couleur et une fenetre."""
        if not type(positions)==list: positions=[positions]
        for position in positions:
            x,y=self.obtenirPositionBrute(position,fenetre)
            wsx,wsy=fenetre.taille #Taille de la fenetre en coordonnees de la fenetre
            sx,sy=self.taille #Taille du plateau en coordonnes du plateau
            cx=wsx/sx #Taille d'une case en x en coordonnees de la fenetre
            cy=wsy/sy #Taille d'une case en y en coordonnees de la fenetre
            mx=x-cx//2+1 #Position d'une case en x en coordonnees de la fenetre
            my=y-cy//2+1 #Position d'une case en y en coordonnees de la fenetre
            for i in range(2,6):
                fenetre.draw.rect(fenetre.screen,couleur,[mx+i,my+i,cx-2*i,cy-2*i],1)

    def colorerLigne(self,ligne,couleur,fenetre):
        """Colorie la ligne."""
        cfg.debug("colorer:ligne:",ligne)
        ligne=outils.obtenirLigne(ligne[0],ligne[-1])
        self.colorerCase(ligne,couleur,fenetre)

    def afficherFond(self,fenetre):
        """Affiche un fond colore."""
        ftx,fty=fenetre.taille
        for y in range(0,fty,10):
            for x in range(0,ftx,10):
                r=abs(bijection(x,[0,ftx],[-100,100]))
                g=255-abs(bijection((x+y)/2,[0,ftx],[-100,100]))
                b=abs(bijection(y,[0,fty],[-100,100]))
                couleur=(r,g,b)
                fenetre.draw.rect(fenetre.screen,couleur,[x,y,10,10],0)

    def afficherDecorationGrille(self,fenetre):
        """Affiche les 4 points pour délimiter le carré central du plateau.
        Aspect uniquement graphique et décoratif afin d'améliorer le confort de l'utilisateur"""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        d=wsy//sy # distance entre deux ligne ou colonne
        positions_points_graphic=[(2*d,2*d),(2*d,wsy-2*d),(wsx-2*d,2*d),(wsx-2*d,wsy-2*d)]
        for position in positions_points_graphic:
            fenetre.draw.circle(fenetre.screen,couleurs.NOIR,position,5,0)

    def afficherMouvements(self,fenetre,mouvements=None,couleur=None):
        """Afficher les coups possible. (point rouge sur la fenêtre)"""
        if not mouvements: mouvements=self.mouvements
        if not couleur: couleur=self.mouvements_couleur
        #devrait  marcher si il n'y a que un moment.
        for move in mouvements:
            wsx,wsy=fenetre.taille
            sx,sy=self.taille
            rayon=int(min(wsx,wsy)/min(sx,sy)/4)
            x,y=move
            position_brute=self.obtenirPositionBrute((x,y),fenetre)
            fenetre.draw.circle(fenetre.screen,(100,0,0),position_brute,rayon+2,0) #affiche des bord aux couleurs, bonne idees mais mal implemente
            fenetre.draw.circle(fenetre.screen,couleur,position_brute,rayon,0)


    def afficherGrille(self,fenetre):
        """Affiche la grille."""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        for y in range(sy):
            _y=y*wsy//sy
            start=(0,_y)
            end=(wsx,_y)
            fenetre.draw.line(fenetre.screen,self.couleur_grille,start,end,1)
        for x in range(sx):
            _x=x*wsx//sx
            start=(_x,0)
            end=(_x,wsy)
            fenetre.draw.line(fenetre.screen,self.couleur_grille,start,end,1)

    def afficherPions(self,fenetre):
        """Affiche les pions durant la partie"""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        taille_relative=2/5 #Taille du pion par rapport a une case
        rayon=int(min(wsx,wsy)/min(sx,sy)*taille_relative) #taille des pions a changer
        for y in range(sy):
            for x in range(sx):
                case=self.obtenirCase((x,y))
                position_brute=self.obtenirPositionBrute((x,y),fenetre)
                if 0<=case and case<=len(self.pieces_couleur)-1 :
                    couleur=self.pieces_couleur[case]
                    fenetre.draw.circle(fenetre.screen,couleurs.reverseColor(couleur),position_brute,rayon+2,0)
                    fenetre.draw.circle(fenetre.screen,couleur,position_brute,rayon,0)

    def afficherAnimationPion(self,fenetre,choix_du_joueur):
        """Permet d'affichier l'animation du placement d'un nouveau pion en faisant clicgnoter son contour."""
        wsx,wsy=fenetre.taille
        sx,sy=self.taille
        rayon=int(min(wsx,wsy)/min(sx,sy)/2.5)
        x,y=choix_du_joueur
        position_brute=self.obtenirPositionBrute((x,y),fenetre)
        case=self.obtenirCase(choix_du_joueur)
        couleur=self.pieces_couleur[case]
        for i in range(2):
            fenetre.draw.circle(fenetre.screen,couleur,position_brute,rayon+2,0)
            fenetre.check()
            fenetre.flip()
            time.sleep(cfg.TEMPS_ANIMATION_PION)
            fenetre.draw.circle(fenetre.screen,(255,0,0),position_brute,rayon+2,0) #tres mal implemente
            fenetre.draw.circle(fenetre.screen,couleur,position_brute,rayon,0)
            fenetre.check()
            fenetre.flip()
