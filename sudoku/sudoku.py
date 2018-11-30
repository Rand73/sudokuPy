import math
from typing import List


class Sudoku:
    """Classe définissant une grille de sudoku et les méthodes necessaire à sa résolution"""
    _board_array: List[List[int]]
    _size: int
    _board: str

    def __init__(self, board):
        """

        :type size: Taille de la grille sudoku
        """
        self._board = board
        self._size = int(math.sqrt(len(self._board)))

        self._board_array = []
        array: List[int] = []

        for i, num in enumerate(self._board):
            array.append(int(num))
            if (i + 1) % self._size == 0 and i != 0:
                self._board_array.append(array)
                array = []

    def is_in_row(self, row: int, number: int):
        """Vérifie si la ligne contient déjà le nombre number.

        Retourne True si la ligne contient déjà le nombre number
        Retourne False si la ligne ne contient pas encore le nombre number

        """
        return True

    def is_in_col(self, col: int, number: int):
        """Vérifie si la colonne contient déjà le nombre number.

        Retourne True si la colonne contient déjà le nombre number
        Retourne False si la colonne ne contient pas encore le nombre number

        """
        return True

    def is_in_box(self, row: int, col: int, number: int):
        """Vérifie si la box contient déjà le nombre number.

        Retourne True si la box contient déjà le nombre number
        Retourne False si la box ne contient pas encore le nombre number

        """
        return True

    def is_ok(self, row: int, col: int, number: int):
        if self.is_in_row(row, number) or self.is_in_col(col, number) or self.is_in_box(row, col, number):
            return False
        return True

    def display(self):
        """Affiche la grille sur la console."""
        #print(self._board)
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
