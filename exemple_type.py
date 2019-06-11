# --coding:utf-8--
from othello import Othello
from panneau import Panneau
from joueur  import Humain



_ = -1
n =  0

maximisation = [
[ _, 1, 1, 1, 1, 1, 1, _],
[ 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, n, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1],
[ _, 1, 1, 1, 1, 1, 1, _]]

DefinivitementStable = [
[ 0, 0, 0, 0, 0, 0, 0, _],
[ 0, 0, 0, 0, _, _, _, _],
[ 0, 0, _, _, _, _, _, _],
[ 0, 0, _, _, _, _, _, _],
[ 0, _, _, _, _, _, _, 0],
[ _, _, _, _, _, _, 0, 0],
[ _, _, _, _, _, 0, 0, 0],
[ _, _, _, _, 0, 0, 0, 0]]

mobilite_1 = [
[ _, 1, 1, 1, 1, 1, 1, _],
[ _, _, 1, 1, 1, 1, _, _],
[ 1, 1, n, 1, 1, n, 1, _],
[ 1, 1, n, 1, 1, 1, 1, _],
[ 1, 1, n, n, n, 1, _, _],
[ _, 1, 1, 1, n, 1, _, _],
[ _, _, 1, n, 1, 1, _, _],
[ _, _, 1, 1, _, 1, _, _]]

mobilite_2 = [
[ _, _, 1, _, _, 1, _, _],
[ _, _, 1, 1, 1, 1, _, _],
[ 1, 1, n, n, n, 1, _, _],
[ 1, n, n, n, 1, 1, _, _],
[ 1, 1, 1, n, 1, _, _, _],
[ 1, 1, 1, n, 1, _, _, _],
[ _, _, n, n, n, 1, _, _],
[ _, n, n, n, n, n, n, _]]

parite = [
[ _, _, 1, 1, 1, 1, 1, _],
[ 1, 1, 1, n, n, 1, _, 1],
[ 1, n, 1, n, n, 1, 1, 1],
[ 1, n, n, 1, n, n, n, 1],
[ 1, 1, n, 1, 1, n, n, 1],
[ 1, 1, n, n, n, 1, 1, 1],
[ 1, _, n, n, n, 1, _, 1],
[ _, 1, 1, 1, 1, 1, 1, _]]

if __name__=="__main__":
    panneau = Panneau(nom="Othello",
                      taille=[1200,800],
                      set=False,
                      plein_ecran=False)

    joueur_noir  = Humain("Toto")
    joueur_blanc = Humain("Caroline")

    jeu = Othello(joueurs=[joueur_noir, joueur_blanc],panneau=panneau)
    jeu.plateau.grille=maximisation
    jeu.lancer()

    jeu.recreer()
    jeu.plateau.grille=DefinivitementStable
    jeu.lancer()

    jeu.recreer()
    jeu.plateau.grille=mobilite_1
    jeu.lancer()

    jeu.recreer()
    jeu.plateau.grille=mobilite_2
    jeu.lancer()

    jeu.recreer()
    jeu.plateau.grille=parite
    jeu.lancer()
