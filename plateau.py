"""
###############################################################################
#
#              Institut Supérieur d'électronique de Paris (ISEP)
#
#                               SUJET DE TIPE:
#                     Othello et Intelligence Artificielle
#
#    Première année  --  MPSI
#
#    Créateurs : Alexandre BIGOT
#                Valentin  COLIN
#                Marc  PARTENSKY
#
#    Version : 2019
#
###############################################################################
#
#                           SOMMAIRE du plateau
#
#    1.    Class Plateau:  ......................................... ligne  75
#    1.1   ----> __init__ (self,theme=None)  ....................... ligne  78
#    1.2   ----> creerGrille (self)  ............................... ligne  89
#    1.3   ----> estDansGrille (self,position)  .................... ligne  98
#    1.4   ----> obtenirPositionPlateau (self,(etc).) .............. ligne 104
#    1.5   ----> obtenirPositionBrute (self,(etc).)  ............... ligne 115
#    1.6   ----> estComplet (self)  ................................ ligne 124
#    1.7   ----> estJouable (self)  ................................ ligne 131
#    1.8   ----> estFini (self)  ................................... ligne 141
#    1.9   ----> obtenirCoteGagnant (self)  ........................ ligne 154
#    1.10  ----> charger (self,cote)  .............................. ligne 165
#    1.11  ----> obtenirCase (self,coordonnees)  ................... ligne 171
#    1.12  ----> obtenirCases (self,coordonnees)  .................. ligne 176
#    1.13  ----> obtenirPions (self,cotes)  ........................ ligne 189
#    1.14  ----> obtenirScores (self)  ............................. ligne 204
#    1.15  ----> compterPions (self,cote)  ......................... ligne 208 # correct jusqu'ici ensuite tous est décaler ou pourra être décaler
#    1.16  ----> obtenirNombrePionsRestant (self)  ................. ligne 214
#    1.17  ----> obtenirEnvironnement (self,positions)  ............ ligne 219
#    1.18  ----> obtenirLignesAlentours (self,position)  ........... ligne 224
#    1.19  ----> insererPion (self,positions,cote)  ................ ligne 229
#    1.20  ----> placerPion (self,position,cote)  .................. ligne 236
#    1.21  ----> estCaseVide (self,position)  ...................... ligne 242
#    1.22  ----> estCaseJoueur (self,position,cote)  ............... ligne 246
#    1.23  ----> obtenirCoteOppose (self,cote_joueur)  ............. ligne 250
#    1.24  ----> obtenirMouvementsValides (self,joueur_cote)  ...... ligne 255
#    1.25  ----> estMouvementValide (self,mouvement,cote)  ......... ligne 266
#    1.26  ----> estMouvementValideDansLigne (self,cote,ligne)  .... ligne 279
#    1.27  ----> obtenirLigneInclus (self,position,vecteur,taille) . ligne 299
#    1.28  ----> obtenirLigneExclus (self,position,vecteur,taille) . ligne 313
#    1.29  ----> obtenirDirections (self)  ......................... ligne 329
#    1.30  ----> conquerir (self,position,cote)  ................... ligne 335
#    1.31  ----> conquerirLigne (self,cote,ligne)  ................. ligne 343
#    1.32  ----> presenter (self, (etc).)  ......................... ligne 357
#    1.33  ----> afficherTexte(self,(etc).)  ....................... ligne 373
#    1.34  ----> colorerCase (self,positions,couleur,fenetre)  ..... ligne 381
#    1.35  ----> afficher (self,fenetre)  .......................... ligne 397
#    1.36  ----> afficherFond (self)  .............................. ligne 404
#    1.37  ----> afficherGrille (self)  ............................ ligne 416
#    1.38  ----> afficherDecorationGrille (self)  .................. ligne 431
#    1.39  ----> afficherPions (self)  ............................. ligne 442
#    1.40  ----> afficherMouvements (self)  ........................ ligne 457
#
###############################################################################
"""
# --coding:utf-8--

import outils
import couleurs
import config as cfg
import time # pour les animations
import pygame



class Plateau:
    """Représentation en classe de l'Othelier."""

    def __init__(self,taille=[8,8]):
        """Cree un plateau."""
        self.taille=taille # taille du plateau 8 lignes et 8 colonnes
        self.creerGrille()
        self.mouvements=[]
        self.gagne=False
        self.taille_x,self.taille_y=self.taille
        self.nombre_de_joueurs=2
        self.demonstration=True
        self.surface=pygame.Surface(cfg.RESOLUTION_PLATEAU)

    def creerGrille(self):
        """Cree une grille. Et place des 4 pions initiaux"""
        sx,sy=self.taille
        self.grille=[[cfg.CASE_VIDE for x in range(sx)] for y in range(sy)]
        mx=sx//2-1 # 4èmes case sur une ligne de 8 cases
        my=sy//2-1
        self.insererPion([(mx,my),(mx+1,my+1)],0)
        self.insererPion([(mx+1,my),(mx,my+1)],1)

    def estDansGrille(self,position):
        """Verifie si la position est dans la grille"""
        sx,sy=self.taille
        x,y=position
        return (0<=x<sx and 0<=y<sy)

    def obtenirPositionPlateau(self,panneau):
        """Renvoie la position dans le systeme de coordonnees du plateau
        à l'aide d'une position brute de la panneau en pixels.
        """
        position_brute=panneau.point()
        wsx,wsy=self.surface.get_size()
        sx,sy=self.taille
        rx,ry=position_brute
        px,py=(int(rx*sx/wsx),int(ry*sy/wsy))
        return (px,py)

    def obtenirPositionBrute(self,position_plateau):
        """Renvoie la position brute en pixel a l'aide d'une position
        dans le systeme de coordonnees du plateau.
        """
        wsx,wsy=self.surface.get_size()
        sx,sy=self.taille
        px,py=position_plateau
        return (int((px+1/2)*wsx/sx),int((py+1/2)*wsy/sy))

    def estComplet(self):
        """Renvoie si le plateau est complet ou non."""
        compteur=0
        for colonne in self.grille:
            compteur+=colonne.count(cfg.CASE_VIDE)
        return compteur == 0

    def estJouable(self):
        """Renvoie si le plateau est jouable."""
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
        l'ensemble des coups qui sont possibles. Cela permet une meilleur
        efficacité dans l'exécution du code."""
        complet=self.estComplet() #Détermine si le plateau est complet
        if complet: # S'il est complet alors la partie est finie
            return True
        else: # Sinon on peut vérifier si celui-ci est jouable.
            jouable=self.estJouable() # Détermine si le plateau est jouable
            # Si le plateau n'est pas jouable alors la partie est finie
            return not(jouable)

    def obtenirCoteGagnant(self):
        """Renvoie le gagnant de la partie au stade actuel."""
        pions0=self.obtenirPions(0)
        pions1=self.obtenirPions(1)
        compte_des_pions=(len(pions0),len(pions1))
        if len(pions0) != len(pions1):
            cote_gagnant = compte_des_pions.index(max(compte_des_pions))
        else:
            cote_gagnant=None
        return cote_gagnant

    def charger(self,cote):
        """Charge les attributs du plateau afin d'être préchargé pour les ias
        et ainsi économiser le temps de calcul.
        """
        self.mouvements=self.obtenirMouvementsValides(cote)

    def obtenirCase(self,coordonnees):
        """Retourne le contenu d'une case"""
        x,y=coordonnees
        return self.grille[y][x]

    def obtenirCases(self,coordonnees):
        """Renvoie la liste de ce que contiennent les case
        aux coordonnees demander.
        """
        if type(coordonnees)==list:
            cases=[]
            for position in coordonnees:
                cases.append(self.obtenirCases(position))
            return cases
        else:
            x,y=coordonnees
            return self.grille[y][x]

    def obtenirPions(self,cotes):
        """Renvoie la liste des position des pions
        appartenant au joueur cotes.
        """
        if not isinstance(cotes,list): cotes=[cotes]
        positions=[]
        for cote in cotes:
            tx,ty=self.taille
            for y in range(ty):
                for x in range(tx):
                    case=self.obtenirCase((x,y))
                    if self.estCaseJoueur((x,y),cote):
                        positions.append((x,y))
        return positions

    def obtenirScores(self):
        """Obtient le score."""
        return [self.compterPions(i) for i in range(self.nombre_de_joueurs)]

    def compterPions(self,cote):
        """Compte le nombre de pions d'un joueur avec son côté."""
        tx,ty=self.taille
        # ce qu'on met dans la liste n'as pas d'importance donc on met un jolie smiley --> "_"
        return len([ "_" for x in range(tx) for y in range(ty) if self.estCaseJoueur((x,y), cote)])

    def obtenirNombrePionsRestant(self):
        """Determine le nombre de cases restantes"""
        #return self.taille[0] * self.taille[1] - self.compterPions(0) - self.compterPions(1)
        return self.compterPions(-1) # compte le nombre de cases vide

    def obtenirEnvironnement(self,positions):
        """Prend en parametre une liste de position de case
        et retourne la liste des postions des cases vide
        se trouvant autour des ces cases.
        """
        if type(positions) != list:
            positions=[positions]
        environnement = []
        directions = self.obtenirDirections()
        for position in positions:
            px, py = position
            for pas in directions:
                stx, sty = pas
                x,y = (px + stx, py + sty)
                if self.estDansGrille((x,y)):
                    if self.estCaseVide((x,y)):
                        environnement.append((x,y))
        environnement = list(set(environnement))
        return environnement

    def obtenirLignesAlentours(self,position):
        """Renvoie les lignes partant du pion de position 'position' et en
        partant dans toutes les directions dans le sens trigonométrique.
        """
        directions = self.obtenirDirections()
        lignes = [self.obtenirLigneExclus(position,direction) for direction in directions]
        return lignes

    def insererPion(self,positions,cote):
        """insererPion insere un pion dans la grille sans se soucier
        de conquerir le territoire.
        """
        if type(positions) != list:
            positions=[positions]
        for position in positions:
            x,y=position
            self.grille[y][x]=cote

    def placerPion(self,position,cote):
        """Place un pion sur le plateau et modifie celui-ci
        en conséquence selon les règle de l'othello.
        """
        self.insererPion(position,cote)
        return self.conquerir(position,cote)

    def estCaseVide(self, position):
        """Determine si la case à la position donnee est une case vide."""
        return self.obtenirCase(position)==cfg.CASE_VIDE

    def estCaseJoueur(self,position,cote):
        """Determine si la case à la position donnée
        contient un pion du joueur cote.
        """
        return self.obtenirCase(position)==cote

    def obtenirCoteOppose(self,cote_joueur):
        """Renvoie le cote oppose en fonction du cote donné."""
        cote_oppose = 1 - cote_joueur # technique du complément à 1.
        return cote_oppose

    def obtenirMouvementsValides(self,joueur_cote):
        """Retourne une liste de tuple qui correspondent aux coordonnees
        des mouvements possibles pour le joueur_cote.
        """
        cote = self.obtenirCoteOppose(joueur_cote)
        positions = self.obtenirPions(cote)
        positions_possibles = self.obtenirEnvironnement(positions)
        mouvements_valides = []
        for position_possible in positions_possibles:
            if self.estMouvementValide(position_possible, joueur_cote):
                mouvements_valides.append(position_possible)
        return mouvements_valides

    def estMouvementValide(self,mouvement,cote):
        """Permet de verifier si un mouvement est valide."""
        directions = self.obtenirDirections()
        resultat = False
        for direction in directions:
            ligne = self.obtenirLigneExclus(mouvement,direction)
            validite = self.estMouvementValideDansLigne(cote,ligne)
            if validite:
                resultat = True
                break
        return resultat

    def estMouvementValideDansLigne(self,cote,ligne):
        """Permet de verifier si un mouvement est valide dans une ligne."""
        valide = False
        possible = False
        cote_oppose = self.obtenirCoteOppose(cote)
        #Regarde si une ligne peut etre prise.
        for position in ligne: #Regarde chaque pion de la ligne dans l'ordre.
            if not self.estDansGrille(position): #Si on sort de la ligne, celle-ci ne peut pas être prise
                break #On arrete la vérification
            else:
                case = self.obtenirCase(position) #Sinon on récupère la case
                if case == cote: #Si la case est a nous
                    if possible: #et que l'on a déja rencontré des pions ennemis on peut prendre cette ligne.
                        valide = True
                    break #On arrete la vérification
                elif case == cote_oppose: #Si la case contient un pion ennemi alors on peut possiblement le prendre
                        possible = True
                else: #Sinon la case est vide et on arrete la vérification
                    break
        return valide

    def obtenirLigneInclus(self,position,vecteur,taille=None):
        """Récupère la ligne des valeurs obtenue
        avec une position et un vecteur.
        incluant la position de départ
        """
        if not taille:
            taille = max(self.taille)
        vx, vy = vecteur
        x, y = position
        n = 0
        ligne = []
        while self.estDansGrille((x,y)) and n < taille:
            ligne.append((x,y))
            x += vx
            y += vy
            n += 1
        return ligne

    def obtenirLigneExclus(self,position,vecteur,taille=None):
        """Récupère la ligne des valeurs obtenue
        avec une position et un vecteur.
        excluant la position de départ
        """
        if not taille:
            taille = max(self.taille)
        vx, vy = vecteur
        x, y = position
        n = 0
        x += vx
        y += vy
        ligne = []
        while self.estDansGrille((x,y)) and n < taille:
            ligne.append((x,y))
            x += vx
            y += vy
            n += 1
        return ligne

    def obtenirDirections(self):
        """Recupere les directions avec les vecteurs orientés selon chaque axe,
        ranger dans un ordre afin de tourner dans le sens trigo"""
        directions=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        return directions

    def conquerir(self,position,cote):
        """Permet au nouveau pion à la position 'position' de couleur 'cote' de
        retourner les autres pions"""
        directions = self.obtenirDirections()
        for direction in directions:
            ligne = self.obtenirLigneExclus(position,direction)
            self.conquerirLigne(cote,ligne)

    def conquerirLigne(self,cote,ligne):
        """Permet au nouveau pion a la position position de couleur cote de
        retouner les autres pions dans une ligne"""
        pions = []
        for position in ligne:
            if not self.estDansGrille(position):
                break
            case = self.obtenirCase(position)
            if case == cfg.CASE_VIDE:
                break
            if case != cote:
                pions.append(position)
            else:
                self.insererPion(pions, cote)
                break

    def presenter(self,positions,couleur,panneau,message=None,clear=True,
                  pause=True,couleur_texte=couleurs.NOIR):
        """Permet de debuger en 1 commande."""
        if self.demonstration:
            if type(positions) != list:
                positions = [positions]
            if clear: self.afficher()
            if positions:
                self.colorerCase(positions,couleur)
                if message:
                    position = self.obtenirPositionBrute([p-2/5 for p in positions[0]])
                    self.afficherTexte(message ,position, couleur_texte)
            panneau.coller(self.surface,0)
            panneau.afficher()
            panneau.flip()
            if pause:
                panneau.attendre(self.vitesse_demonstration)

    def afficherTexte(self,texte,position,couleur=None,taille=None):
        """Affiche du texte à l'écran."""
        if not couleur:
            couleur = cfg.THEME_PLATEAU["couleur texte"]
        if not taille:
            taille = cfg.THEME_PLATEAU["taille texte"]
        font = pygame.font.SysFont(cfg.THEME_PLATEAU["police"], taille)
        surface_texte = font.render(texte, 1, couleur)
        self.surface.blit(surface_texte, position)

    def colorerCase(self,positions,couleur):
        """Colorie une case du plateau d'une certaine couleur
        en affichant les contours d'un carre de couleur.
        Cette fonction est utile pour debug. Utilise la position
        dans le systeme de coordonnees du plateau et une couleur.
        """
        if not type(positions)==list: positions=[positions]
        for position in positions:
            x,y=self.obtenirPositionBrute(position)
            wsx,wsy=self.surface.get_size() #Taille d'un panneau en coordonnees de ce panneau
            sx,sy=self.taille #Taille du plateau en coordonnes du plateau
            cx=wsx/sx #Taille d'une case en x en coordonnees de la panneau
            cy=wsy/sy #Taille d'une case en y en coordonnees de la panneau
            mx=x-cx//2+1 #Position d'une case en x en coordonnees du panneau
            my=y-cy//2+1 #Position d'une case en y en coordonnees du panneau
            for i in range(2,6):
                pygame.draw.rect(self.surface,couleur,[mx+i,my+i,cx-2*i,cy-2*i],1)

    def afficher(self):
        """Affiche l'ensemble des éléments du plateau."""
        self.afficherFond()
        self.afficherGrille()
        self.afficherDecorationGrille()
        self.afficherMouvements()
        self.afficherPions()

    def afficherFond(self):
        """Permet de charger un arriere plan sur la surface."""
        ftx,fty=self.surface.get_size()
        # on colore le plateau de case de 10 pixel
        # pour produire un dégrader de couleur
        for y in range(0,fty,10):
            for x in range(0,ftx,10):
                r =       abs(outils.bijection(x,[0,ftx],[-100,100]))
                g = 255 - abs(outils.bijection((x+y)/2,[0,ftx],[-100,100]))
                b =       abs(outils.bijection(y,[0,fty],[-100,100]))
                couleur=(r,g,b)
                pygame.draw.rect(self.surface,couleur,[x,y,10,10],0)

    def afficherGrille(self):
        """Affiche la grille."""
        wsx, wsy = self.surface.get_size()
        sx, sy = self.taille
        for y in range(sy):
            _y = y * wsy // sy
            start = (0,_y)
            end = (wsx,_y)
            pygame.draw.line(self.surface,cfg.THEME_PLATEAU["couleur grille"],start,end,1)
        for x in range(sx):
            _x = x * wsx // sx
            start = (_x,0)
            end = (_x,wsy)
            pygame.draw.line(self.surface,cfg.THEME_PLATEAU["couleur grille"],start,end,1)

    def afficherDecorationGrille(self):
        """Affiche les 4 points pour délimiter le carré central du plateau.
        Aspect uniquement graphique et décoratif afin
        d'améliorer le confort de l'utilisateur.
        """
        wsx, wsy = self.surface.get_size()
        sx, sy = self.taille
        d = wsy // sy # distance entre deux ligne ou colonne
        positions_points_graphic = [(    2*d, 2*d), (    2*d, wsy-2*d),
                                    (wsx-2*d, 2*d), (wsx-2*d, wsy-2*d)]
        rayon = 5
        for position in positions_points_graphic:
            pygame.draw.circle(self.surface,cfg.THEME_PLATEAU["couleur grille"],position,rayon,0)

    def afficherPions(self): # pas rigoureux la taille_relative
        """Affiche les pions"""
        wsx , wsy = self.surface.get_size()
        sx, sy = self.taille
        rayon = int(min(wsx,wsy) / min(sx,sy) * cfg.THEME_PLATEAU["rayon relatif pion"])
        for y in range(sy):
            for x in range(sx):
                case = self.obtenirCase((x,y))
                position_brute = self.obtenirPositionBrute((x,y))
                if 0 <= case <= len(cfg.THEME_PLATEAU["couleur pions"]) - 1:
                    couleur = cfg.THEME_PLATEAU["couleur pions"][case]
                    pygame.draw.circle(self.surface,couleurs.inverser(couleur),position_brute,rayon+2,0)
                    pygame.draw.circle(self.surface,couleur,position_brute,rayon,0)

    def afficherMouvements(self):
        """Afficher les coups possible. (rond rouge sur le plateau)"""
        if cfg.THEME_PLATEAU["aide mouvement"]:
            couleur = cfg.THEME_PLATEAU["couleur mouvement"]
            #devrait  marcher si il n'y a que un mouvement.
            for mouvement in self.mouvements:
                wsx, wsy = self.surface.get_size()
                sx, sy = self.taille
                rayon = int(min(wsx,wsy) / min(sx,sy)*cfg.THEME_PLATEAU["rayon relatif mouvement"])
                position_brute = self.obtenirPositionBrute(mouvement)
                #affiche des bord aux couleurs, bonne idées mais mal implemente
                pygame.draw.circle(self.surface,(100,0,0),position_brute,rayon+2,0)
                pygame.draw.circle(self.surface,couleur,position_brute,rayon,0)

    def afficherAnimation(self,choix):
        """Affiche le coup joueur avec un contour rouge."""
        wsx, wsy = self.surface.get_size()
        sx, sy = self.taille
        case = self.obtenirCase(choix)
        couleur = cfg.THEME_PLATEAU["couleur pions"][case]
        position=self.obtenirPositionBrute(choix)
        rayon=int((min(wsx,wsy) / min(sx,sy)) * cfg.THEME_PLATEAU["rayon relatif pion"])
        pygame.draw.circle(self.surface,cfg.THEME_PLATEAU["couleur animation pion"],position,rayon+2,0)
        pygame.draw.circle(self.surface,couleur,position,rayon,0)
