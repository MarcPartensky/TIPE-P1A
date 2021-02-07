class Menu:
    """Représentation du menu du jeu de l'Othello."""

    def __init__(self, dictionnaire):
        """Crée un menu du jeu."""
        p = Page("Principal", dictionnaire)

    def __call__(self, fenetre):
        """Boucle."""
        while fenetre.ouverte and self.ouvert:
            self.afficher(fenetre)
            self.actualiser(fenetre)
            self.choisir()

    def afficher(self, fenetre):
        """Affiche la page correspondante."""
        self.page.afficher(fenetre)

    def actualiser(self):
        """Actualise la page."""
        self.page.actualiser(fenetre)

    def choisir(self):
        """Choisi la page correspondante."""
        self.page.choisir()
        self.choix = self.page.choix

    def obtenirPage(self):
        """Renvoi la page correspondante."""
        return self.pages[self.cle]

    def choisirPage(self, page):
        """Choisi la page correspondante."""
        self.cle = self.pages.index(page)

    page = property(obtenirPage, choisirPage)


class Page:
    """Représentation d'une page du menu."""

    def __init__(self, nom, dictionnaire, taille=[1200, 1000], couleur=couleurs.BLEU):
        """Crée une page de menu."""
        dictionnaire
        self.bouttons = bouttons
        self.couleur = couleur
        self.chargerSurface(taille)
        self.afficherFond()

    def chargerSurface(taille, couleur):
        """Charge la surface de la page."""
        self.surface = pygame.Surface(taille)

    def afficher(self, fenetre):
        """Affiche la page avec la fenetre."""
        positions = self.obtenirPositionsBoutonsCentrer()
        for position in positions:
            self.afficherBoutton(position)

    def afficherBoutton(self, position):
        """Affiche le boutton."""

    def obtenirPositionsBoutonsCentrer(self):
        """Renvoie la position de tous les boutons de la page
        relativement au nombre de pion."""
        l = len(self.bouttons)
        tx, ty = self.taille
        return positions

    def actualiser(self, fenetre):
        """Actualise l'état de la page."""
        for boutton in self.bouttons:
            self.boutton.actualiser(fenetre)

    def recharger(self):
        """Recharge les bouttons."""
        for boutton in self.bouttons:
            boutton.recharger()

    def obtenirTaille(self):
        """Renvoie la taille de la page."""
        return self.surface.get_size()

    def choisirTaille(self, taille):
        """Choisi la taille de la fenetre en transformant la taille de la surface."""
        pygame.transform(self.surface, taille)

    def obtenirBoutons(self):
        """Renvoie la liste des bouttons."""
        return [a[0] for a in self.actions]

    def choisirBoutons(self, bouttons):
        """Choisi la liste des bouttons."""
        self.actions = [(b, a[1]) for (a, b) in zip(self.actions, self.bouttons)]

    def obtenirCommandes(self):
        """Renvoie la liste des commandes."""
        return [a[1] for a in self.actions]

    def choisirCommandes(self, commandes):
        """Choisi la liste des commandes."""
        self.actions == [(a[0], c) for (a, c) in zip(self.actions, self.commandes)]

    taille = property(obtenirTaille, choisirTaille)
    bouttons = property(obtenirBoutons, choisirBoutons)
    commandes = property(obtenirCommandes, choisirCommandes)


class Boutton:
    """Représentation du bouton d'une page."""

    def __init__(self, nom, taille=[20, 20], couleur=couleurs.VERT, police="monospace"):
        """Crée un bouton d'une page."""
        self.nom = nom
        self.clique = False
        self.couleur = couleur
        self.police = police
        self.chargerSurface(taille)

    def chargerSurface(self, taille):
        """Charge la surface du boutton."""
        self.surface = pygame.Surface(taille)

    def afficherFond(self, couleur=None):
        """Affiche le fond du boutton."""
        if not couleur:
            couleur = self.couleur
        self.surface.fill(couleur)

    def afficherNom(self, couleur=couleurs.NOIR, taille=5):
        """Affiche le nom."""
        pass

    def afficher(self):
        """Affiche le fond et le nom du boutton."""
        font = pygame.font.SysFont(self.police, self.taille)
        self.surface = font.render(texte, 1, couleur)

    def recharger(self):
        """Recharge le boutton en mettant clique à Faux."""
        self.clique = False

    def obtenirTaille(self):
        """Renvoie la taille de la page."""
        return self.surface.get_size()

    def choisirTaille(self, taille):
        """Choisi la taille de la fenetre en transformant la taille de la surface."""
        pygame.transform(self.surface, taille)

    taille = property(obtenirTaille, choisirTaille)


bouttons1 = [Boutton("Jouer"), Boutton("Options"), Boutton("Quitter")]
commandes1 = [11, 21, 31, 41]
actions = [()]
# page=Page(bouttons1,actions1)
