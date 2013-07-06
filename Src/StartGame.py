#-------------------------------------------------------------------------------
# Name:        StartGame
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Player import *
from itertools import cycle
from GUIBoard import *
from Constants import Color
import ctypes


class StartGame():

    def __init__(self):
        self.wPlayer = HumanPlayer("Human chess player", Color.White)
        self.bPlayer = PlayerAI("AI player", Color.Black)
        self.players = cycle([self.wPlayer, self.bPlayer])
        self.guiBoard = GUIBoard()

    def ChangePlayer(self):
        return next(self.players)

    def MainLoop(self):
        while not self.guiBoard.GameOver():
            self.guiBoard.Redraw()
            playerOnMove = self.ChangePlayer()  # toggle palyers

            if playerOnMove.IsAI():
                fromPos, toPos = playerOnMove.GetMove(self.guiBoard.chessBoard)
            elif playerOnMove.IsHuman():
                fromPos, toPos = self.guiBoard.GetPlayerInput()

            self.guiBoard.MakeMove(fromPos, toPos)

        winer = playerOnMove
        ctypes.windll.user32.MessageBoxW(
            0, "Winner is " + winer.name, "Game is over.", 0)

        # exit game
        pygame.quit()
        sys.exit(0)


game = StartGame()
game.MainLoop()
