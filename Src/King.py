#-------------------------------------------------------------------------------
# Name:        King
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


class King(Piece):

    def __init__(self, color, pType, pos):
        Piece.__init__(self, color, pType, pos)

    def is_empty(self):
        return False

    def GetPossibleMoves(self, board):
        possibleMoves = []

        for move in [-10, -1, -11, -1, 1, 10, 9, 11]:
            movePosition = (self.position + move).value
            movePiece = board[movePosition]
            if movePiece.type == PieceType.Empty \
                or Color.GetOpposite(self.color) == movePiece.color:
                    possibleMoves.append(movePosition)

        return possibleMoves


class WhiteKing(King):

    def __init__(self, pos):
        King.__init__(self, Color.White, PieceType.wKing, pos)


class BlackKing(King):

    def __init__(self, pos):
        King.__init__(self, Color.Black, PieceType.bKing, pos)
