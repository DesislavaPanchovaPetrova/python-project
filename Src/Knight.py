#-------------------------------------------------------------------------------
# Name:        Knight
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Piece import Piece
from Constants import *


class Knight(Piece):

    def __init__(self, color, pType, pos):
        Piece.__init__(self, color, pType, pos)

    def is_empty(self):
        return False

    def GetPossibleMoves(self, board):
        possibleMoves = []

        for move in [-8, -12, -21, -19, 21, 19, 12, 8]:
            movePosition = (self.position + move).value
            movePiece = board[movePosition]
            if movePiece.type == PieceType.Empty \
                or Color.GetOpposite(self.color) == movePiece.color:
                    possibleMoves.append(movePosition)

        return possibleMoves


class WhiteKnight(Knight):

    def __init__(self, pos):
        Knight.__init__(self, Color.White, PieceType.wKnight, pos)


class BlackKnight(Knight):

    def __init__(self, pos):
        Knight.__init__(self, Color.Black, PieceType.bKnight, pos)
