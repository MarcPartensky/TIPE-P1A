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
#    Créateurs : Alexandre BIGOT
#                Valentin  COLIN
#                Marc  PARTENSKY
#
#    Version : 2019
#
################################################################################
#
#                           SOMMAIRE de Fenetre
#    0.    generer_constante () ......................................... ligne 83
#
#    1.    class PlateauAnalysable (plateau):  .......................... ligne 96
#    1.1   ------> __init__ (self,(etc).)  .............................. ligne 100
#    1.2   ------> obtenirToutesLesLignes(self)  ........................ ligne 109
#    1.3   ------> obtenirToutesLesLignesSansDirection(self)  ........... ligne 125
#    1.4   ------> presenterPionsStables(self,fenetre)  ................. ligne 138
#    1.5   ------> obtenirTousLesPionsDefinitivementStables(self,etc) ... ligne 158
#    1.6   ------> estUnPionDefinitivementStable(self,pion,panneau) ..... ligne 168
#    1.7   ------> obtenirTousLesPionsStables(self,cote,fenetre)  ....... ligne 196
#    1.8   ------> estUnPionStable(self,pion,fenetre,niveau=1)  ......... ligne 205
#    1.9   ------> obtenirTousLesPionsPrenables(self,cote,fenetre)  ..... ligne 226
#    1.10  ------> estUnPionPrenable(self,pion)  ........................ ligne 235
#    1.11  ------> estLigneDefinitivementStable(self,ligne)  ............ ligne 250
#    1.12  ------> test_parite_avantageuse(self)  ....................... ligne 262
#    1.13  ------> obtenir_couleur_position(self, position)  ............ ligne 268
#    1.14  ------> obtenirCoinQuartier(self, pos)  ...................... ligne 272
#    1.15  ------> possessionCoinDuQuartier(self,pos, cote)  ............ ligne 283
#    1.16  ------> testSiJoueurCotePossedeUneDeCesPositions(self,etc)  .. ligne 288
#    1.17  ------> testSiJoueurCotePossedeTouesCesPositions(self,etc)  .. ligne 298
#    1.18  ------> test_si_le_joueur_cote_peut_prendre_position(self,etc) ligne 308
#    1.19  ------> est_coup_bourbier_par_cote(self, pos, cote)  ......... ligne 329
#    1.20  ------> obtenir_coups_bourbier(self, cote)  .................. ligne 337
#    1.21  ------> Nombre_pion_retourne(self, pos, cote) ................ ligne 343
#    1.22  ------> Augmentation_coup_possible_adv_dans_zone(self,etc)  .. ligne 352
#    1.23  ------> Nombre_pion_stable_zone(self, cote, zone)  ........... ligne 364
#    1.24  ------> Augmentation_pion_stable_dans_zone(self,etc)  ........ ligne 373
#    1.25  ------> Augmentation_pion_dans_zone(self, cote, zone, pos)  .. ligne 382
#    1.26  ------> Nombre_coin_adjacent_pris(self, cote, pos_coin)  ..... ligne 391
#    1.27  ------> position_stable_pour_cote(self, position, cote)  ..... ligne 404
#    1.28  ------> __deepcopy__(self,memoire_inutile)  .................. ligne 432
#
################################################################################
"""
# --coding:utf-8--
from plateau import Plateau
from config import debug

import config as cfg
import outils, couleurs, copy

# La liste des différentes zone de jeu :
# Ne doit pas etre une liste
ZONE_COIN = 4
ZONE_VERTE = 3
ZONE_BLANCHE = 2
ZONE_ROUGE = 1
ZONE_NOIRE = 0
ZONE_TOUT = -1

LISTE_ZONES = [ZONE_COIN, ZONE_VERTE, ZONE_BLANCHE, ZONE_ROUGE, ZONE_NOIRE, ZONE_TOUT]

PLATEAU_COLORE = [
    [
        ZONE_COIN,
        ZONE_NOIRE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_NOIRE,
        ZONE_COIN,
    ],
    [
        ZONE_NOIRE,
        ZONE_NOIRE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_NOIRE,
        ZONE_NOIRE,
    ],
    [
        ZONE_VERTE,
        ZONE_ROUGE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_ROUGE,
        ZONE_VERTE,
    ],
    [
        ZONE_VERTE,
        ZONE_ROUGE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_ROUGE,
        ZONE_VERTE,
    ],
    [
        ZONE_VERTE,
        ZONE_ROUGE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_ROUGE,
        ZONE_VERTE,
    ],
    [
        ZONE_VERTE,
        ZONE_ROUGE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_BLANCHE,
        ZONE_ROUGE,
        ZONE_VERTE,
    ],
    [
        ZONE_NOIRE,
        ZONE_NOIRE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_ROUGE,
        ZONE_NOIRE,
        ZONE_NOIRE,
    ],
    [
        ZONE_COIN,
        ZONE_NOIRE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_VERTE,
        ZONE_NOIRE,
        ZONE_COIN,
    ],
]

LISTE_POSITION_ZONE = {}


def generer_constante():
    """Permet de génerer LISTE_POSITION_ZONE."""
    for i in range(len(LISTE_ZONES)):
        result = []
        key = LISTE_ZONES[i]
        for x in range(len(PLATEAU_COLORE)):
            for y in range(len(PLATEAU_COLORE[x])):
                if PLATEAU_COLORE[x][y] == key or key == ZONE_TOUT:
                    result.append((x, y))
        LISTE_POSITION_ZONE[key] = result


generer_constante()


class PlateauAnalysable(Plateau):
    """Le plateau analysable est une classe qui hérite de plateau et qui fournit
    des outils d'analyses supplémentaires pour les intelligences artificielles."""

    def __init__(self, *args, **kwargs):
        """Créer un plateau analysable."""
        if kwargs.get("ne_pas_initialiser", False):
            return None
        self.vitesse_demonstration = (
            1  # Possibilité de changer la vitesse de démonstration.
        )
        super().__init__(*args, **kwargs)
        # super() Retourne la classe mère de PlateauAnalysable, c'est Plateau.
        # On initialise l'instance de PlateauAnalysable comme s'il s'agissait d'une instance de Plateau.

    def obtenirToutesLesLignes(self):
        """Renvoie la liste de toutes les lignes possibles de la grille."""
        lignes = []
        tx, ty = self.taille
        m = max(self.taille)
        for y in range(ty):
            for x in range(tx):
                for direction in self.obtenirDirections():
                    for n in range(m):
                        position = (x, y)
                        ligne = self.obtenirLigneInclus(position, direction, n)
                        lignes.append(tuple(ligne))
        lignes = list(set(lignes))
        vrai_lignes = [list(ligne) for ligne in lignes]
        return vrai_lignes

    def obtenirToutesLesLignesSansDirection(self):
        """Renvoie toutes les lignes possibles de la grille mais
        sans prendre en compte l'ordre des positions de celles-ci.
        """
        lignes = self.obtenirToutesLesLignes()
        lignes_triees = []
        for ligne in lignes:
            ligne.sort()
            lignes_triees.append(tuple(ligne))
        lignes_triees = list(set(lignes_triees))
        lignes = []
        for ligne_triee in lignes_triees:
            lignes.append(list(ligne_triee))
        return lignes

    def presenterPionsStables(self, fenetre):  # Obsolète
        """Présente les pions stables a l'ecran en les trouvant,
        cela s'effectue avec la fenêtre.
        """
        self.afficher()
        fenetre.coller(self.surface, 0)
        fenetre.afficher()
        fenetre.flip()
        tous_les_pions = []
        for i in range(2):
            pions = self.obtenirTousLesPionsDefinitivementStables(i, fenetre)
            tous_les_pions.append(pions)
            self.presenter(
                pions,
                self.pieces_couleur[i],
                fenetre,
                message="pions stables",
                pause=True,
            )
        cfg.debug("Pions définitivement stables:", tous_les_pions)
        fenetre.clear()
        plateau.afficher(fenetre)
        for i in range(2):
            plateau.presenter(
                tous_les_pions[i],
                self.pieces_couleur[i],
                fenetre,
                message="pions stables",
                clear=False,
            )
        if tous_les_pions.count([]) != 2:
            fenetre.attendre()  # Par défaut la fenêtre attend 1 seconde.

    def obtenirTousLesPionsDefinitivementStables(self, cote, panneau):
        """Renvoie la liste de tous les pions qui sont definitivement stables."""
        stables = []
        pions = self.obtenirPions(cote)
        # plateau.presenter(pions,couleurs.ROUGE,fenetre,"pions"+str(cote))
        for pion in pions:
            if self.estUnPionDefinitivementStable(pion, panneau):
                stables.append(pion)
        return stables

    def estUnPionDefinitivementStable(self, pion, panneau):
        """Determine si un pion est définivement stable en déterminant
        pour chaque ligne auquel il appartient,
        si il peut être définitivement stable.
        Pour cela, on se ramène à un problème plus simple:
                c'est à dire vérifier la stabilité d'un pion dans une ligne.
        Ainsi on vérifie pour chaque ligne auquelle ce pion appartient,
        si celui-ci peut-être définitivment stable, et si c'est bien le cas,
        alors ce pion est définitivment stable sans équivoque."""
        cote = self.obtenirCase(pion)
        lignes = self.obtenirLignesAlentours(pion)  # lignes de positions
        cote_oppose = self.obtenirCoteOppose(cote)
        stable = True
        for (i, ligne) in enumerate(lignes):
            ci = (i + 4) % 8
            ligne_oppose = lignes[
                ci
            ]  # Permet de récupérer la ligne qui est située a l'opposée de la i-ème ligne.
            cases = self.obtenirCases(ligne)  # lignes de contenus de cases
            cases_opposees = self.obtenirCases(ligne_oppose)
            if cote_oppose in cases:
                if cfg.CASE_VIDE in cases_opposees:
                    stable = False
            if cfg.CASE_VIDE in cases:
                if (cote_oppose in cases_opposees) or (cfg.CASE_VIDE in cases_opposees):
                    stable = False
            # Présentation des lignes sur l'écran pour le mode démonstration.
            self.presenter(ligne, couleurs.BLEU, panneau, "ligne", pause=False)
            self.presenter(
                ligne_oppose,
                couleurs.VIOLET,
                panneau,
                "ligne oppose",
                clear=False,
                pause=False,
            )
            self.presenter(pion, couleurs.ROUGE, panneau, "pion teste", clear=False)
            if not stable:
                break
        return stable

    def obtenirTousLesPionsStables(self, cote, fenetre):
        """Renvoie la liste de tous les pions stables sur le plateau appartenant au joueur du côté 'cote'."""
        pions = self.obtenirPions(cote)
        pions_stables = []
        for pion in pions:
            if self.estUnPionStable(pion, fenetre):
                pions_stables.append(pion)
        return pions

    def estUnPionStable(
        self, pion, fenetre, niveau=1
    ):  # Cette fonction a été remplacée par le concept de stabilité d'Alexandre.
        """Détermine si un pion est stable selon le concept obselète de Marc."""
        cote = self.obtenirCase(pion)  # Obtient le côté du joueur ayant posé le pion.
        cote_oppose = self.obtenirCoteOppose(
            cote
        )  # Récupère le côté opposé avec le côté du joueur.
        mouvements = self.obtenirMouvementsValides(
            cote_oppose
        )  # Récupère tous les mouvements enemis.
        # Détermine si un pion est imprenable.
        if not self.estUnPionPrenable(pion):  # Si c'est le cas, il est stable.
            stable = True  # On retient le fait que le pion soit stable.
        else:  # Sinon lorsqu'il est prenable, il est stable uniquement si celui-ci devient instable après être pris.
            stable = True  # On suppose au départ le pion stable, et on cherche un mouvement qui perment de discréditer cette supposition.
            for (
                mouvement
            ) in mouvements:  # Fait une itération de chaque mouvement un par un.
                nouveau_plateau = copy.deepcopy(
                    self
                )  # On copie le plateau pour simuler chaque mouvement ennemi.
                nouveau_plateau.placerPion(
                    mouvement, cote_oppose
                )  # On joue le mouvement ennemi itéré dans le nouveau plateau.
                nouveau_cote = nouveau_plateau.obtenirCase(
                    pion
                )  # On récupère la couleur du pion après le mouvement enemi.
                if (
                    nouveau_cote != cote
                ):  # Détermine si ce pion est pris i.e. si la couleur de ce pion dans le nouveau plateau est différente de celle d'avant.
                    nouveau_plateau.presenter(
                        pion,
                        couleurs.ORANGE,
                        fenetre,
                        "niveau:" + str(niveau),
                        couleur_texte=couleurs.ORANGE,
                    )  # Affiche le pion que l'on considère et le niveau de récusion
                    if nouveau_plateau.estUnPionStable(
                        pion, fenetre, niveau + 1
                    ):  # Détermine si ce pion devient stable après être pris.
                        stable = False  # Si c'est le cas alors forcément il n'est pas devenu instable donc le pion ne pouvait pas être stable à la base.
                        break  # Donc comme ce pion ne peut pas être stable, il n'y a pas de raison de vérifier s'il peut l'être pour d'autre mouvements.
        return stable  # On renvoie le booléen correspondant à la stabilité du pion.

    def obtenirTousLesPionsPrenables(self, cote, fenetre):
        """Renvoie la liste de tous les pions d'un côté 'cote' qui sont prenables au tour suivant."""
        pions = self.obtenirPions(cote)
        prenables = []
        for pion in pions:
            if self.estUnPionPrenable(pion):
                prenables.append(pion)
        return prenables

    def estUnPionPrenable(self, pion):
        """Détermine si un pion est prenable à l'instant en utilisant le pion."""
        cote = self.obtenirCase(pion)
        cote_oppose = self.obtenirCoteOppose(cote)
        mouvements = self.obtenirMouvementsValides(cote_oppose)
        prenable = False
        for mouvement in mouvements:
            nouveau_plateau = copy.deepcopy(self)
            nouveau_plateau.placerPion(mouvement, cote_oppose)
            nouveau_cote = nouveau_plateau.obtenirCase(pion)
            if nouveau_cote != cote:
                prenable = True
                break
        return prenable

    def estLigneDefinitivementStable(self, ligne):
        """Détermine si une ligne est stable selon le concept de stabilité obselète de Marc."""
        ligne = outils.obtenirLigneComplete(ligne)
        stable = True
        for pion in ligne:
            if not pion in self.pions_stables:
                stable = False
                break
        return stable

    # Les fonctions suivantes sont les méthodes de la classe ia.py déplacées dans plateau_analyable.py.

    def test_parite_avantageuse(self):
        """Détermine si la parité est à priori avantageuse pour le joueur qui est sur le point de jouer
        On fait l'approximation suivante :
        Si le nombre de case restante est impaire c'est avantageux."""
        return self.obtenirNombrePionsRestant() % 2 == 1

    def obtenir_couleur_position(self, position):
        """Retourne la couleur de la position position, il s'agit également de la zone dans laquelle est la position."""
        return PLATEAU_COLORE[position[0]][position[1]]

    def obtenirCoinQuartier(self, pos):
        """Retourne la position du coin le plus proche de la position 'pos'."""
        return [
            [(0, 0), (0, 0), (0, 0), (0, 0), (0, 7), (0, 7), (0, 7), (0, 7)],
            [(0, 0), (0, 0), (0, 0), (0, 0), (0, 7), (0, 7), (0, 7), (0, 7)],
            [(0, 0), (0, 0), (0, 0), (0, 0), (0, 7), (0, 7), (0, 7), (0, 7)],
            [(0, 0), (0, 0), (0, 0), (0, 0), (0, 7), (0, 7), (0, 7), (0, 7)],
            [(7, 0), (7, 0), (7, 0), (7, 0), (7, 7), (7, 7), (7, 7), (7, 7)],
            [(7, 0), (7, 0), (7, 0), (7, 0), (7, 7), (7, 7), (7, 7), (7, 7)],
            [(7, 0), (7, 0), (7, 0), (7, 0), (7, 7), (7, 7), (7, 7), (7, 7)],
            [(7, 0), (7, 0), (7, 0), (7, 0), (7, 7), (7, 7), (7, 7), (7, 7)],
        ][pos[0]][pos[1]]

    def possessionCoinDuQuartier(self, pos, cote):
        """Retourne si le joueur de côté 'cote' possède le coin le plus proche de
        la position 'pos' dans le plateau plateau."""
        return self.estCaseJoueur(self.obtenirCoinQuartier(pos), cote)

    def testSiJoueurCotePossedeUneDeCesPositions(self, cote, positions):
        """Prend une liste de positions dans le plateau et vérifie si le joueur
        de côté 'cote' possède un pion à l'une des position de la liste positions."""
        resultat = False
        for position in positions:
            if self.estCaseJoueur(position, cote):
                resultat = True
                break
        return resultat

    def testSiJoueurCotePossedeTouesCesPositions(self, cote, positions):
        """Prend une liste de positions dans le plateau et vérifie si le joueur
        de côté 'cote' possède tous les pions sur les position de la liste."""
        resultat = True
        for position in positions:
            if not (self.estCaseJoueur(position, cote)):
                resultat = False
                break
        return resultat

    def test_si_le_joueur_cote_peut_prendre_position(
        self, cote, positions
    ):  # c'est utilisé ?
        """On a un plateau, c'est le tour de joueur de côté 'cote' et on souhaite
        déterminer, si dans ses mouvements possibles, un permet d'avoir une pion
        de sa couleur dans une des positions de la liste positions dans le plateau
        positions peut être une liste ou simple coo (si ).
        """
        from copy import deepcopy

        resultat = False
        if isinstance(positions, tuple):
            if (
                len(positions) == 2
            ):  #'positions' n'est pas une liste de positions mais juste une couple de coordonnées.
                postions = [positions]
        mouvements_possible_cote = self.obtenirMouvementsValides(cote)
        for position_posible_joueur_cote in mouvements_possible_cote:
            plateau_simulation = deepcopy(self)
            plateau_simulation.placerPion(position_posible_joueur_cote, cote)
            if self.testSiJoueurCotePossedeUneDeCesPositions(positions, cote):
                # On vérifie si le  coup a permis de prendre une des positions.
                resultat = True
                break
        return resultat

    def est_coup_bourbier_par_cote(self, pos, cote):
        """Détermine si le coup à la position 'pos' joué par le joueur de côté
        'cote' empêche l'adversaire de jouer au prochain tour."""
        cote_oppose = 1 - cote
        plateau_simulation = copy.deepcopy(self)
        plateau_simulation.placerPion(pos, cote)
        return len(plateau_simulation.obtenirMouvementsValides(cote_oppose)) == 0

    def obtenir_coups_bourbier(self, cote):
        """Retourne la liste de tout les coups bourbier parmi les coups possibles
        pour le joueur de coté 'cote'."""
        MouvementsValides = self.obtenirMouvementsValides(cote)
        return [
            mouvement
            for mouvement in MouvementsValides
            if self.est_coup_bourbier_par_cote(mouvement, cote)
        ]

    def Nombre_pion_retourne(self, pos, cote):
        """ "Renvoie le nombre de pion qui sont retournés lorsque self pose un
        pion à la position 'pos' sur le plateau."""
        plateau_simulation = copy.deepcopy(self)
        nombre_init = plateau_simulation.compterPions(pos)
        plateau_simulation.placerPion(pos, cote)
        nombre_final = plateau_simulation.compterPions(pos)
        return (
            nombre_final - nombre_init - 1
        )  # -1 Car on pose un pion et ce pion n'a pas été retourné.

    def Augmentation_coup_possible_adv_dans_zone(self, pos, zone, cote):
        """ "Renvoie de combien augmente le nombre de coup possible de l'adversaire
        dans la zone 'zone' après que self ait joué à position 'pos'."""
        cote_oppose = 1 - cote
        plateau_simulation = copy.deepcopy(self)
        coup_possible_dans_zone = outils.intersection(
            plateau_simulation.obtenirMouvementsValides(cote_oppose),
            LISTE_POSITION_ZONE[zone],
        )
        nombre_coup_possible_dans_zone = len(coup_possible_dans_zone)
        plateau_simulation.placerPion(pos, cote)
        final_coup_possible_dans_zone = outils.intersection(
            plateau_simulation.obtenirMouvementsValides(cote_oppose),
            LISTE_POSITION_ZONE[zone],
        )
        final_nombre_coup_possible_dans_zone = len(final_coup_possible_dans_zone)
        return final_nombre_coup_possible_dans_zone - nombre_coup_possible_dans_zone

    def Nombre_pion_stable_zone(self, cote, zone):
        """Détermine le nombre de pions stables avec le côté 'cote' et la zone 'zone'."""
        resultat = 0
        position_pion_zone = outils.intersection(
            self.obtenirPions(cote), LISTE_POSITION_ZONE[zone]
        )
        for pos in position_pion_zone:
            if self.position_stable_pour_cote(pos, cote):
                resultat += 1
        return resultat

    def Augmentation_pion_stable_dans_zone(self, cote, zone, pos):
        """ "Renvoie de combien augmente le nombre de pions stables de côté 'cote'
        dans la zone 'zone' après que le joueur ait joué à la position 'pos'."""
        nombre_initial = self.Nombre_pion_stable_zone(cote, zone)
        plateau_simulation = copy.deepcopy(self)
        plateau_simulation.placerPion(pos, cote)
        nombre_final = plateau_simulation.Nombre_pion_stable_zone(cote, zone)
        return nombre_final - nombre_initial

    def Augmentation_pion_dans_zone(self, cote, zone, pos):
        """ "Renvoie de combien on augmente le nombre de pion de côté 'cote' dans
        la zone 'zone' après que joueur joue à la position 'pos'."""
        plateau_simulation = copy.deepcopy(self)
        nombre_initial = len(
            outils.intersection(
                plateau_simulation.obtenirPions(cote), LISTE_POSITION_ZONE[zone]
            )
        )
        plateau_simulation.placerPion(pos, cote)
        nombre_final = len(
            outils.intersection(
                plateau_simulation.obtenirPions(cote), LISTE_POSITION_ZONE[zone]
            )
        )
        return nombre_final - nombre_initial

    def Nombre_coin_adjacent_pris(self, cote, pos_coin):
        """Renvoie le nombre de coin adjacents pris, avec le côté du joueur de côté
        'cote' et la position du coin."""
        resultat = 0
        x, y = pos_coin
        size = self.taille_x - 1
        modulo = 2 * size
        if self.estCaseJoueur(((x + size) % modulo, y), cote):
            resultat += 1
        if self.estCaseJoueur((x, (y + size) % modulo), cote):
            resultat += 1
        return resultat

    def position_stable_pour_cote(self, position, cote):
        """Détermine si une position est stable pour un côté avec la position
        'position' et le côté 'cote'."""
        cote_oppose = 1 - cote
        liste_des_cas_particuliers = {}
        mouv_valide_adv = self.obtenirMouvementsValides(cote_oppose)
        for mouv in mouv_valide_adv:
            plateau_simulation = copy.deepcopy(self)
            plateau_simulation.placerPion(mouv, cote_oppose)
            if plateau_simulation.estCaseJoueur(position, cote_oppose):
                # On est dans le deuxième cas
                liste_des_cas_particuliers[tuple(mouv)] = plateau_simulation
        if liste_des_cas_particuliers == {}:
            # L'adversaire ne peut pas prendre la position quelque soit son coup.
            return True
        else:
            for mouv_cas_particulier in liste_des_cas_particuliers:
                # La position est alors stable si pour tout les mouvements la
                # position est instable pour côté opposé.
                plateau_de_ce_cas = liste_des_cas_particuliers[mouv_cas_particulier]
                if plateau_de_ce_cas.position_stable_pour_cote(position, cote_oppose):
                    # L'adversaire a réussi a former une position stable, cela
                    # signifie que la position de départ n'était pas stable.
                    return False
            # L'adversaire ne peut pas former une position stable en prenant notre
            # pion, notre position est donc stable
            return True

    def __deepcopy__(self, memoire_inutile):
        """Il s'agit d'une méthode spéciale qui est executée lorsque deepcopy du module copy souhaite faire une copie
        d'un plateau analysable.
        Renvoie une copie du plateau juste en lui copiant tous ses attributs sauf les attributs suivant :
        taille, vitesse_demonstration, surface, taille_x, taille_y, nombre_de_joueurs et demonstration.
        """
        plateau = PlateauAnalysable(ne_pas_initialiser=True)
        # Ce paramètre optionnel permet de ne pas initialiser l'objet
        # Comme les autres: plateau ne reçoit aucun attributs lors de son
        # initialisation, on les lui donne "manuellement" avec les lignes
        # suivantes:
        keys = self.__dict__.keys()
        for key in keys:
            if key in (
                "taille",
                "vitesse_demonstration",
                "surface",
                "taille_x",
                "taille_y",
                "nombre_de_joueurs",
                "demonstration",
            ):
                plateau.__dict__[key] = self.__dict__[key]
            else:
                plateau.__dict__[key] = copy.deepcopy(self.__dict__[key])
        return plateau
