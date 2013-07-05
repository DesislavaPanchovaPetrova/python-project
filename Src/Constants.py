#-------------------------------------------------------------------------------
# Name:        Constants
# Purpose:     Class with dictionaries with chess positions, piece types enum
#              values, color enum
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class PieceType:
    Empty = 0
    Illegal = 99
    wKing = 6
    wQueen = 5
    wRook = 4
    wBishop = 3
    wKnight = 2
    wPawn = 1
    bKing = 16
    bQueen = 15
    bRook = 14
    bBishop = 13
    bKnight = 12
    bPawn = 11


class Color:
    White = 'w'
    Black = 'b'
    Empty = 0

    @staticmethod
    def GetOpposite(color):
        if color == Color.White:
            return Color.Black
        elif color == Color.Black:
            return Color.White
        return Color.Empty


class Rank:
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8


class File:
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'

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


def main():
    pass

if __name__ == '__main__':
    main()
