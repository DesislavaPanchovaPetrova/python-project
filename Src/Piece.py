#-------------------------------------------------------------------------------
# Name:        Piece
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Position import *
from Constants import Color as ChessColor
from Constants import PieceType
import pygame
from pygame.locals import *


class Piece():

    def __init__(self, color=ChessColor.Empty, pType=PieceType.Illegal, pos=0):
        if hasattr(self, 'imagePath'):
            self.image = pygame.image.load(self.imagePath)
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.color = color
        self.type = pType
        self.position = Position(pos)

    def draw(self, screen):
        if hasattr(self, 'image'):
            screenPos = self.position.ScreenXY()
            screen.blit(self.image, screenPos)

    def is_empty(self):
        return True

    def GetPossibleMoves(self, board):
        return []


class PieceEmpty(Piece):

    def __init__(self, pos):
        Piece.__init__(self, ChessColor.Empty, PieceType.Empty, pos)

    def GetPossibleMoves(self, board):
        return []


class PieceIllegal(Piece):

    def __init__(self, pos):
        Piece.__init__(self, ChessColor.Empty, PieceType.Illegal, pos)

    def GetPossibleMoves(self, board):
        return []
