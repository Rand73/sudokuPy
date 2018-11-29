from sudoku.sudoku import Sudoku

print("Test avec grille de sudoku")

file = open("fichiers/puzzles.sdk", 'r')
board = file.readline().replace('\n', '')
file.close()
sudoku = Sudoku(board)

print(sudoku)
print(sudoku)

