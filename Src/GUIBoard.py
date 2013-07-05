#-------------------------------------------------------------------------------
# Name:        GUIBoard
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
import os
import sys
from itertools import cycle
from ImagesData import *
from ChessBoard import *
from Constants import *
from Position import *


class GUIBoard:

    BorderSize = 50
    SquareDim = 50
    SquareDimTuple = (50, 50)
    DisplaySize = (500, 500)
    FILES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8]
    ANITIALIAS = 1
    White = (255, 255, 255)
    Black = (0, 0, 0)
    LightSlateGrey = (119, 136, 153)
    CSSGold = (204, 153, 0)
    Yellow = (255, 255, 0)
    FontSize = 30

    def __init__(self):
        self.chessBoard = ChessBoard()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('Chess game with AI')
        self.screen = pygame.display.set_mode(self.DisplaySize)
        self.screen.fill(self.CSSGold)
        pygame.display.update()
        self.LoadImages()
        self.fontDefault = pygame.font.Font(None, self.FontSize)

    def LoadImages(self):
        self.black_pawn = pygame.image.load(Images.bPawn).convert()
        self.black_pawn = pygame.transform.scale(
            self.black_pawn, self.SquareDimTuple)
        self.black_rook = pygame.image.load(Images.bRook).convert()
        self.black_rook = pygame.transform.scale(
            self.black_rook, self.SquareDimTuple)
        self.black_knight = pygame.image.load(Images.bKnight).convert()
        self.black_knight = pygame.transform.scale(
            self.black_knight, self.SquareDimTuple)
        self.black_bishop = pygame.image.load(Images.bBishop).convert()
        self.black_bishop = pygame.transform.scale(
            self.black_bishop, self.SquareDimTuple)
        self.black_king = pygame.image.load(Images.bKing).convert()
        self.black_king = pygame.transform.scale(
            self.black_king, self.SquareDimTuple)
        self.black_queen = pygame.image.load(Images.bQueen).convert()
        self.black_queen = pygame.transform.scale(
            self.black_queen, self.SquareDimTuple)

        self.white_pawn = pygame.image.load(Images.wPawn).convert()
        self.white_pawn = pygame.transform.scale(
            self.white_pawn, self.SquareDimTuple)
        self.white_rook = pygame.image.load(Images.wRook).convert()
        self.white_rook = pygame.transform.scale(
            self.white_rook, self.SquareDimTuple)
        self.white_knight = pygame.image.load(Images.wKnight).convert()
        self.white_knight = pygame.transform.scale(
            self.white_knight, self.SquareDimTuple)
        self.white_bishop = pygame.image.load(Images.wBishop).convert()
        self.white_bishop = pygame.transform.scale(
            self.white_bishop, self.SquareDimTuple)
        self.white_king = pygame.image.load(Images.wKing).convert()
        self.white_king = pygame.transform.scale(
            self.white_king, self.SquareDimTuple)
        self.white_queen = pygame.image.load(Images.wQueen).convert()
        self.white_queen = pygame.transform.scale(
            self.white_queen, self.SquareDimTuple)

    def DrawBlankBoard(self):
        for pos in self.chessBoard.POS_MAP.keys():
            position = self.chessBoard.board[pos].position
            square = pygame.Surface(self.SquareDimTuple)
            if position.IsBlackSquare():
                square.fill(self.LightSlateGrey)
            else:
                square.fill(self.White)
            self.screen.blit(square, position.ScreenXY())

    def DrawRanks(self):
        screenX = Position.FILE_TO_SCREEN_X[1] - self.SquareDim/2
        for r in self.RANKS:
            screenY = Position.RANK_TO_SCREEN_Y[r] + self.SquareDim/4
            renderedLine = self.fontDefault.render(
                str(r), self.ANITIALIAS, self.Black)
            self.screen.blit(renderedLine, (screenX, screenY))

    def DrawFiles(self):
        screenY = Position.RANK_TO_SCREEN_Y[1] + 5*self.SquareDim/4
        for f in range(1, 9):
            screenX = Position.FILE_TO_SCREEN_X[f] + self.SquareDim/3
            renderedLine = self.fontDefault.render(
                INT_TO_FILE[f], self.ANITIALIAS, self.Black)
            self.screen.blit(renderedLine, (screenX, screenY))

    def DrawPossibleMoves(self, moves=[]):
        border = 3
        for pos in moves:
            rank, file = Position.POS_TO_RANK_FILE[pos]
            screenX = Position.FILE_TO_SCREEN_X[file]
            screenY = Position.RANK_TO_SCREEN_Y[rank]
            pygame.draw.rect(self.screen, self.Yellow,
                    (screenX, screenY, self.SquareDim, self.SquareDim), border)

    def DrawPieces(self):
        for piece in self.chessBoard.board:
            position = piece.position.ScreenXY()
            if piece.type == PieceType.bPawn:
                self.screen.blit(self.black_pawn, position)
            if piece.type == PieceType.bRook:
                self.screen.blit(self.black_rook, position)
            if piece.type == PieceType.bKnight:
                self.screen.blit(self.black_knight, position)
            if piece.type == PieceType.bBishop:
                self.screen.blit(self.black_bishop, position)
            if piece.type == PieceType.bQueen:
                self.screen.blit(self.black_queen, position)
            if piece.type == PieceType.bKing:
                self.screen.blit(self.black_king, position)
            if piece.type == PieceType.wPawn:
                self.screen.blit(self.white_pawn, position)
            if piece.type == PieceType.wRook:
                self.screen.blit(self.white_rook, position)
            if piece.type == PieceType.wKnight:
                self.screen.blit(self.white_knight, position)
            if piece.type == PieceType.wBishop:
                self.screen.blit(self.white_bishop, position)
            if piece.type == PieceType.wQueen:
                self.screen.blit(self.white_queen, position)
            if piece.type == PieceType.wKing:
                self.screen.blit(self.white_king, position)

    def Redraw(self, moves=[]):
        self.screen.fill(self.CSSGold)
        self.DrawBlankBoard()
        self.DrawRanks()
        self.DrawFiles()
        self.DrawPossibleMoves(moves)
        self.DrawPieces()
        pygame.display.flip()

    def GetPlayerInput(self):
        fromPos = None
        toPos = None
        possibleMoves = []
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.ExitGame()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if not fromPos:
                        if self.IsPlayersPiece(mouseX, mouseY):
                            fromPos = Position.GetChessPosition(mouseX, mouseY)
                            possibleMoves = self.GetValidMoves(fromPos)
                            if len(possibleMoves) == 0:
                                fromPos = None
                            self.Redraw(possibleMoves)
                    elif not toPos:
                        toPos = Position.GetChessPosition(mouseX, mouseY)
                        if toPos in possibleMoves:
                            return (fromPos, toPos)
                        elif self.IsPlayersPiece(mouseX, mouseY):
                            fromPos = Position.GetChessPosition(mouseX, mouseY)
                            toPos = None
                            possibleMoves = self.GetValidMoves(fromPos)
                            if len(possibleMoves) == 0:
                                fromPos = None
                            self.Redraw(possibleMoves)
                        else:
                            fromPos = None
                            toPos = None
                            possibleMoves = []
                            self.Redraw(possibleMoves)

    def ExitGame(self):
        pygame.quit()
        sys.exit(0)

    def IsPlayersPiece(self, mouseX, mouseY):
        fromPos = Position.GetChessPosition(mouseX, mouseY)
        if fromPos:
            piece = self.chessBoard.board[fromPos]
            if piece.color == self.chessBoard.playerColor:
                return True

    def GetValidMoves(self, fromPos):
        return self.chessBoard.GetValidMoves(fromPos)

    def MakeMove(self, fromPos, toPos):
        self.chessBoard.MakeMove(fromPos, toPos)

    def GameOver(self):
        if self.chessBoard.GameOver():
            self.Redraw()
            return True
        else:
            return False
