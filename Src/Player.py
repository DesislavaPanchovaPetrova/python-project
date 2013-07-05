#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from BoardEval import *


class Player():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def IsAI(self):
        return False

    def IsHuman(self):
        return False


class HumanPlayer(Player):

    def __init__(self, name, color):
        Player.__init__(self, name, color)

    def IsHuman(self):
        return True

    def IsAI(self):
        return False


class PlayerAI(Player):

    def __init__(self, name, color):
        Player.__init__(self, name, color)

    def IsHuman(self):
        return False

    def IsAI(self):
        return True

    def GetMove(self, chessBoard):
        return BoardEval.GetMove(chessBoard)
