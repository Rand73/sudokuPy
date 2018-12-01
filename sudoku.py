from sudoku.sudoku import Sudoku

print("Test avec grille de sudoku")

file = open("fichiers/puzzles.sdk", 'r')
board = file.readline().replace('\n', '')
file.close()
#sudoku = Sudoku("029405006640082000000000000908060200000000000005040803000000000000530021500109430")
sudoku = Sudoku("100000000000010000000000000000000001000000000000000000000000000000000000000000100")
#sudoku = Sudoku(board)
sudoku.display()
if sudoku.solve():
    sudoku.display()
