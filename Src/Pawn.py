#-------------------------------------------------------------------------------
# Name:        Pawn
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
from ImagesData import Images

class Pawn(Piece):

    def __init__(self, color, pType, pos):
        Piece.__init__(self, color, pType, pos)

    def is_empty(self):
        return False

    def IsOpponentPiece(self, piece):
        return self.color == Color.GetOpposite(piece.color)


class WhitePawn(Pawn):

    def __init__(self, pos):
        self.imagePath = Images.wPawn
        Pawn.__init__(self, Color.White, PieceType.wPawn, pos)

    def move_forward1(self):
        return self.position + 10

    def move_forward2(self):
        if self.position.rank == Rank.Two:
            return self.position + 20

    def move_left_diag(self):
        return self.position + 9

    def move_right_diag(self):
        return self.position + 11

    def GetPossibleMoves(self, board):
        possibleMoves = []

        # one field forward
        oneForwardPos = self.move_forward1().value
        oneForwardPiece = board[oneForwardPos]
        if oneForwardPiece.type == PieceType.Empty:
            possibleMoves.append(oneForwardPos)
            # two fields foward (one piece forward should be empty)
            twoForwardPos = self.move_forward2()
            if twoForwardPos:
                twoForwardPiece = board[twoForwardPos.value]
                if twoForwardPiece.type == PieceType.Empty:
                    possibleMoves.append(twoForwardPos.value)
        # left capture move
        leftMovePos = self.move_left_diag().value
        leftMovePiece = board[leftMovePos]
        if leftMovePiece.color == Color.Black:
            possibleMoves.append(leftMovePos)
        # right capture move
        rightMovePos = self.move_right_diag().value
        rightMovePiece = board[rightMovePos]
        if rightMovePiece.color == Color.Black:
            possibleMoves.append(rightMovePos)

        return possibleMoves


class BlackPawn(Pawn):

    def __init__(self, pos):
        self.imagePath = Images.bPawn
        Pawn.__init__(self, Color.Black, PieceType.bPawn, pos)

    def move_forward1(self):
        return self.position - 10

    def move_forward2(self):
        if self.position.rank == Rank.Seven:
            return self.position - 20

    def move_left_diag(self):
        return self.position - 9

    def move_right_diag(self):
        return self.position - 11

    def GetPossibleMoves(self, board):
        possibleMoves = []

        # one field forward
        oneForwardPos = self.move_forward1().value
        oneForwardPiece = board[oneForwardPos]
        if oneForwardPiece.type == PieceType.Empty:
            possibleMoves.append(oneForwardPos)
            # two fields foward (one piece forward should be empty)
            twoForwardPos = self.move_forward2()
            if twoForwardPos:
                twoForwardPiece = board[twoForwardPos.value]
                if twoForwardPiece.type == PieceType.Empty:
                    possibleMoves.append(twoForwardPos.value)
        # left capture move
        leftMovePos = self.move_left_diag().value
        leftMovePiece = board[leftMovePos]
        if leftMovePiece.color == Color.White:
            possibleMoves.append(leftMovePos)
        # right capture move
        rightMovePos = self.move_right_diag().value
        rightMovePiece = board[rightMovePos]
        if rightMovePiece.color == Color.White:
            possibleMoves.append(rightMovePos)

        return possibleMoves
