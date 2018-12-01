import unittest
from sudoku.sudoku import Sudoku

sudo = Sudoku("200000060000075030048090100000300000300010009000008000001020570080730000090000004")

"""
    pour info 
board_array = [[2 0 0, 0 0 0, 0 6 0],
               [0 0 0, 0 7 5, 0 3 0],
               [0 4 8, 0 9 0, 1 0 0],
               
               [0 0 0, 3 0 0, 0 0 0],
               [3 0 0, 0 1 0, 0 0 9],
               [0 0 0, 0 0 8, 0 0 0],
               
               [0 0 1, 0 2 0, 5 7 0],
               [0 8 0, 7 3 0, 0 0 0],
               [0 9 0, 0 0 0, 0 0 4]]
"""


class MyTestSudoku(unittest.TestCase):

    def test_is_in_row(self):
        self.assertEqual(sudo.is_in_row(0, 3), False)
        self.assertEqual(sudo.is_in_row(0, 2), True)
        self.assertEqual(sudo.is_in_row(1, 7), True)
        self.assertEqual(sudo.is_in_row(8, 4), True)

    def test_is_in_col(self):
        self.assertEqual(sudo.is_in_col(0, 3), True)
        self.assertEqual(sudo.is_in_col(7, 3), True)
        self.assertEqual(sudo.is_in_col(4, 3), True)
        self.assertEqual(sudo.is_in_col(1, 9), True)

    def test_is_in_box(self):
        self.assertEqual(sudo.is_in_box(2, 2, 2), True)
        self.assertEqual(sudo.is_in_box(3, 4, 8), True)
        self.assertEqual(sudo.is_in_box(7, 5, 7), True)
        self.assertEqual(sudo.is_in_box(4, 7, 9), True)

    def test_is_ok(self):
        self.assertEqual(sudo.is_ok(5, 3, 9), True)
        self.assertEqual(sudo.is_ok(8, 5, 1), True)
        self.assertEqual(sudo.is_ok(6, 1, 6), True)
        self.assertEqual(sudo.is_ok(0, 6, 4), True)

        self.assertEqual(sudo.is_ok(1, 1, 8), False)



if __name__ == '__main__':
    unittest.main()
