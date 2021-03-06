#-------------------------------------------------------------------------------
# Name:        EvalConsts
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class EvalConsts():

    wPawnTable = [0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 5, 10, 10,-25,-25, 10, 10,  5, 0,
                  0, 5, -5,-10,  0,  0,-10, -5,  5, 0,
                  0, 0,  0,  0, 25, 25,  0,  0,  0, 0,
                  0, 5,  5, 10, 27, 27, 10,  5,  5, 0,
                  0,10, 10, 20, 30, 30, 20, 10, 10, 0,
                  0,50, 50, 50, 50, 50, 50, 50, 50, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0]

    wKnightTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,-50,-40,-20,-30,-30,-20,-40,-50, 0,
                    0,-40,-20,  0,  5,  5,  0,-20,-40, 0,
                    0,-30,  5, 10, 15, 15, 10,  5,-30, 0,
                    0,-30,  0, 15, 20, 20, 15,  0,-30, 0,
                    0,-30,  5, 15, 20, 20, 15,  5,-30, 0,
                    0,-30,  0, 10, 15, 15, 10,  0,-30, 0,
                    0,-40,-20,  0,  0,  0,  0,-20,-40, 0,
                    0,-50,-40,-30,-30,-30,-30,-40,-50, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    wBishopTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,-10,  5,  0,  0,  0,  0,  5,-10, 0,
                    0,-10, 10, 10, 10, 10, 10, 10,-10, 0,
                    0,-10,  0, 10, 10, 10, 10,  0,-10, 0,
                    0,-10,  5,  5, 10, 10,  5,  5,-10, 0,
                    0,-10,  0,  5, 10, 10,  5,  0,-10, 0,
                    0, 10, 10, 20, 30, 30, 20, 10, 10, 0,
                    0,-10,  0,  0,  0,  0,  0,  0,-10, 0,
                    0,-20,-10,-10,-10,-10,-10,-10,-20, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    wRookTable = [0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  5,  5,  0,  0,  0, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0, 5, 10, 10, 10, 10, 10, 10,  5, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0]

    wQueenTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,-20,-10,-10, -5, -5,-10,-10,-20, 0,
                   0,-10,  0,  5,  0,  0,  0,  0,-10, 0,
                   0,-10,  5,  5,  5,  5,  5,  0,-10, 0,
                   0,  0,  0,  5,  5,  5,  5,  0, -5, 0,
                   0, -5,  0,  5,  5,  5,  5,  0, -5, 0,
                   0,-10,  0,  5,  5,  5,  5,  0,-10, 0,
                   0,-10,  0,  0,  0,  0,  0,  0,-10, 0,
                   0,-20,-10,-10, -5, -5,-10,-10,-20, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    wKingTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,20,  30, 10,  0,  0, 10, 30, 20, 0,
                  0, 20, 20,  0,  0,  0,  0, 20, 20, 0,
                  0,-10,-20,-20,-20,-20,-20,-20,-10, 0,
                  0,-20,-30,-30,-40,-40,-30,-30,-20, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    wKingTableEndGame = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,-50,-30,-30,-30,-30,-30,-30,-50, 0,
                         0,-50,-30,-30,-30,-30,-30,-30,-50, 0,
                         0,-30,-30,  0,  0,  0,  0,-30,-30, 0,
                         0,-30,-10, 20, 30, 30, 20,-10,-30, 0,
                         0,-30,-10, 30, 40, 40, 30,-10,-30, 0,
                         0,-30,-10, 20, 30, 30, 20,-10,-30, 0,
                         0,-30,-20,-10,  0,  0,-10,-20,-30, 0,
                         0,-50,-40,-30,-20,-20,-30,-40,-50, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

###############################################################################

    bPawnTable = [0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,50, 50, 50, 50, 50, 50, 50, 50, 0,
                  0,10, 10, 20, 30, 30, 20, 10, 10, 0,
                  0, 5,  5, 10, 27, 27, 10,  5,  5, 0,
                  0, 0,  0,  0, 25, 25,  0,  0,  0, 0,
                  0, 5, -5,-10,  0,  0,-10, -5,  5, 0,
                  0, 5, 10, 10,-25,-25, 10, 10,  5, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0]

    bKnightTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,-50,-40,-30,-30,-30,-30,-40,-50, 0,
                    0,-40,-20,  0,  0,  0,  0,-20,-40, 0,
                    0,-30,  0, 10, 15, 15, 10,  0,-30, 0,
                    0,-30,  5, 15, 20, 20, 15,  5,-30, 0,
                    0,-30,  5, 15, 20, 20, 15,  5,-30, 0,
                    0,-30,  5, 10, 15, 15, 10,  5,-30, 0,
                    0,-40,-20,  0,  5,  5,  0,-20,-40, 0,
                    0,-50,-40,-20,-30,-30,-20,-40,-50, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    bBishopTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,-20,-10,-10,-10,-10,-10,-10,-20, 0,
                    0,-10,  0,  0,  0,  0,  0,  0,-10, 0,
                    0, 10, 10, 20, 30, 30, 20, 10, 10, 0,
                    0,-10,  0,  5, 10, 10,  5,  0,-10, 0,
                    0,-10,  5,  5, 10, 10,  5,  5,-10, 0,
                    0,-10,  0, 10, 10, 10, 10,  0,-10, 0,
                    0,-10, 10, 10, 10, 10, 10, 10,-10, 0,
                    0,-10,  5,  0,  0,  0,  0,  5,-10, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                    0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    bRookTable = [0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 5, 10, 10, 10, 10, 10, 10,  5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0,-5,  0,  0,  0,  0,  0,  0, -5, 0,
                  0, 0,  0,  0,  5,  5,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0, 0,  0,  0,  0,  0,  0,  0,  0, 0]

    bQueenTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,-20,-10,-10, -5, -5,-10,-10,-20, 0,
                   0,-10,  0,  0,  0,  0,  0,  0,-10, 0,
                   0,-10,  0,  5,  5,  5,  5,  0,-10, 0,
                   0, -5,  0,  5,  5,  5,  5,  0, -5, 0,
                   0,  0,  0,  5,  5,  5,  5,  0, -5, 0,
                   0,-10,  5,  5,  5,  5,  5,  0,-10, 0,
                   0,-10,  0,  5,  0,  0,  0,  0,-10, 0,
                   0,-20,-10,-10, -5, -5,-10,-10,-20, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                   0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    bKingTable = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-30,-40,-40,-50,-50,-40,-40,-30, 0,
                  0,-20,-30,-30,-40,-40,-30,-30,-20, 0,
                  0,-10,-20,-20,-20,-20,-20,-20,-10, 0,
                  0, 20, 20,  0,  0,  0,  0, 20, 20, 0,
                  0,20,  30, 10,  0,  0, 10, 30, 20, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                  0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

    bKingTableEndGame = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,-50,-40,-30,-20,-20,-30,-40,-50, 0,
                         0,-30,-20,-10,  0,  0,-10,-20,-30, 0,
                         0,-30,-10, 20, 30, 30, 20,-10,-30, 0,
                         0,-30,-10, 20, 30, 30, 20,-10,-30, 0,
                         0,-30,-10, 20, 30, 30, 20,-10,-30, 0,
                         0,-30,-30,  0,  0,  0,  0,-30,-30, 0,
                         0,-50,-30,-30,-30,-30,-30,-30,-50, 0,
                         0,-50,-30,-30,-30,-30,-30,-30,-50, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0,
                         0,  0,  0,  0,  0,  0,  0,  0,  0, 0]

###############################################################################
##
##    bPawnTable = [0,  0,   0,   0,  0,  0,  0,  0,  0, 0,\
##                  0,  0,   0,   0,  0,  0,  0,  0,  0, 0,\
##                  0,  0,   0,   0,  0,  0,  0,  0,  0, 0,\
##                  0,-50, -50, -50,-50,-50,-50,-50,-50, 0,\
##                  0,-10, -10, -20,-30,-30,-20,-10,-10, 0,\
##                  0, -5,  -5, -10,-27,-27,-10, -5, -5, 0,\
##                  0,  0,   0,   0,-25,-25,  0,  0,  0, 0,\
##                  0, -5,   5,  10,  0,  0, 10,  5, -5, 0,\
##                  0, -5, -10, -10, 25, 25,-10,-10, -5, 0,\
##                  0,  0,   0,   0,  0,  0,  0,  0,  0, 0,\
##                  0,  0,   0,   0,  0,  0,  0,  0,  0, 0,\
##                  0,  0,   0,   0,  0,  0,  0,  0,  0, 0]
##
##    bKnightTable = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0, 50,40, 30, 30, 30, 30,40,50, 0,\
##                    0, 40,20,  0,  0,  0,  0,20,40, 0,\
##                    0, 30, 0,-10,-15,-15,-10, 0,30, 0,\
##                    0, 30,-5,-15,-20,-20,-15,-5,30, 0,\
##                    0, 30, 0,-15,-20,-20,-15, 0,30, 0,\
##                    0, 30,-5,-10,-15,-15,-10,-5,30, 0,\
##                    0, 40,20,  0, -5, -5,  0,20,40, 0,\
##                    0, 50,40, 20, 30, 30, 20,40,50, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##
##    bBishopTable = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0, 20, 10, 10, 10, 10, 10, 10, 20, 0,\
##                    0, 10,  0,  0,  0,  0,  0,  0, 10, 0,\
##                    0,-10,-10,-20,-30,-30,-20,-10,-10, 0,\
##                    0, 10,  0, -5,-10,-10, -5,  0, 10, 0,\
##                    0, 10, -5, -5,-10,-10, -5, -5, 10, 0,\
##                    0, 10,  0,-10,-10,-10,-10,  0, 10, 0,\
##                    0, 10,-10,-10,-10,-10,-10,-10, 10, 0,\
##                    0,-10,  5,  0,  0,  0,  0,  5,-10, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##
##    bRookTable = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0, 0,  0,  0,  0,  0,  0,  0, 0, 0,\
##                    0,-5,-10,-10,-10,-10,-10,-10,-5, 0,\
##                    0, 5,  0,  0,  0,  0,  0,  0, 5, 0,\
##                    0, 5,  0,  0,  0,  0,  0,  0, 5, 0,\
##                    0, 5,  0,  0,  0,  0,  0,  0, 5, 0,\
##                    0, 5,  0,  0,  0,  0,  0,  0, 5, 0,\
##                    0, 5,  0,  0,  0,  0,  0,  0, 5, 0,\
##                    0, 0,  0,  0, -5, -5,  0,  0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##
##    bQueenTable = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,20, 10,10, 5, 5,10, 10,20, 0,\
##                    0,10,  0, 0, 0, 0, 0,  0,10, 0,\
##                    0,10,  0,-5,-5,-5,-5,  0,10, 0,\
##                    0, 5,  0,-5,-5,-5,-5,  0, 5, 0,\
##                    0, 0,  0,-5,-5,-5,-5,  0, 5, 0,\
##                    0,10, -5,-5,-5,-5,-5,  0,10, 0,\
##                    0,10,  0,-5, 0, 0, 0,  0,10, 0,\
##                    0,20, 10,10, 5, 5,10, 10,20, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##
##    bKingTable = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0, 30, 40, 40,50,50, 40, 40, 30, 0,\
##                    0, 30, 40, 40,50,50, 40, 40, 30, 0,\
##                    0, 30, 40, 40,50,50, 40, 40, 30, 0,\
##                    0, 30, 40, 40,50,50, 40, 40, 30, 0,\
##                    0, 20, 30, 30,40,40, 30, 30, 20, 0,\
##                    0, 10, 20, 20,20,20, 20, 20, 10, 0,\
##                    0,-20,-20,  0, 0, 0,  0,-20,-20, 0,\
##                    0,-20,-30,-10, 0, 0,-10,-30,-20, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##
##    bKingTableEndGame = [0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,50,40, 30, 20, 20, 30,40,50, 0,\
##                    0,30,20, 10,  0,  0, 10,20,30, 0,\
##                    0,30,10,-20,-30,-30,-20,10,30, 0,\
##                    0,30,10,-30,-40,-40,-30,10,30, 0,\
##                    0,30,10,-30,-40,-40,-30,10,30, 0,\
##                    0,30,10,-20,-30,-30,-20,10,30, 0,\
##                    0,30,30,  0,  0,  0,  0,30,30, 0,\
##                    0,50,30, 30, 30, 30, 30,30,50, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0,\
##                    0,  0, 0,  0,  0,  0,  0, 0, 0, 0]
##############################################################

    wPawnEval = 100
    wKnightEval = 320
    wBishopEval = 330
    wRookEval = 500
    wQueenEval = 900
    wKingEval = 20000

##    bPawnEval = -100
##    bKnightEval = -320
##    bBishopEval = -330
##    bRookEval = -500
##    bQueenEval = -900
##    bKingEval = -20000

    MobilityShare = 7

    DEPTH = 2  # 3
    MIN_INT = -10**10
    MAX_INT = 10*10


def main():
    # print all matrixes
    print(BoardEval.bPawnTable)
    print(BoardEval.bKingTableEndGame)
    print(BoardEval.bBishopTable)
    print(BoardEval.bKingTable)
    print(BoardEval.bKnightTable)
    print(BoardEval.bQueenTable)
    print(BoardEval.bRookTable)

    print(BoardEval.wPawnTable)
    print(BoardEval.wKingTableEndGame)
    print(BoardEval.wBishopTable)
    print(BoardEval.wKingTable)
    print(BoardEval.wKnightTable)
    print(BoardEval.wQueenTable)
    print(BoardEval.wRookTable)

if __name__ == '__main__':
    main()
