from sudoku.sudoku import Sudoku

puzzle = open("fichiers/puzzles.sdk", 'r')
res_puzzle = open("fichiers/puzzle_result.sdk", 'a')

i=0
for line in puzzle:
    i += 1
    line = line.replace('\n', '')
    sudo = Sudoku(line)
    if sudo.solve():
        res_puzzle.write("{}\n".format(sudo))
        print(i)
puzzle.close()
res_puzzle.close()
