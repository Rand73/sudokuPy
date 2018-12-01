from sudoku.sudoku import Sudoku

puzzle = open("fichiers/puzzles.sdk", 'r')
res_puzzle = open("fichiers/puzzle_result.sdk", 'a')


for line in puzzle:
    line = line.replace('\n', '')
    sudo = Sudoku(line)
    if sudo.solve():
        res_puzzle.write("{]\n".format(sudo))
        print(sudo)
puzzle.close()
res_puzzle.close()
