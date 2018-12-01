import math
from typing import List


class Sudoku:
    """Classe définissant une grille de sudoku et les méthodes necessaire à sa résolution"""
    _board: str
    _board_array: List[List[int]]
    _SIZE: int
    _BOX: int


    def __init__(self, board):
        """

        :type _size: Taille de la grille sudoku
        """
        self._board = board
        self._SIZE = int(math.sqrt(len(self._board)))
        self._BOX = int(math.sqrt(self._SIZE))
        self._board_array = []
        array: List[int] = []

        for i, num in enumerate(self._board):
            array.append(int(num))
            if (i + 1) % self._SIZE == 0 and i != 0:
                self._board_array.append(array)
                array = []

    def is_in_row(self, row: int, number: int):
        """Vérifie si la ligne contient déjà le nombre number.

        Retourne True si la ligne contient déjà le nombre number
        Retourne False si la ligne ne contient pas encore le nombre number

        """
        return number in self._board_array[row]

    def is_in_col(self, col: int, number: int):
        """Vérifie si la colonne contient déjà le nombre number.

        Retourne True si la colonne contient déjà le nombre number
        Retourne False si la colonne ne contient pas encore le nombre number

        """
        for i in self._board_array:
            if i[col] == number:
                return True
        return False

    def is_in_box(self, row: int, col: int, number: int):
        """Vérifie si la box contient déjà le nombre number.

        Retourne True si la box contient déjà le nombre number
        Retourne False si la box ne contient pas encore le nombre number

        """
        r = row - row % self._BOX
        c = col - col % self._BOX

        for i in range(r, r + 3, 1):
            for j in range(c, c + 3, 1):
                if self._board_array[i][j] == number:
                    return True
        return False

    def is_ok(self, row: int, col: int, number: int):
        if self.is_in_row(row, number) or self.is_in_col(col, number) or self.is_in_box(row, col, number):
            return False
        return True


    def solve(self):
        for r, row in enumerate(self._board_array):
            for c, number in enumerate(row):
                if number == 0:
                    for i in range(1, 10):
                        if self.is_ok(r, c, i):
                            self._board_array[r][c] = i
                            if self.solve():

                                return True
                            else:
                                self._board_array[r][c] = 0
                                #print(self._board_array)
                    return False
        self.display()
        return True


    def display(self):
        """Affiche la grille sur la console."""
        #print(self._board)
        self._board = ""
        for r in self._board_array:
            for num in r:
                self._board += str(num)

        size = len(self._board)
        size_box = math.sqrt(math.sqrt(size))
        # print(size_box)
        print_row_separator = " " + ("-" * int((size / (size_box * (size_box + 1) / size_box))))
        # print(len(print_row_separator))
        print_row = '| '
        print(print_row_separator)
        for i, row in enumerate(self._board):
            print_row += '{0} '.format(row)
            if (i + 1) % math.sqrt(math.sqrt(size)) == 0:
                print_row += '| '
            if (i + 1) % math.sqrt(size) == 0:
                print(print_row)
                print_row = '| '
            if (i + 1) % (size / size_box) == 0:
                print(print_row_separator)

    def __str__(self):
        s: str = ""
        for r in self._board_array:
            for num in r:
                s += str(num)
        return s
