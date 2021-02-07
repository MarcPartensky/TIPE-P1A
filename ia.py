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
#                             SOMMAIRE de Cyrano
#
#    1.    class Cyrano (joueur.Robot):  ........................... ligne  63
#    1.1   ---->  __init__ (self,nom=None)  ........................ ligne  66
#    1.2   ---->  reinitialiser (self, plateau)  ................... ligne  72
#    1.3   ---->  main (self, plateau, fenetre=None)  .............. ligne  79
#    1.4   ---->  comparer_blanc (self, pos1, pos2)  ............... ligne  88
#    1.5   ---->  comparer_rouge (self, pos1, pos2)  ............... ligne 124
#    1.6   ---->  comparer_vert(self, pos1, pos2)  ................. ligne 144
#    1.7   ---->  comparer_noir(self, pos1, pos2)  ................. ligne 173
#    1.8   ---->  comparer_coin(self, pos1, pos2)  ................. ligne 199
#    1.9   ---->  comparer_blanc_rouge(self, blanc, rouge)  ........ ligne 225
#    1.10  ---->  comparer_blanc_vert(self, blanc, vert)  .......... ligne 228
#    1.11  ---->  comparer_blanc_noir(self, blanc, noir)  .......... ligne 245
#    1.12  ---->  comparer_blanc_coin(self, blanc, coin)  .......... ligne 248
#    1.13  ---->  comparer_rouge_vert(self, rouge, vert)  .......... ligne 251
#    1.14  ---->  comparer_rouge_noir(self, rouge, noir)  .......... ligne 268
#    1.15  ---->  comparer_rouge_coin(self, rouge, coin)  .......... ligne 288
#    1.16  ---->  comparer_vert_noir (self, vert, noir)  ........... ligne 291
#    1.17  ---->  comparer_vert_coin (self, vert, coin)  ........... ligne 306
#    1.18  ---->  comparer_noir_coin (self, noir, coin)  ........... ligne 309
#    1.19  ---->  comparer_2_positions (self,position1,position2)  . ligne 312
#    1.20  ---->  comparer_n_positions (self, *args)  .............. ligne 370
#
###############################################################################
"""
# --coding:utf-8--

from outils import intersection, est_superieur
from plateau_analysable import PlateauAnalysable
import outils, joueur
import config as cfg
from copy import deepcopy

# La liste des différentes zone de jeu :
# Ne doit pas être une liste
ZONE_COIN = 4
ZONE_VERTE = 3
ZONE_BLANCHE = 2
ZONE_ROUGE = 1
ZONE_NOIRE = 0
ZONE_TOUT = -1


class Cyrano(joueur.Robot):
    """Classe d'IA NON-naïve"""

    def __init__(self, nom=None):
        "Lance l'__init__ de la classe joueur.Robot"
        super().__init__(nom)
        # super() retourne la classe mère de IA, c'est joueur.Robot
        # on initialise l'instance IA comme s'il s'agisasit d'une instance de Plateau

    def reinitialiser(self, plateau):
        """Cette fonction est lancée au debut de chaque tour.
        Ici on definit des variables qui ne vont pas etre modifiées pendant
        tout le tour afin d'economiser du temps...
        """
        self.plateau = plateau  # il ne faut pas faire de simulations sur ce plateau !
        self.mouvements_possibles = plateau.obtenirMouvementsValides(self.cote)
        self.parite_desavantageuse = not (plateau.test_parite_avantageuse())

    def main(self, plateau, fenetre=None):
        """Méthode principale de la classe.
        Cette méthode est executé lorsque l'IA doit jouer :
        elle prend en paramètre le plateau actuel et
        renvoie la position choisie
        """
        self.fenetre = fenetre
        self.reinitialiser(plateau)  # Il faut prendre en compte le nouveau plateau
        return self.comparer_n_positions(*self.mouvements_possibles)
        # Les prochaines méthodes permettent de comparer les positions

    def comparer_blanc(self, pos1, pos2):
        """Comparer deux positions de couleur blanche"""
        coeff1, coeff2 = [], []

        # Les méthodes de comparaisons à partir des couleurs sont toutes construites de la même façon.
        # A chaque position, on associe une liste.
        # En fonction des critères ordonnés de l'algorithme que l'on applique sur chaque position, on ajoute un
        # coefficient dans la liste correspondante : plus le coefficient est élevé, plus le coup est favorisé.
        # Si le critère est qualitatif, le coefficient peut être des Booléens converti en 0 ou 1.
        # Si le critère est quantitatif, le coefficient est la quantité examinée (éventuellement multiplié par -1
        # si le critère demande de limiter cette quantité)
        # Enfin, pour déterminer la position choisie, il suffit de comparer les deux listes termes par terme : cf la
        # fonction est_superieur dans outils.py

        # Le coefficeint ci dessous est un porduit astucieux :
        # Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
        # de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
        # des coups proposes.
        # Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
        # il n'influe donc pas dans  la selection du coup

        coeff1.append(
            self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)
            * self.parite_desavantageuse
        )
        coeff2.append(
            self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)
            * self.parite_desavantageuse
        )

        coeff1.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos1, ZONE_TOUT, self.cote
            )
        )
        coeff2.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos2, ZONE_TOUT, self.cote
            )
        )

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        if est_superieur(coeff1, coeff2):
            return pos1
        else:
            return pos2

    def comparer_rouge(self, pos1, pos2):
        """Permet de comparer deux positions rouge"""
        coeff1, coeff2 = [], []
        coeff1.append(
            self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)
            * self.parite_desavantageuse
        )
        coeff2.append(
            self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)
            * self.parite_desavantageuse
        )

        coeff1.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos1, ZONE_VERTE, self.cote
            )
        )
        coeff2.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos2, ZONE_VERTE, self.cote
            )
        )

        coeff1.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos1, ZONE_TOUT, self.cote
            )
        )
        coeff2.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos2, ZONE_TOUT, self.cote
            )
        )

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        if est_superieur(coeff1, coeff2):
            return pos1
        else:
            return pos2

    def comparer_vert(self, pos1, pos2):
        """On produit ci dessous est en fait une astuce :
        Si self.parite_desavantageuse est True, la parite est desavantgeuse,
        il faut essayer de faire passer le tour de l'adversaire, pour cela,
        on cherche un "coup bourbier",
        il faut donc en prendre compte dans la selection des coups proposes.
        Sinon, alors self.parite_desavantageuse est False et
        le produit est dans les deux cas egal à 0
        il n'influe donc pas dans la selection du coup
        """
        coeff1, coeff2 = [], []

        coeff1.append(
            self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)
            * self.parite_desavantageuse
        )
        coeff2.append(
            self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)
            * self.parite_desavantageuse
        )

        coeff1.append(int(self.plateau.position_stable_pour_cote(pos1, self.cote)))
        coeff2.append(int(self.plateau.position_stable_pour_cote(pos2, self.cote)))

        coeff1.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos1, ZONE_VERTE, self.cote
            )
        )
        coeff2.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos2, ZONE_VERTE, self.cote
            )
        )

        coeff1.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos1, ZONE_TOUT, self.cote
            )
        )
        coeff2.append(
            -1
            * self.plateau.Augmentation_coup_possible_adv_dans_zone(
                pos2, ZONE_TOUT, self.cote
            )
        )

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        if est_superieur(coeff1, coeff2):
            return pos1
        else:
            return pos2

    def comparer_noir(self, pos1, pos2):
        """On produit ci dessous est en fait une astuce :
        Si self.parite_desavantageuse est True, la parite est desavantgeuse,
        il faut essayer de faire passer le tour de l'adversaire,
        pour cela, on cherche un "coup bourbier",
        il faut donc en prendre compte dans la selection des coups proposes.
        Sinon, alors self.parite_desavantageuse est False et
        le porduit est dans les deux cas egal à 0
        il n'influe donc pas dans la selection du coup
        """
        coeff1, coeff2 = [], []

        coeff1.append(
            self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)
            * self.parite_desavantageuse
        )
        coeff2.append(
            self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)
            * self.parite_desavantageuse
        )

        coeff1.append(int(self.plateau.position_stable_pour_cote(pos1, self.cote)))
        coeff2.append(int(self.plateau.position_stable_pour_cote(pos2, self.cote)))

        coeff1.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos1)
        )
        coeff2.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos2)
        )

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        if est_superieur(coeff1, coeff2):
            return pos1
        else:
            return pos2

    def comparer_coin(self, pos1, pos2):
        """On produit ci dessous est en fait une astuce :
        Si self.parite_desavantageuse est True, la parite est desavantgeuse,
        il faut essayer de faire passer le tour
        de l'adversaire, pour cela, on cherche un "coup bourbier",
        il faut donc en prendre compte dans la selection des coups proposes.
        Sinon, alors self.parite_desavantageuse est False et
        le porduit est dans les deux cas egal à 0
        il n'influe donc pas dans la selection du coup
        """
        coeff1, coeff2 = [], []

        coeff1.append(
            self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)
            * self.parite_desavantageuse
        )
        coeff2.append(
            self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)
            * self.parite_desavantageuse
        )

        coeff1.append(self.plateau.Nombre_coin_adjacent_pris(self.cote, pos1))
        coeff2.append(self.plateau.Nombre_coin_adjacent_pris(self.cote, pos2))

        coeff1.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos1)
        )
        coeff2.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos2)
        )

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        if est_superieur(coeff1, coeff2):
            return pos1
        else:
            return pos2

    def comparer_blanc_rouge(self, blanc, rouge):
        return blanc

    def comparer_blanc_vert(self, blanc, vert):
        coeff_blanc, coeff_vert = [], []

        coeff_blanc.append(
            self.plateau.est_coup_bourbier_par_cote(blanc, self.cote)
            * self.parite_desavantageuse
        )
        coeff_vert.append(
            self.plateau.est_coup_bourbier_par_cote(vert, self.cote)
            * self.parite_desavantageuse
        )

        coeff_blanc.append(
            int(not (self.plateau.position_stable_pour_cote(vert, self.cote)))
        )
        coeff_vert.append(1)

        coeff_blanc.append(1)
        coeff_vert.append(0)

        if est_superieur(coeff_blanc, coeff_vert):
            return blanc
        else:
            return vert

    def comparer_blanc_noir(self, blanc, noir):
        return blanc

    def comparer_blanc_coin(self, blanc, coin):
        return coin

    def comparer_rouge_vert(self, rouge, vert):
        coeff_rouge, coeff_vert = [], []

        coeff_rouge.append(
            int(not (self.plateau.position_stable_pour_cote(vert, self.cote)))
        )
        coeff_vert.append(1)

        coeff_rouge.append(
            self.plateau.est_coup_bourbier_par_cote(rouge, self.cote)
            * self.parite_desavantageuse
        )
        coeff_vert.append(
            self.plateau.est_coup_bourbier_par_cote(vert, self.cote)
            * self.parite_desavantageuse
        )

        coeff_rouge.append(1)
        coeff_vert.append(0)

        if est_superieur(coeff_rouge, coeff_vert):
            return rouge
        else:
            return vert

    def comparer_rouge_noir(self, rouge, noir):
        coeff_rouge, coeff_noir = [], []

        coeff_noir.append(int(self.plateau.possessionCoinDuQuartier(noir, self.cote)))
        coeff_rouge.append(1)

        coeff_noir.append(
            self.plateau.est_coup_bourbier_par_cote(noir, self.cote)
            * self.parite_desavantageuse
        )
        coeff_rouge.append(
            self.plateau.est_coup_bourbier_par_cote(rouge, self.cote)
            * self.parite_desavantageuse
        )

        coeff_rouge.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, rouge)
        )
        coeff_noir.append(
            self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, noir)
        )

        coeff_rouge.append(self.plateau.Nombre_pion_retourne(rouge, self.cote))
        coeff_noir.append(self.plateau.Nombre_pion_retourne(noir, self.cote))

        if est_superieur(coeff_rouge, coeff_noir):
            return rouge
        else:
            return noir

    def comparer_rouge_coin(self, rouge, coin):
        return coin

    def comparer_vert_noir(self, vert, noir):

        coeff_vert, coeff_noir = [], []

        coeff_noir.append(int(self.plateau.possessionCoinDuQuartier(noir, self.cote)))
        coeff_vert.append(1)

        coeff_noir.append(1)
        coeff_vert.append(0)

        if est_superieur(coeff_vert, coeff_noir):
            return vert
        else:
            return noir

    def comparer_vert_coin(self, vert, coin):
        return coin

    def comparer_noir_coin(self, noir, coin):
        return coin

    def comparer_2_positions(self, position1, position2):
        """Prend en parametre deux position de couleur quelconque et retourne la position la plus avantageuse"""
        dictionnaire_des_fct_comparaison = {
            ZONE_BLANCHE: {
                ZONE_COIN: (self.comparer_blanc_coin, True),
                ZONE_VERTE: (self.comparer_blanc_vert, True),
                ZONE_ROUGE: (self.comparer_blanc_rouge, True),
                ZONE_NOIRE: (self.comparer_blanc_noir, True),
                ZONE_BLANCHE: (self.comparer_blanc, True),
            },
            ZONE_ROUGE: {
                ZONE_COIN: (self.comparer_rouge_coin, True),
                ZONE_VERTE: (self.comparer_rouge_vert, True),
                ZONE_ROUGE: (self.comparer_rouge, True),
                ZONE_NOIRE: (self.comparer_rouge_noir, True),
                ZONE_BLANCHE: (self.comparer_blanc_rouge, False),
            },
            ZONE_VERTE: {
                ZONE_COIN: (self.comparer_vert_coin, True),
                ZONE_VERTE: (self.comparer_vert, True),
                ZONE_ROUGE: (self.comparer_rouge_vert, False),
                ZONE_NOIRE: (self.comparer_vert_noir, True),
                ZONE_BLANCHE: (self.comparer_blanc_vert, False),
            },
            ZONE_NOIRE: {
                ZONE_COIN: (self.comparer_noir_coin, True),
                ZONE_VERTE: (self.comparer_vert_noir, False),
                ZONE_ROUGE: (self.comparer_rouge_noir, False),
                ZONE_NOIRE: (self.comparer_noir, True),
                ZONE_BLANCHE: (self.comparer_blanc_noir, False),
            },
            ZONE_COIN: {
                ZONE_COIN: (self.comparer_coin, True),
                ZONE_VERTE: (self.comparer_vert_coin, False),
                ZONE_ROUGE: (self.comparer_rouge_coin, False),
                ZONE_NOIRE: (self.comparer_noir_coin, False),
                ZONE_BLANCHE: (self.comparer_blanc_coin, False),
            },
        }

        couleur_pos1 = self.plateau.obtenir_couleur_position(position1)
        couleur_pos2 = self.plateau.obtenir_couleur_position(position2)

        fonction_de_comparaison, position_dans_ordre = dictionnaire_des_fct_comparaison[
            couleur_pos1
        ][couleur_pos2]
        # fonction_de_comparaison est une variable contenant une fonction de comparaison.
        # Cette fonction permet de comparer les position1 et 2 en fonction de leur couleur
        # position_dans_ordre est un Booléen qui est False si les positions 1 et 2 doivent être inversés pour être dans
        # l'orde dans les paramètre de fonction comparaison
        if not (position_dans_ordre):
            position1, position2 = position2, position1

        # Ici on fait une pré-selection selon le critère rédhibitoire :
        # Ne pas donner l'opportunité à l'adversaire de prendre un coin
        if (
            self.plateau.Augmentation_coup_possible_adv_dans_zone(
                position1, ZONE_COIN, self.cote
            )
            <= 0
        ):
            if (
                self.plateau.Augmentation_coup_possible_adv_dans_zone(
                    position2, ZONE_COIN, self.cote
                )
                <= 0
            ):
                return fonction_de_comparaison(position1, position2)
            else:
                return position1
        else:
            if (
                self.plateau.Augmentation_coup_possible_adv_dans_zone(
                    position2, ZONE_COIN, self.cote
                )
                <= 0
            ):
                return position2
            else:
                return fonction_de_comparaison(position1, position2)

    def comparer_n_positions(self, *args):
        """Permet de faire la comparaison d'un nombre fini de positions"""
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return self.comparer_2_positions(args[0], args[1])
        return self.comparer_n_positions(
            self.comparer_2_positions(args[0], args[1]), *args[2:]
        )
