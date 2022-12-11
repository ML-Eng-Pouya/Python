import random
my_list = [i for i in range(1, 10)]
random.shuffle(my_list)
sudoku_board = list()
tile_num = 1
sudo_set = {i for i in range(1, 10)}
for i in range(3):
    if not i:
        sudoku_board.append(my_list[:])
    else:
        sudoku_board.append(sudoku_board[i-1][3:])
        sudoku_board[i].extend(sudoku_board[i - 1][:3])
for i in range(3):
    sudoku_board.append(sudoku_board[i][1:])
    sudoku_board[i+3].extend(sudoku_board[i][:1])
for i in range(3):
    sudoku_board.append(sudoku_board[i][2:])
    sudoku_board[i + 6].extend(sudoku_board[i][:2])
print(sudoku_board)
for line in sudoku_board:
    print(line)

"""
[7, 4, 8, 9, 1, 6, 2, 5, 3]
[5, 3, 2, 8, 4, 7, 9, 6, 1]
[6, 1, 9, 2, 3, 5, 8, 7, 4]
[1, 8, 6, 5, 9, 3, 7, 4, 2]
[3, 9, 5, 7, 2, 4, 6, 1, 8]
[4, 2, 7, 6, 8, 1, 5, 3, 9]
[2, 5, 4, 1, 7, 8, 3, 9, 6]
[8, 7, 1, 3, 6, 9, 4, 2, 5]
[9, 6, 3, 4, 5, 2, 1, 8, 7]
"""