#J'essaie de faires des ias naives vite fait ...

import outils

class DefinivitementStable(Robot):
    """Robot qui essaie seulement de maximiser ses pions définitivement stables."""
    def __init__(self,*args,**kwargs):
        """Crée un robot."""
        super().__init__(*args,**kwargs)

    def jouer(self,plateau,panneau=None):
        """Joue en maximisant les pions définivitement stables."""
        stables=plateau.obtenirTousLesPionsDefinitivementStables()
        coups_possibles=plateau.obtenirMouvementsValides()
        intersection=outils.intersection(stables,coups_possibles)
        if intersections:
            choix=intersections[0]
            return choix
        else:
            self.jouerAleatoire()
