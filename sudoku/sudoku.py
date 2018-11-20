


class Sudoku:
    """Classe définissant une grille de sudoku et les méthodes necessaire à sa résolution"""


    def __init__(self, size: int):
        """

        :type size: Taille de la grille sudoku
        """
        self.board = [0] * size, [0] * size
        return

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
