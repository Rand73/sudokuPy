import math

class Sudoku:
    """Classe définissant une grille de sudoku et les méthodes necessaire à sa résolution"""


    def __init__(self, board):
        """

        :type size: Taille de la grille sudoku
        """
        self.board = board


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
        #print(self.board)
        size = len(self.board)
        size_box = math.sqrt(math.sqrt(size))
        #print(size_box)
        print_row_separator = " " + ("-" * int((size / (size_box * (size_box + 1)/size_box))))
        #print(len(print_row_separator))
        print_row = '| '
        print(print_row_separator)
        for i, row in enumerate(self.board):
            print_row += '{0} '.format(row)
            if (i + 1) % math.sqrt(math.sqrt(size)) == 0:
                print_row += '| '
            if (i + 1) % math.sqrt(size) == 0:
                print(print_row)
                print_row = '| '
            if (i + 1) % (size / size_box) == 0:
                print(print_row_separator)

