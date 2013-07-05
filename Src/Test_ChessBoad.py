#-------------------------------------------------------------------------------
# Name:        Test_ChessBoad
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import unittest
from ChessBoard import *
from Piece import *
from Rook import *
from Queen import *
from King import *
from Bishop import *
from Knight import *

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.chessBoard = ChessBoard()

    def tearDown(self):
        pass

    def test_board_paramethers(self):
        try:
            self.assertEqual(len(self.chessBoard.board), 120)

            self.assertEqual(self.chessBoard.board[0].type, PieceType.Illegal)
            self.assertEqual(self.chessBoard.board[21].type, PieceType.wRook)

            self.assertEqual(self.chessBoard.playerColor, Color.White)
            self.assertEqual(len(self.chessBoard.wPieces), 16)
            self.assertEqual(len(self.chessBoard.bPieces), 16)
        except Exception as exc:
            print("Initial board paramethers : " + exc.__str__())
        finally:
            print("test_board_paramethers is over")

    def test_make_move(self):
        try:
            self.chessBoard.MakeMove(31, 41)

            self.assertTrue(isinstance(self.chessBoard.board[41], WhitePawn))
            self.assertTrue(isinstance(self.chessBoard.board[31], PieceEmpty))

            self.assertEqual(self.chessBoard.playerColor, Color.Black)
        except Exception as exc:
            print("Make chess move : " + exc.__str__())
        finally:
            print("test_make_move is over")

    def test_make_move_fail(self):
        try:
            self.assertRaises(ValueError, self.chessBoard.MakeMove, 21, 31) # illegal move
        except Exception as exc:
            print("Make chess move with exception : " + exc.__str__())
        finally:
            print("test_make_move_fail is over")

    def test_get_valid_moves(self):
        try:
            self.chessBoard.MakeMove(31, 41)

            validMoves = self.chessBoard.GetValidMoves(81)
            self.assertEqual(len(validMoves), 2)
            self.assertEqual(validMoves, [71, 61])

        except Exception as exc:
            print("Get valid moves failed : " + exc.__str__())
        finally:
            print("test_get_valid_moves is over")

    def test_game_over(self):
        try:
            self.chessBoard.board = \
                [PieceIllegal(0),
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
                      PieceEmpty(21),
                      PieceEmpty(22),
                      PieceEmpty(23),
                      PieceEmpty(24),
                      WhiteKing(25),
                      PieceEmpty(26),
                      PieceEmpty(27),
                      PieceEmpty(28),
                      PieceIllegal(29),
                      PieceIllegal(30),
                      PieceEmpty(31),
                      PieceEmpty(32),
                      PieceEmpty(33),
                      PieceEmpty(34),
                      PieceEmpty(35),
                      PieceEmpty(36),
                      BlackQueen(37),
                      PieceEmpty(38),
                      PieceIllegal(39),
                      PieceIllegal(40),
                      PieceEmpty(41),
                      PieceEmpty(42),
                      PieceEmpty(43),
                      BlackRook(44),
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
                      PieceEmpty(81),
                      PieceEmpty(82),
                      PieceEmpty(83),
                      PieceEmpty(84),
                      PieceEmpty(85),
                      PieceEmpty(86),
                      PieceEmpty(87),
                      PieceEmpty(88),
                      PieceIllegal(89),
                      PieceIllegal(90),
                      PieceEmpty(91),
                      PieceEmpty(92),
                      PieceEmpty(93),
                      PieceEmpty(94),
                      BlackKing(95),
                      PieceEmpty(96),
                      PieceEmpty(97),
                      PieceEmpty(98),
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

            self.chessBoard.wPiecesPos = [25]
            self.chessBoard.wPieces = \
                [self.chessBoard.board[pos] for pos in self.chessBoard.wPiecesPos]
            self.chessBoard.bPiecesPos = [44, 95, 37]
            self.chessBoard.bPieces = \
                [self.chessBoard.board[pos] for pos in self.chessBoard.bPiecesPos]
            self.chessBoard.playerColor = Color.White;

            self.assertTrue(self.chessBoard.GameOver())
        except Exception as exc:
            print("Test game over method : " + exc.__str__())
        finally:
            print("test_game_over is over")

    def test_game_over_false(self):
        try:
            self.chessBoard.board = \
                [PieceIllegal(0),
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
                      PieceEmpty(21),
                      PieceEmpty(22),
                      PieceEmpty(23),
                      PieceEmpty(24),
                      WhiteKing(25),
                      PieceEmpty(26),
                      PieceEmpty(27),
                      PieceEmpty(28),
                      PieceIllegal(29),
                      PieceIllegal(30),
                      PieceEmpty(31),
                      PieceEmpty(32),
                      PieceEmpty(33),
                      PieceEmpty(34),
                      PieceEmpty(35),
                      PieceEmpty(36),
                      BlackQueen(37),
                      PieceEmpty(38),
                      PieceIllegal(39),
                      PieceIllegal(40),
                      PieceEmpty(41),
                      BlackRook(42),
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
                      PieceEmpty(81),
                      PieceEmpty(82),
                      PieceEmpty(83),
                      PieceEmpty(84),
                      PieceEmpty(85),
                      PieceEmpty(86),
                      PieceEmpty(87),
                      PieceEmpty(88),
                      PieceIllegal(89),
                      PieceIllegal(90),
                      PieceEmpty(91),
                      PieceEmpty(92),
                      PieceEmpty(93),
                      PieceEmpty(94),
                      BlackKing(95),
                      PieceEmpty(96),
                      PieceEmpty(97),
                      PieceEmpty(98),
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

            self.chessBoard.wPiecesPos = [25]
            self.chessBoard.wPieces = \
                [self.chessBoard.board[pos] for pos in self.chessBoard.wPiecesPos]
            self.chessBoard.bPiecesPos = [42, 95, 37]
            self.chessBoard.bPieces = \
                [self.chessBoard.board[pos] for pos in self.chessBoard.bPiecesPos]
            self.chessBoard.playerColor = Color.White;

            self.assertFalse(self.chessBoard.GameOver())
        except Exception as exc:
            print("In not game over fails : " + exc.__str__())
        finally:
            print("test_game_over_false is over")


if __name__ == '__main__':
    unittest.main()

