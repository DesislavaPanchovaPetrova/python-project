#-------------------------------------------------------------------------------
# Name:        ImagesData
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import pygame
from pygame.locals import *


class Images():

    RootWhite = "Images" + os.sep + "Set" + os.sep + "White"
    RootBlack = "Images" + os.sep + "Set" + os.sep + "Black"

    bPawn = os.path.join(RootBlack, "Pawn.png")
    bRook = os.path.join(RootBlack, "Rook.png")
    bKnight = os.path.join(RootBlack, "Knight.png")
    bBishop = os.path.join(RootBlack, "Bishop.png")
    bKing = os.path.join(RootBlack, "King.png")
    bQueen = os.path.join(RootBlack, "Queen.png")

    wPawn = os.path.join(RootWhite, "Pawn.png")
    wRook = os.path.join(RootWhite, "Rook.png")
    wKnight = os.path.join(RootWhite, "Knight.png")
    wBishop = os.path.join(RootWhite, "Bishop.png")
    wKing = os.path.join(RootWhite, "King.png")
    wQueen = os.path.join(RootWhite, "Queen.png")

    ImageDimentions = (50, 50)

if __name__ == '__main__':
    img = Images()
    print(os.path.join("image", "white.png"))
    print(Images.bKing)
    print(Images.wPawn)
    print(Images.WhiteSqr)
