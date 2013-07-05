#-------------------------------------------------------------------------------
# Name:        Queen
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


class Queen(Piece):

    def __init__(self, color, pType, pos):
        Piece.__init__(self, color, pType, pos)

    def is_empty(self):
        return False

    def GetLineMoves(self, board, step):
        possibleMoves = []

        stepPosition = self.position.value + step
        stepPiece = board[stepPosition]
        while stepPiece.type == PieceType.Empty:
            possibleMoves.append(stepPosition)
            stepPosition = stepPosition + step
            stepPiece = board[stepPosition]

        if stepPiece.color == Color.GetOpposite(self.color):
            possibleMoves.append(stepPosition)

        return possibleMoves

    def GetPossibleMoves(self, board):
        possibleMoves = []

        for moveStep in [-10, -1, 1, 10, -11, -9, 9, 11]:
            possibleMoves.extend(self.GetLineMoves(board, moveStep))
        return possibleMoves


class WhiteQueen(Queen):

    def __init__(self, pos):
        Queen.__init__(self, Color.White, PieceType.wQueen, pos)


class BlackQueen(Queen):

    def __init__(self, pos):
        Queen.__init__(self, Color.Black, PieceType.bQueen, pos)