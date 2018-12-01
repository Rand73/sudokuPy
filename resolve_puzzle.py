from sudoku.sudoku import Sudoku

res_puzzle = open("fichiers/puzzle_result.sdk", 'a')
puzzle = open("fichiers/puzzle.sdk", "r")

for line in puzzle:
    line = line.replace('\n', '')
    sudo = Sudoku(line)
    if sudo.solve():
        res_puzzle.write("{]\n".format(sudo))
        print(sudo)
puzzle.close()
res_puzzle.close()
