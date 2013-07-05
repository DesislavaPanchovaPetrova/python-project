#-------------------------------------------------------------------------------
# Name:        Test_BoardEval
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from BoardEval import *
from ChessBoard import *

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.chessBoard = ChessBoard()

    def tearDown(self):
        pass

    def test_GetBoardEvaluation(self):
        try:
            evaluation = BoardEval.GetBoardEvaluation(self.chessBoard.board,\
                 self.chessBoard.GetPlayerPieces(), self.chessBoard.GetOpponentPieces(),\
                 self.chessBoard.playerColor)

            self.assertEqual(evaluation,0)

        except Exception as exc:
            print("Board evaluation fails : " + exc.__str__())
        finally:
            print("test_GetBoardEvaluation is over")

    def test_GetBoardEvaluation_started_game(self):
        try:
            self.chessBoard.MakeMove(31, 41)
            self.chessBoard.MakeMove(81, 71)
            self.chessBoard.MakeMove(35, 55)
            blackMove = BoardEval.GetMove(self.chessBoard)

            self.assertEqual(blackMove, (85, 65))
        except Exception as exc:
            print("Get chess move fails : " + exc.__str__())
        finally:
            print("test_GetMove is over")

    def test_GetMove(self):
        try:
            self.chessBoard.MakeMove(31, 41)
            self.chessBoard.MakeMove(81, 71)
            self.chessBoard.MakeMove(35, 55)
            blackMove = BoardEval.GetMove(self.chessBoard)

            self.assertEqual(blackMove, (85, 65))
        except Exception as exc:
            print("Get chess move fails : " + exc.__str__())
        finally:
            print("test_GetMove is over")

if __name__ == '__main__':
    #unittest.main()
    import doctest
    doctest.testmod()
