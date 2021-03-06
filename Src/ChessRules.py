#-------------------------------------------------------------------------------
# Name:        ChessRules
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Piece import PieceEmpty
from Position import Position
from King import King
from Constants import *
from collections import defaultdict
from copy import deepcopy
from itertools import chain


class ChessRules:
    POS_MAP = {21: "A1", 22: "A2", 23: "A3", 24: "A4", 25: "A5", 26: "A6", 27: "A7", 28: "A8",
               31: "B1", 32: "B2", 33: "B3", 34: "B4", 35: "B5", 36: "B6", 37: "B7", 38: "B8",
               41: "C1", 42: "C2", 43: "C3", 44: "C4", 45: "C5", 46: "C6", 47: "C7", 48: "C8",
               51: "D1", 52: "D2", 53: "D3", 54: "D4", 55: "D5", 56: "D6", 57: "D7", 58: "D8",
               61: "E1", 62: "E2", 63: "E3", 64: "E4", 65: "E5", 66: "E6", 67: "E7", 68: "E8",
               71: "F1", 72: "F2", 73: "F3", 74: "F4", 75: "F5", 76: "F6", 77: "F7", 78: "F8",
               81: "G1", 82: "G2", 83: "G3", 84: "G4", 85: "G5", 86: "G6", 87: "G7", 88: "G8",
               91: "H1", 92: "H2", 93: "H3", 94: "H4", 95: "H5", 96: "H6", 97: "H7", 98: "H8"}

    @staticmethod
    def IsCheckmate(chessBoard, myPieces):
        my_valid_moves = ChessRules.GetAllValidMovesList(chessBoard, myPieces)
        return len(my_valid_moves) == 0

    @staticmethod
    def GetAllValidMovesList(chessBoard, pieces):
        validMovesDict = ChessRules.GetAllValidMovesDict(chessBoard, pieces)
        result = list(chain.from_iterable(validMovesDict.values()))
        return result

    @staticmethod
    def GetAllValidMovesDict(chessBoard, pieces):
        validMoves = dict()
        for piece in pieces:
            validMoves[piece] = ChessRules.GetValidMovesList(chessBoard, piece)
        return validMoves

    @staticmethod
    def GetValidMovesList(chessBoard, piece):
        moves = []
        possibleMoves = piece.GetPossibleMoves(chessBoard.board)
        for move in possibleMoves:
            to_piece = chessBoard.board[move]
            if not ChessRules.DoesMovePutPlayerInCheck(chessBoard, piece, to_piece):
                moves.append(move)
            if ChessRules.DoesMoveRemoveThreatPiece(chessBoard.board, piece.color, to_piece):
                moves.append(move)
        return moves

    @staticmethod
    def DoesMoveRemoveThreatPiece(board, my_color, toPiece):
        kingPos = 0
        for pos in POS_MAP.keys():
            piece = board[pos]
            if isinstance(piece, King) and piece.color == my_color:
                kingPos = pos

        moves = toPiece.GetPossibleMoves(board)
        if kingPos in moves:
            return True

    @staticmethod
    def DoesMovePutPlayerInCheck(chessBoard, piece, toPiece):
        piecePos = piece.position.value
        toPos = toPiece.position.value
        copied_board = deepcopy(chessBoard.board)
        copied_board[toPos] = deepcopy(piece)
        copied_board[toPos].position = Position(toPos)
        copied_board[piecePos] = PieceEmpty(piecePos)
        return ChessRules.IsPlayerInCheck(copied_board, piece.color)

    @staticmethod
    def IsPlayerInCheck(board, color):
        """ Returns True in case King of player with color
            is in Check.
        """
        kingPos = 0
        for pos in POS_MAP.keys():
            piece = board[pos]
            if isinstance(piece, King) and piece.color == color:
                kingPos = piece.position.value

        if kingPos != 0:
            for pos in POS_MAP.keys():
                enemyPiece = board[pos]
                if enemyPiece.color == Color.GetOpposite(color):
                    if kingPos in enemyPiece.GetPossibleMoves(board):
                        return True
        return False
