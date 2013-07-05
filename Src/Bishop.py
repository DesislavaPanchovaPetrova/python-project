#-------------------------------------------------------------------------------
# Name:        Bishop
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


class Bishop(Piece):

    def __init__(self, color, pType, pos):
        Piece.__init__(self, color, pType, pos)

    def is_empty(self):
        return False

    def GetDiagonalMoves(self, board, step):
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

        for moveStep in [-11, -9, 9, 11]:
            possibleMoves.extend(self.GetDiagonalMoves(board, moveStep))

        return possibleMoves


class WhiteBishop(Bishop):

    def __init__(self, pos):
        Bishop.__init__(self, Color.White, PieceType.wBishop, pos)


class BlackBishop(Bishop):

    def __init__(self, pos):
        Bishop.__init__(self, Color.Black, PieceType.bBishop, pos)
