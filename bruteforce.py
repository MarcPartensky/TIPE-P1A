# coding: utf-8

from myminimax import Minimax
#from joueur import Joueur
from joueur import Robot

from copy import deepcopy
from random import choice

import config as cfg

class BruteForce(Robot): #Permet d'évaluer d'autres intelligences artificielles en fixant une échelle de niveau
    def __init__(self,nom="Brute Force",level=1):
        super().__init__(nom)
        self.level=level
        self.advantage=[[ 9,-2, 1, 1, 1, 1,-2, 9],
                        [-2,-2,-1,-1,-1,-1,-2,-2],
                        [ 1,-1, 0, 0, 0, 0,-1, 1],
                        [ 1,-1, 0, 0, 0, 0,-1, 1],
                        [ 1,-1, 0, 0, 0, 0,-1, 1],
                        [ 1,-1, 0, 0, 0, 0,-1, 1],
                        [-2,-2,-1,-1,-1,-1,-2,-2],
                        [ 9,-2, 1, 1, 1, 1,-2, 9]]

    def jouer(self,board,window):
        #board.presenterPionsStables(window) #Pas encore au point
        self.board=board
        board.mouvements=self.board.obtenirMouvementsValides(self.cote)
        tree=self.treePlay(board.grille,self.cote)
        cfg.debug("[BruteForce]: arbre des possibilitees",tree)
        if self.container(tree):
            minimax=Minimax(tree,start=0)
            result=minimax()
        else:
            result=None
        if result:
            return board.mouvements[result]
        else:
            return choice(board.mouvements)


    def treePlay(self,grid,cote,level=0):
        if level>self.level:
            return self.reward(grid,cote)
        else:
            tree=[]
            self.board.grille=grid
            moves=self.board.obtenirMouvementsValides(cote)
            for move in moves:
                sub_grid=deepcopy(grid)
                x,y=move
                self.board.grille=sub_grid
                self.board.placerPion(move,cote)
                tree.append(self.treePlay(self.board.grille,(cote+1)%2,level+1))
            return tree

    def reward(self,grid,cote):
        result=self.evaluate(grid,cote)
        return result

    def evaluate(self,grid,cote):
        return sum([sum([(int(grid[y][x]==self.cote)-int(grid[y][x]!=self.cote and grid[y][x]>=0))*self.advantage[y][x] for x in range(len(self.advantage[y]))]) for y in range(len(self.advantage))])

    def container(self,tree):
        if type(tree)!=list:
            return True
        else:
            found=False
            for element in tree:
                if self.container(element):
                    found=True
                    break
            return found
