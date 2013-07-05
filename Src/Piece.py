#-------------------------------------------------------------------------------
# Name:        Piece
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Position import *
from Constants import *


class Piece():

    def __init__(self, color=Color.Empty, pType=PieceType.Illegal, pos=0):
        self.color = color
        self.type = pType
        self.position = Position(pos)

    def is_empty(self):
        return True

    def GetPossibleMoves(self, board):
        return []


class PieceEmpty(Piece):

    def __init__(self, pos):
        Piece.__init__(self, Color.Empty, PieceType.Empty, pos)

    def GetPossibleMoves(self, board):
        return []


class PieceIllegal(Piece):

    def __init__(self, pos):
        Piece.__init__(self, Color.Empty, PieceType.Illegal, pos)

    def GetPossibleMoves(self, board):
        return []
