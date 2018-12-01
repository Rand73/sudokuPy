from sudoku.sudoku import Sudoku

print("Test avec grille de sudoku")

file = open("fichiers/puzzles.sdk", 'r')
board = file.readline().replace('\n', '')
file.close()
#sudoku = Sudoku("800000000003600000070090200050007000000045700000100030001000068008500010090000400")
sudoku = Sudoku(board)
sudoku.display()
if sudoku.solve():
    sudoku.display()
