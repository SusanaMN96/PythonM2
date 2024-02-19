board = []
EMPTY = ' '
tst = 1

for i in range(8):
    row = [EMPTY for i in range(3)]
    board.append(row)
print(board)

board = [[EMPTY for i in range(3)] for j in range(8)]
print(board)
