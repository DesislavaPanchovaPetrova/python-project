#-------------------------------------------------------------------------------
# Name:        Board evaluation
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from ChessBoard import *
from ChessRules import *
from EvalConsts import *
from copy import deepcopy
from Player import *
from Piece import *


class BoardEval():

    @staticmethod
    def GetMove(chessBoard):
        ((fromPos, toPos), boardEval) = BoardEval.NegaMaxAlphaBeta(
            chessBoard,
            EvalConsts.DEPTH,
            EvalConsts.MIN_INT,
            EvalConsts.MAX_INT)
        return (fromPos, toPos)

    @staticmethod
    def NegaMaxAlphaBeta(chessBoard, level, alpha, beta):
        best_move = (-1, -1)   # illegal from and to tuple

        if (level == 1 or
        ChessRules.IsCheckmate(
            chessBoard.board,
            chessBoard.GetPlayerPieces()) or
        ChessRules.IsCheckmate(
            chessBoard.board,
            chessBoard.GetOpponentPieces())):
                return (best_move, BoardEval.GetBoardEvaluation(
                        chessBoard.board,
                        chessBoard.GetPlayerPieces(),
                        chessBoard.GetOpponentPieces(),
                        chessBoard.playerColor))

        for (piece, moves_list) in ChessRules.GetAllValidMovesDict(
                chessBoard.board, chessBoard.GetPlayerPieces()).items():
            for move in moves_list:
                next_board = BoardEval.MovePiece(chessBoard, piece, move)
                (_, score) = BoardEval.NegaMaxAlphaBeta(
                    next_board, level-1, -1*beta, -1*alpha)
                nega_score = -1*score
                if nega_score > alpha:  # better alpha found
                    alpha = nega_score
                    best_move = (piece.position.value, move)
                ### alpha-beta cut-off
                if alpha >= beta:
                    break
        return (best_move, alpha)

    @staticmethod
    def MovePiece(chessBoard, piece, movePos):
        fromPos = piece.position.value
        copy_board = deepcopy(chessBoard)
        copy_board.MakeMove(fromPos, movePos)
        return copy_board

    @staticmethod
    def GetBoardEvaluation(board, my_pieces, opponent_pices, my_color):
        sign = -1 if my_color == Color.White else 1
        boardEvaluation = 0

        for pos in POS_MAP.keys():
            piece = board[pos]
            if piece.type == PieceType.wPawn:
                boardEvaluation -= EvalConsts.wPawnEval
                boardEvaluation -= EvalConsts.wPawnTable[pos]
            if piece.type == PieceType.wKnight:
                boardEvaluation -= EvalConsts.wKnightEval
                boardEvaluation -= EvalConsts.wKnightTable[pos]
            if piece.type == PieceType.wBishop:
                boardEvaluation -= EvalConsts.wBishopEval
                boardEvaluation -= EvalConsts.wBishopTable[pos]
            if piece.type == PieceType.wRook:
                boardEvaluation -= EvalConsts.wRookEval
                boardEvaluation -= EvalConsts.wRookTable[pos]
            if piece.type == PieceType.wQueen:
                boardEvaluation -= EvalConsts.wQueenEval
                boardEvaluation -= EvalConsts.wQueenTable[pos]
            if piece.type == PieceType.wKing:
                boardEvaluation -= EvalConsts.wKingEval
                boardEvaluation -= EvalConsts.wKingTable[pos]
            if piece.type == PieceType.bPawn:
                boardEvaluation += EvalConsts.wPawnEval
                boardEvaluation += EvalConsts.bPawnTable[pos]
            if piece.type == PieceType.bKnight:
                boardEvaluation += EvalConsts.wKnightEval
                boardEvaluation += EvalConsts.bKnightTable[pos]
            if piece.type == PieceType.bBishop:
                boardEvaluation += EvalConsts.wBishopEval
                boardEvaluation += EvalConsts.bBishopTable[pos]
            if piece.type == PieceType.bRook:
                boardEvaluation += EvalConsts.wRookEval
                boardEvaluation += EvalConsts.bRookTable[pos]
            if piece.type == PieceType.bQueen:
                boardEvaluation += EvalConsts.wQueenEval
                boardEvaluation += EvalConsts.bQueenTable[pos]
            if piece.type == PieceType.bKing:
                boardEvaluation += EvalConsts.wKingEval
                boardEvaluation += EvalConsts.bKingTable[pos]

        countOfValidMovesForWhite = len(
            ChessRules.GetAllValidMovesList(board, opponent_pices))
        countOfValidMovesForBlack = len(
            ChessRules.GetAllValidMovesList(board, my_pieces))
        boardEvaluation = boardEvaluation + EvalConsts.MobilityShare * \
            (countOfValidMovesForBlack - countOfValidMovesForWhite)
        return boardEvaluation


def main():
    pass

if __name__ == '__main__':
    main()
