#-------------------------------------------------------------------------------
# Name:        Position
# Purpose:
#
# Author:      Deesis
#
# Created:
# Copyright:   (c) Deesis
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Position():

    SQUARE_DIM = 50
    ILLEGAL_VALUE = 0
    FILE_TO_INT = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    INT_TO_FILE = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    RANK_TO_SCREEN_Y = {1: 8*SQUARE_DIM, 2: 7*SQUARE_DIM,
                        3: 6*SQUARE_DIM, 4: 5*SQUARE_DIM,
                        5: 4*SQUARE_DIM, 6: 3*SQUARE_DIM,
                        7: 2*SQUARE_DIM, 8: 1*SQUARE_DIM}
    FILE_TO_SCREEN_X = {1: 1*SQUARE_DIM, 2: 2*SQUARE_DIM,
                        3: 3*SQUARE_DIM, 4: 4*SQUARE_DIM,
                        5: 5*SQUARE_DIM, 6: 6*SQUARE_DIM,
                        7: 7*SQUARE_DIM, 8: 8*SQUARE_DIM}
    POS_TO_RANK_FILE = \
         {0: (0, 0),  1: (0, 0),  2: (0, 0),  3: (0, 0),  4: (0, 0),  5: (0, 0),  6: (0, 0),  7: (0, 0),  8: (0, 0),  9: (0, 0),
         10: (0, 0), 11: (0, 0), 12: (0, 0), 13: (0, 0), 14: (0, 0), 15: (0, 0), 16: (0, 0), 17: (0, 0), 18: (0, 0), 19: (0, 0),
         20: (0, 0), 21: (1, 1), 22: (1, 2), 23: (1, 3), 24: (1, 4), 25: (1, 5), 26: (1, 6), 27: (1, 7), 28: (1, 8), 29: (0, 0),
         30: (0, 0), 31: (2, 1), 32: (2, 2), 33: (2, 3), 34: (2, 4), 35: (2, 5), 36: (2, 6), 37: (2, 7), 38: (2, 8), 39: (0, 0),
         40: (0, 0), 41: (3, 1), 42: (3, 2), 43: (3, 3), 44: (3, 4), 45: (3, 5), 46: (3, 6), 47: (3, 7), 48: (3, 8), 49: (0, 0),
         50: (0, 0), 51: (4, 1), 52: (4, 2), 53: (4, 3), 54: (4, 4), 55: (4, 5), 56: (4, 6), 57: (4, 7), 58: (4, 8), 59: (0, 0),
         60: (0, 0), 61: (5, 1), 62: (5, 2), 63: (5, 3), 64: (5, 4), 65: (5, 5), 66: (5, 6), 67: (5, 7), 68: (5, 8), 69: (0, 0),
         70: (0, 0), 71: (6, 1), 72: (6, 2), 73: (6, 3), 74: (6, 4), 75: (6, 5), 76: (6, 6), 77: (6, 7), 78: (6, 8), 79: (0, 0),
         80: (0, 0), 81: (7, 1), 82: (7, 2), 83: (7, 3), 84: (7, 4), 85: (7, 5), 86: (7, 6), 87: (7, 7), 88: (7, 8), 89: (0, 0),
         90: (0, 0), 91: (8, 1), 92: (8, 2), 93: (8, 3), 94: (8, 4), 95: (8, 5), 96: (8, 6), 97: (8, 7), 98: (8, 8), 99: (0, 0),
         100: (0, 0), 101: (0, 0), 102: (0, 0), 103: (0, 0), 104: (0, 0), 105: (0, 0), 106: (0, 0), 107: (0, 0), 108: (0, 0), 109: (0, 0),
         110: (0, 0), 111: (0, 0), 112: (0, 0), 113: (0, 0), 114: (0, 0), 115: (0, 0), 116: (0, 0), 117: (0, 0), 118: (0, 0), 119: (0, 0)}

    RANK_FILE_TO_POS = \
        {(1, 1): 21, (1, 2): 22, (1, 3): 23, (1, 4): 24, (1, 5): 25, (1, 6): 26, (1, 7): 27, (1, 8): 28,
         (2, 1): 31, (2, 2): 32, (2, 3): 33, (2, 4): 34, (2, 5): 35, (2, 6): 36, (2, 7): 37, (2, 8): 38,
         (3, 1): 41, (3, 2): 42, (3, 3): 43, (3, 4): 44, (3, 5): 45, (3, 6): 46, (3, 7): 47, (3, 8): 48,
         (4, 1): 51, (4, 2): 52, (4, 3): 53, (4, 4): 54, (4, 5): 55, (4, 6): 56, (4, 7): 57, (4, 8): 58,
         (5, 1): 61, (5, 2): 62, (5, 3): 63, (5, 4): 64, (5, 5): 65, (5, 6): 66, (5, 7): 67, (5, 8): 68,
         (6, 1): 71, (6, 2): 72, (6, 3): 73, (6, 4): 74, (6, 5): 75, (6, 6): 76, (6, 7): 77, (6, 8): 78,
         (7, 1): 81, (7, 2): 82, (7, 3): 83, (7, 4): 84, (7, 5): 85, (7, 6): 86, (7, 7): 87, (7, 8): 88,
         (8, 1): 91, (8, 2): 92, (8, 3): 93, (8, 4): 94, (8, 5): 95, (8, 6): 96, (8, 7): 97, (8, 8): 98}

    def __init__(self, pos):
        if pos in self.POS_TO_RANK_FILE.keys():
            self.value = pos
            self.rank = self.POS_TO_RANK_FILE[self.value][0]
            self.file = self.POS_TO_RANK_FILE[self.value][1]

    def ScreenX(self):
        return self.FILE_TO_SCREEN_X[self.file]

    def ScreenY(self):
        return self.RANK_TO_SCREEN_Y[self.rank]

    def ScreenXY(self):
        if self.file in self.FILE_TO_SCREEN_X.keys()\
            and self.rank in self.RANK_TO_SCREEN_Y.keys():
            return (self.FILE_TO_SCREEN_X[self.file], self.RANK_TO_SCREEN_Y[self.rank])

    def IsBlackSquare(self):
        if self.file and self.rank:
            return ((self.rank + self.file) % 2 == 0)

    @staticmethod
    def GetChessPosition(x, y):
        file = x // Position.SQUARE_DIM
        rank = 9 - y // Position.SQUARE_DIM
        if (rank, file) in Position.RANK_FILE_TO_POS.keys():
            return Position.RANK_FILE_TO_POS[(rank, file)]

    def __add__(self, number):
        return Position(self.value + number)

    def __radd__(self, number):
        return Position(self.value + number)

    def __iadd__(self, number):
        self.value = self.value + number
        self.rank = self.POS_TO_RANK_FILE[self.value][0]
        self.file = self.POS_TO_RANK_FILE[self.value][1]

    def __sub__(self, number):
        return Position(self.value - number)

    def __rsub__(self, number):
        return Position(number - self.value)

    def __isub__(self, number):
        self.value = self.value + number
        self.rank = self.POS_TO_RANK_FILE[self.value][0]
        self.file = self.POS_TO_RANK_FILE[self.value][1]

    def __eq__(self, position):
        return self.value == position.value

    def is_illegal(self):
        return self.value not in range(120)

    def is_legal(self):
        return self.value in range(120)


def main():
    pass

if __name__ == '__main__':
    main()
