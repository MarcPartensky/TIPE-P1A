from outils import intersection, est_superieur
from plateau_analysable import PlateauAnalysable
import outils, joueur, random
import config as cfg
from copy import deepcopy

#La liste des différentes zone de jeu :
ZONE_COIN=4#Ne doit pas etre une liste
ZONE_BORD=3
ZONE_BLANCHE=2
ZONE_ROUGE=1
ZONE_NOIR=0
ZONE_TOUT=-1


class IA(joueur.Robot):
    """Classe d'IA NON-naïve"""

    def __init__(self,nom=None):
        "Lance l'__init__ de la classe joueur.Robot"
        super().__init__(nom)

    def reinitialiser(self, plateau):
        """Cette fonction est lancée au debut de chaque tour
        Ici on definit des variables qui ne vont pas etre modifiées pendant tout le tour afin d'economiser du temps..."""
        self.plateau=plateau#il ne faut pas faire de simulations sur ce plateau !
        self.mouvements_possibles=plateau.obtenirMouvementsValides(self.cote)
        self.parite_desavantageuse = not(plateau.test_parite_avantageuse())

    def comparer_blanc(self, pos1, pos2):
        """ On produit ci dessous est en fait une astuce :
            Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
            de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
            des coups proposes.
            Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
            il n'influe donc pas dans  la selection du coup"""
        coeff1,coeff2=[],[]

        coeff1.append(self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)*self.parite_desavantageuse)
        coeff2.append(self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)*self.parite_desavantageuse)

        coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_TOUT, self.cote_oppose))
        coeff2.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_TOUT, self.cote_oppose))

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        outils.ajouter_coeff_alea(coeff1, coeff2)
        if est_superieur(coeff1, coeff2) :
            return pos1
        else :
            return pos2


    def comparer_rouge(self, pos1, pos2):
        """ On produit ci dessous est en fait une astuce :
            Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
            de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
            des coups proposes.
            Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
            il n'influe donc pas dans  la selection du coup """
        coeff1,coeff2=[],[]

        coeff1.append(self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)*self.parite_desavantageuse)
        coeff2.append(self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)*self.parite_desavantageuse)

        coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_BORD, self.cote_oppose))
        coeff2.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_BORD, self.cote_oppose))

        coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_TOUT, self.cote_oppose))
        coeff2.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_TOUT, self.cote_oppose))

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))
        outils.ajouter_coeff_alea(coeff1, coeff2)
        if est_superieur(coeff1, coeff2) :
            return pos1
        else :
            return pos2

    def comparer_vert(self, pos1, pos2):
        """ On produit ci dessous est en fait une astuce :
            Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
            de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
            des coups proposes.
            Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
            il n'influe donc pas dans  la selection du coup"""
        coeff1,coeff2=[],[]

        coeff1.append(self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)*self.parite_desavantageuse)
        coeff2.append(self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)*self.parite_desavantageuse)

        #coeff1.append(self.Augmentation_pion_stable_dans_zone(self.plateau, self.cote, ZONE_BORD, pos1))
        #coeff2.append(self.Augmentation_pion_stable_dans_zone(self.plateau, self.cote, ZONE_BORD, pos2))

        #coeff1.append(self.Augmentation_pion_stable_dans_zone(self.plateau, self.cote, ZONE_TOUT, pos1))
        #coeff2.append(self.Augmentation_pion_stable_dans_zone(self.plateau, self.cote, ZONE_TOUT, pos2))

        coeff1.append(int(self.plateau.position_stable_pour_cote(pos1, self.cote)))
        coeff2.append(int(self.plateau.position_stable_pour_cote(pos2, self.cote)))

        coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_BORD, self.cote))
        coeff2.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_BORD, self.cote))

        coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_TOUT, self.cote))
        coeff2.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_TOUT, self.cote))

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        outils.ajouter_coeff_alea(coeff1, coeff2)
        if est_superieur(coeff1, coeff2) :
            return pos1
        else :
            return pos2


    def comparer_noir(self, pos1, pos2):
        """ On produit ci dessous est en fait une astuce :
            Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
            de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
            des coups proposes.
            Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
            il n'influe donc pas dans  la selection du coup"""
        coeff1,coeff2=[],[]

        coeff1.append(self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)*self.parite_desavantageuse)
        coeff2.append(self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)*self.parite_desavantageuse)

        #coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos1, ZONE_COIN, self.cote))
        #coeff1.append(-1*self.plateau.Augmentation_coup_possible_adv_dans_zone(pos2, ZONE_COIN, self.cote))

        coeff1.append(int(self.plateau.position_stable_pour_cote(pos1, self.cote)))
        coeff2.append(int(self.plateau.position_stable_pour_cote(pos2, self.cote)))

        #todo faire cas Case noir sur l'extrême bord, juste à côté d’un coin conquis
        coeff1.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos1))
        coeff2.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos2))

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1, self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2, self.cote))

        outils.ajouter_coeff_alea(coeff1, coeff2)
        if est_superieur(coeff1, coeff2) :#todo utiliser le mot cle or en python
            return pos1
        else :
            return pos2

    def comparer_coin(self, pos1, pos2):
        """ On produit ci dessous est en fait une astuce :
            Si self.parite_desavantageuse est True, la parite est desavantgeuse, il faut essayer de faire passer le tour
            de l'adversaire, pour cela, on cherche un "coup bourbier", il faut donc en prendre compte dans la selection
            des coups proposes.
            Sinon, alors self.parite_desavantageuse est False et le porduit est dans les deux cas egal à 0
            il n'influe donc pas dans  la selection du coup"""
        coeff1,coeff2=[],[]

        coeff1.append(self.plateau.est_coup_bourbier_par_cote(pos1, self.cote)*self.parite_desavantageuse)
        coeff2.append(self.plateau.est_coup_bourbier_par_cote(pos2, self.cote)*self.parite_desavantageuse)

        coeff1.append(self.plateau.Nombre_coin_adjacent_pris(self.cote, pos1))
        coeff2.append(self.plateau.Nombre_coin_adjacent_pris(self.cote, pos2))

        coeff1.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos1))
        coeff2.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, pos2))

        coeff1.append(self.plateau.Nombre_pion_retourne(pos1,self.cote))
        coeff2.append(self.plateau.Nombre_pion_retourne(pos2,self.cote))

        outils.ajouter_coeff_alea(coeff1, coeff2)
        if est_superieur(coeff1, coeff2) :
            return pos1
        else :
            return pos2

    def comparer_blanc_rouge(self, blanc, rouge):

        cfg.debug("on a bourre comapre blacn et rouge","<[vient de ia.py de la fonction comparer_blanc_rouge, alexandre explique cet ligne, elle veut rien dire]>")
        cfs
        return blanc
        coeff_blanc, coeff_rouge = [], []


        coeff_blanc.append(self.plateau.est_coup_bourbier_par_cote(blanc, self.cote) * self.parite_desavantageuse)
        coeff_rouge.append(self.plateau.est_coup_bourbier_par_cote(rouge, self.cote) * self.parite_desavantageuse)

        coeff_rouge.append(int(self.plateau.Augmentation_coup_possible_adv_dans_zone(rouge, ZONE_BORD)<=0))
        coeff_blanc.append(1)

        coeff_rouge.append(int(self.plateau.Nombre_pion_retourne(rouge)>=self.plateau.Nombre_pion_retourne(blanc)))
        coeff_blanc.append(1)



        coeff_rouge.append(1)
        coeff_blanc.append(0)

        #outils.ajouter_coeff_alea(coeff_blanc, coeff_rouge)

        if est_superieur(coeff_blanc, coeff_rouge):
            return blanc
        else:
            return rouge



    def comparer_blanc_vert(self, blanc, vert):#todo faire un debug affichable

        coeff_blanc, coeff_vert = [], []

        coeff_blanc.append(self.plateau.est_coup_bourbier_par_cote(blanc, self.cote) * self.parite_desavantageuse)
        coeff_vert.append(self.plateau.est_coup_bourbier_par_cote(vert, self.cote) * self.parite_desavantageuse)


        coeff_blanc.append(int(not(self.plateau.position_stable_pour_cote(vert, self.cote))))
        coeff_vert.append(1)


        coeff_blanc.append(1)#on prend le blanc en prioro
        coeff_vert.append(0)

        if est_superieur(coeff_blanc, coeff_vert):
            return blanc
        else:
            return vert


    def comparer_blanc_noir(self, blanc, noir):#todo faire un debug affichable
        cfg.debug("on a bourre comparer blanc rouge","<[vient de ia.py de la fonction comparer_blanc_noir, alexandre explique cet ligne, elle veut rien dire]>")
        return blanc
        coeff_blanc, coeff_noir = [], []

        coeff_blanc.append(1)
        coeff_noir.append(int(self.plateau.Augmentation_coup_possible_adv_dans_zone(noir, ZONE_COIN)<=0))

        coeff_blanc.append(self.plateau.est_coup_bourbier_par_cote(blanc, self.cote) * self.parite_desavantageuse)
        coeff_noir.append(self.plateau.est_coup_bourbier_par_cote(noir, self.cote) * self.parite_desavantageuse)

        coeff_blanc.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, blanc))
        coeff_noir.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, noir))

        coeff_blanc.append(self.plateau.Nombre_pion_retourne(blanc))
        coeff_noir.append(self.plateau.Nombre_pion_retourne(noir))

        outils.ajouter_coeff_alea(coeff_blanc, coeff_noir)

        if est_superieur(coeff_blanc, coeff_noir):
            return blanc
        else:
            return noir


    def comparer_blanc_coin(self, blanc, coin):
        return coin


    def comparer_rouge_vert(self, rouge, vert):#todo revoir ca + debug affichage

        coeff_rouge, coeff_vert=[],[]

        coeff_rouge.append(int(not(self.plateau.position_stable_pour_cote(vert, self.cote))))
        coeff_vert.append(1)

        coeff_rouge.append(self.plateau.est_coup_bourbier_par_cote(rouge, self.cote)*self.parite_desavantageuse)
        coeff_vert.append(self.plateau.est_coup_bourbier_par_cote(vert, self.cote)*self.parite_desavantageuse)

        coeff_rouge.append(1)
        coeff_vert.append(0)

        outils.ajouter_coeff_alea(coeff_vert, coeff_rouge)
        if est_superieur(coeff_rouge, coeff_vert) :
            return rouge
        else :
            return vert




    def comparer_rouge_noir(self, rouge, noir):#todo revoir ca + debug affichage

        coeff_rouge, coeff_noir = [], []

        #coeff_noir.append(int(self.Augmentation_coup_possible_adv_dans_zone(self.plateau, noir, ZONE_COIN)<=0))
        #coeff_rouge.append(1)

        coeff_noir.append(int(self.plateau.possessionCoinDuQuartier(noir, self.cote)))
        coeff_rouge.append(1)

        coeff_noir.append(self.plateau.est_coup_bourbier_par_cote(noir, self.cote)*self.parite_desavantageuse)
        coeff_rouge.append(self.plateau.est_coup_bourbier_par_cote(rouge, self.cote)*self.parite_desavantageuse)

        coeff_rouge.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, rouge))
        coeff_noir.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_TOUT, noir))

        coeff_rouge.append(self.plateau.Nombre_pion_retourne(rouge, self.cote))
        coeff_noir.append(self.plateau.Nombre_pion_retourne(noir, self.cote))

        outils.ajouter_coeff_alea(coeff_rouge, coeff_noir)
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
        cfg.debug("on a bourre vert noir","<[vient de ia.py de la fonction comparer_vert_noir, alexandre explique cet ligne, elle veut rien dire]>")

        coeff_noir.append(1)
        coeff_vert.append(0)
        coeff_noir.append(int(self.plateau.Augmentation_coup_possible_adv_dans_zone(noir, ZONE_COIN, self.cote)<=0))
        coeff_vert.append(1)

        coeff_noir.append(self.plateau.est_coup_bourbier_par_cote(noir, self.cote)*self.parite_desavantageuse)
        coeff_vert.append(self.plateau.est_coup_bourbier_par_cote(vert, self.cote)*self.parite_desavantageuse)


        coeff_vert.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_BORD, vert))
        coeff_noir.append(self.plateau.Augmentation_pion_stable_dans_zone(self.cote, ZONE_BORD, noir))

        coeff_vert.append(self.plateau.Augmentation_pion_dans_zone(self.cote, ZONE_BORD, vert))
        coeff_noir.append(self.plateau.Augmentation_pion_dans_zone(self.cote, ZONE_BORD, noir))

        coeff_vert.append(self.plateau.Nombre_pion_retourne(vert, self.cote))
        coeff_noir.append(self.plateau.Nombre_pion_retourne(noir, self.cote))

        outils.ajouter_coeff_alea(coeff_vert, coeff_noir)
        if est_superieur(coeff_vert, coeff_noir):
            return vert
        else:
            return noir


    def comparer_vert_coin(self, vert, coin):
        return coin


    def comparer_noir_coin(self, noir, coin):
        return coin

    def comparer(self, position1, position2):
        liste_degueulasse = { ZONE_BLANCHE  : { ZONE_BLANCHE : self.comparer_blanc,
                                                ZONE_ROUGE   : self.comparer_blanc_rouge,
                                                ZONE_BORD    : self.comparer_blanc_vert,
                                                ZONE_NOIR    : self.comparer_blanc_noir,
                                                ZONE_COIN    : self.comparer_blanc_coin },

                              ZONE_ROUGE    : {   ZONE_ROUGE : self.comparer_rouge,
                                                ZONE_BORD  : self.comparer_rouge_vert,
                                                ZONE_NOIR  : self.comparer_rouge_noir,
                                                ZONE_COIN  : self.comparer_rouge_coin },

                              ZONE_BORD     : {   ZONE_BORD : self.comparer_vert,
                                                ZONE_COIN : self.comparer_vert_coin,
                                                ZONE_NOIR : self.comparer_vert_noir },

                              ZONE_NOIR     : {   ZONE_NOIR : self.comparer_noir,
                                                ZONE_COIN : self.comparer_noir_coin },

                              ZONE_COIN     : {   ZONE_COIN : self.comparer_coin }
                            }

        try : # On essaye ce code, si une erreur python est levé on sort du try et on continuer le programme
            fonction_compa = liste_degueulasse[self.plateau.obtenir_couleur_position(position1)][self.plateau.obtenir_couleur_position(position2)]
            arg = (position1, position2)
        except KeyError : # si l'erreur levée précédemment est une KeyError (c'est à dire que on demande un élément du dictionnaire qui n'existe pas) on éxécute ce code ci dessous
            fonction_compa = liste_degueulasse[self.plateau.obtenir_couleur_position(position2)][self.plateau.obtenir_couleur_position(position1)]
            arg = (position2, position1)

        if self.plateau.Augmentation_coup_possible_adv_dans_zone(arg[0], ZONE_COIN, self.cote) <= 0:
            if self.plateau.Augmentation_coup_possible_adv_dans_zone(arg[1], ZONE_COIN, self.cote) <= 0:
                return fonction_compa(arg[0], arg[1])
            else :
                return arg[0]
        else :
            if self.plateau.Augmentation_coup_possible_adv_dans_zone(arg[1], ZONE_COIN, self.cote) <= 0:
                return arg[1]
            else :
                return fonction_compa(arg[0], arg[1])


    def compa_diago(self, fct2,*args):
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return fct2(args[0], args[1])
        #cfg.debug("le args", args)
        return self.compa_diago(fct2,fct2(args[0], args[1]), *args[2:])

    def main(self, plateau, fenetre=None):
        """On surcharge la méthode main de robot (c'est à dire qu'on redéfinie la méthode main lorsque l'on se trouve cette cette sous-classe)
        Fonction principal qui est appeler par la class robot lorsque l'othello demande au joueur de jouer"""
        self.fenetre=fenetre
        self.reinitialiser(plateau)  # Il faut prednre en compte le nouveau plateau
        cfg.debug("les coup possible :", repr(self.mouvements_possibles))
        return self.compa_diago(self.comparer, *self.mouvements_possibles)
        #if coups_bourbier!=[] :
        #    cfg.debug("##Coup Bourbier !")
        #    return self.compa_diago(self.comparer, *coups_bourbier)
        #else :
        #    return self.compa_diago(self.comparer, *self.mouvements_possibles)

    def debug_case(self, positions,couleur,message=None,clear=True,pause=True):
        if self.fenetre!=None :
            self.plateau.presenter(positions,couleur,self.fenetre,message=message,clear=clear,pause=pause)
