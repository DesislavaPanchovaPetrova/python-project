#-------------------------------------------------------------------------------
# Name:        ChessBoard
# Purpose:     Represent board state
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Pawn import *
from Knight import *
from Bishop import *
from Rook import *
from Queen import *
from King import *
from Piece import *
from Constants import *
from ChessRules import *
from itertools import cycle


class ChessBoard():
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8]
    FILES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    INT_TO_FILE = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

    POS_MAP = {21: "A1", 22: "A2", 23: "A3", 24: "A4", 25: "A5", 26: "A6", 27: "A7", 28: "A8",
               31: "B1", 32: "B2", 33: "B3", 34: "B4", 35: "B5", 36: "B6", 37: "B7", 38: "B8",
               41: "C1", 42: "C2", 43: "C3", 44: "C4", 45: "C5", 46: "C6", 47: "C7", 48: "C8",
               51: "D1", 52: "D2", 53: "D3", 54: "D4", 55: "D5", 56: "D6", 57: "D7", 58: "D8",
               61: "E1", 62: "E2", 63: "E3", 64: "E4", 65: "E5", 66: "E6", 67: "E7", 68: "E8",
               71: "F1", 72: "F2", 73: "F3", 74: "F4", 75: "F5", 76: "F6", 77: "F7", 78: "F8",
               81: "G1", 82: "G2", 83: "G3", 84: "G4", 85: "G5", 86: "G6", 87: "G7", 88: "G8",
               91: "H1", 92: "H2", 93: "H3", 94: "H4", 95: "H5", 96: "H6", 97: "H7", 98: "H8"}

    SQUARE_MAP = {"A1": 21, "A2": 22, "A3": 23, "A4": 24, "A5": 25, "A6": 26, "A7": 27, "A8": 28,
                  "B1": 31, "B2": 32, "B3": 33, "B4": 34, "B5": 35, "B6": 36, "B7": 37, "B8": 38,
                  "C1": 41, "C2": 42, "C3": 43, "C4": 44, "C5": 45, "C6": 46, "C7": 47, "C8": 48,
                  "D1": 51, "D2": 52, "D3": 53, "D4": 54, "D5": 55, "D6": 56, "D7": 57, "D8": 58,
                  "E1": 61, "E2": 62, "E3": 63, "E4": 64, "E5": 65, "E6": 66, "E7": 67, "E8": 68,
                  "F1": 71, "F2": 72, "F3": 73, "F4": 74, "F5": 75, "F6": 76, "F7": 77, "F8": 78,
                  "G1": 81, "G2": 82, "G3": 83, "G4": 84, "G5": 85, "G6": 86, "G7": 87, "G8": 88,
                  "H1": 91, "H2": 92, "H3": 93, "H4": 94, "H5": 95, "H6": 96, "H7": 97, "H8": 98}

    def __init__(self):
        self.board = [PieceIllegal(0),
                      PieceIllegal(1),
                      PieceIllegal(2),
                      PieceIllegal(3),
                      PieceIllegal(4),
                      PieceIllegal(5),
                      PieceIllegal(6),
                      PieceIllegal(7),
                      PieceIllegal(8),
                      PieceIllegal(9),
                      PieceIllegal(10),
                      PieceIllegal(11),
                      PieceIllegal(12),
                      PieceIllegal(13),
                      PieceIllegal(14),
                      PieceIllegal(15),
                      PieceIllegal(16),
                      PieceIllegal(17),
                      PieceIllegal(18),
                      PieceIllegal(19),
                      PieceIllegal(20),
                      WhiteRook(21),
                      WhiteKnight(22),
                      WhiteBishop(23),
                      WhiteQueen(24),
                      WhiteKing(25),
                      WhiteBishop(26),
                      WhiteKnight(27),
                      WhiteRook(28),
                      PieceIllegal(29),
                      PieceIllegal(30),
                      WhitePawn(31),
                      WhitePawn(32),
                      WhitePawn(33),
                      WhitePawn(34),
                      WhitePawn(35),
                      WhitePawn(36),
                      WhitePawn(37),
                      WhitePawn(38),
                      PieceIllegal(39),
                      PieceIllegal(40),
                      PieceEmpty(41),
                      PieceEmpty(42),
                      PieceEmpty(43),
                      PieceEmpty(44),
                      PieceEmpty(45),
                      PieceEmpty(46),
                      PieceEmpty(47),
                      PieceEmpty(48),
                      PieceIllegal(49),
                      PieceIllegal(50),
                      PieceEmpty(51),
                      PieceEmpty(52),
                      PieceEmpty(53),
                      PieceEmpty(54),
                      PieceEmpty(55),
                      PieceEmpty(56),
                      PieceEmpty(57),
                      PieceEmpty(58),
                      PieceIllegal(59),
                      PieceIllegal(60),
                      PieceEmpty(61),
                      PieceEmpty(62),
                      PieceEmpty(63),
                      PieceEmpty(64),
                      PieceEmpty(65),
                      PieceEmpty(66),
                      PieceEmpty(67),
                      PieceEmpty(68),
                      PieceIllegal(69),
                      PieceIllegal(70),
                      PieceEmpty(71),
                      PieceEmpty(72),
                      PieceEmpty(73),
                      PieceEmpty(74),
                      PieceEmpty(75),
                      PieceEmpty(76),
                      PieceEmpty(77),
                      PieceEmpty(78),
                      PieceIllegal(79),
                      PieceIllegal(80),
                      BlackPawn(81),
                      BlackPawn(82),
                      BlackPawn(83),
                      BlackPawn(84),
                      BlackPawn(85),
                      BlackPawn(86),
                      BlackPawn(87),
                      BlackPawn(88),
                      PieceIllegal(89),
                      PieceIllegal(90),
                      BlackRook(91),
                      BlackKnight(92),
                      BlackBishop(93),
                      BlackQueen(94),
                      BlackKing(95),
                      BlackBishop(96),
                      BlackKnight(97),
                      BlackRook(98),
                      PieceIllegal(99),
                      PieceIllegal(100),
                      PieceIllegal(101),
                      PieceIllegal(102),
                      PieceIllegal(103),
                      PieceIllegal(104),
                      PieceIllegal(105),
                      PieceIllegal(106),
                      PieceIllegal(107),
                      PieceIllegal(108),
                      PieceIllegal(109),
                      PieceIllegal(110),
                      PieceIllegal(111),
                      PieceIllegal(112),
                      PieceIllegal(113),
                      PieceIllegal(114),
                      PieceIllegal(115),
                      PieceIllegal(116),
                      PieceIllegal(117),
                      PieceIllegal(118),
                      PieceIllegal(119)]

        self.wPiecesPos = [21, 22, 23, 24, 25, 26, 27, 28,
                           31, 32, 33, 34, 35, 36, 37, 38]
        self.wPieces = [self.board[pos] for pos in self.wPiecesPos]

        self.bPiecesPos = [81, 82, 83, 84, 85, 86, 87, 88,
                           91, 92, 93, 94, 95, 96, 97, 98]
        self.bPieces = [self.board[pos] for pos in self.bPiecesPos]

        self.temporary_moves = []
        self.playerColors = cycle([Color.White, Color.Black])
        self.playerColor = self.SwitchPlayer()

    def GetPlayerPieces(self):
        if self.playerColor == Color.White:
            return self.wPieces
        elif self.playerColor == Color.Black:
            return self.bPieces

    def GetOpponentPieces(self):
        if self.playerColor == Color.White:
            return self.bPieces
        elif self.playerColor == Color.Black:
            return self.wPieces

    def RemoveOpponentPiece(self, pos):
        removed_piece = self.board[pos]
        if self.playerColor == Color.White:
            self.bPieces.remove(self.board[pos])
            self.bPiecesPos.remove(pos)
        elif self.playerColor == Color.Black:
            self.wPieces.remove(self.board[pos])
            self.wPiecesPos.remove(pos)

        self.board[pos] = PieceEmpty(pos)
        return removed_piece

    def RemoveMyPiece(self, pos):
        removed_piece = self.board[pos]
        if self.playerColor == Color.White:
            self.wPieces.remove(self.board[pos])
            self.wPiecesPos.remove(pos)
        elif self.playerColor == Color.Black:
            self.bPieces.remove(self.board[pos])
            self.bPiecesPos.remove(pos)

        self.board[pos] = PieceEmpty(pos)
        return removed_piece

    def RemovePiece(self, pos):
        removed_piece = self.board[pos]
        if removed_piece.color == Color.White:
            self.wPieces.remove(self.board[pos])
            self.wPiecesPos.remove(pos)
        elif removed_piece.color == Color.Black:
            self.bPieces.remove(self.board[pos])
            self.bPiecesPos.remove(pos)

        self.board[pos] = PieceEmpty(pos)
        return removed_piece

    def AddMyPieceToList(self, pos):
        if self.playerColor == Color.White:
            self.wPiecesPos.append(pos)
            self.wPieces.append(self.board[pos])
        elif self.playerColor == Color.Black:
            self.bPiecesPos.append(pos)
            self.bPieces.append(self.board[pos])

    def MoveMyPiece(self, fromPos, toPos):
        my_piece = self.RemoveMyPiece(fromPos)
        self.board[toPos] = my_piece  # move piece
        self.board[toPos].position = Position(toPos)  # correct position
        self.AddMyPieceToList(toPos)

    def MakeMove(self, myPiecePos, toPos):
        capture_piece = self.board[toPos]
        if capture_piece.type not in [PieceType.Empty, PieceType.Illegal]:
            self.RemoveOpponentPiece(toPos)
        self.MoveMyPiece(myPiecePos, toPos)

        self.playerColor = self.SwitchPlayer()

##    def MovePiece(self, fromPos, toPos):
##        fromPiece = self.board[fromPos]
##        if fromPiece.color == Color.White:
##            self.wPieces.remove(fromPiece)
##            self.wPiecesPos.remove(fromPos)
##            fromPiece.position = Position(toPos)
##            self.wPieces.append(fromPiece)
##            self.wPiecesPos.append(toPos)
##        elif fromPiece.color == Color.Black:
##            self.bPieces.remove(fromPiece)
##            self.bPiecesPos.remove(fromPos)
##            fromPiece.position = Position(toPos)
##            self.bPieces.append(fromPiece)
##            self.bPiecesPos.append(toPos)
##
##    def MakeTemopraryMove(self, myPiecePos, toPos):
##        remove_piece = self.RemovePiece(toPos)
##        self.MovePiece(myPiecePos, toPos)
##
##        self.temporary_moves.append(((myPiecePos, toPos), remove_piece))
##
##        self.playerColor = self.SwitchPlayer()
##
##    def UndoTemporaryMove(self):
##        if any(self.temporary_moves):
##            self.playerColor = self.SwitchPlayer()  # go back to previuos player
##            (myPiecePos, toPos), remove_piece  = self.temporary_moves.pop()
##            self.MoveMyPiece(toPos, myPiecePos)
##            self.board[toPos] = remove_piece

    def SwitchPlayer(self):
        return next(self.playerColors)

    def GetValidMoves(self, fromPos):
        return ChessRules.GetValidMovesList(self, self.board[fromPos])

    def GameOver(self):
        if self.playerColor == Color.White:
            return ChessRules.IsCheckmate(self, self.wPieces)
        else:
            return ChessRules.IsCheckmate(self, self.bPieces)
