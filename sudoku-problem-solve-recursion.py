import numpy as np

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# sudoku
board = np.array(board)

####### fonksiyonlar ########

def isColumnTrue(n, x, y, sudoku):

    size = len(sudoku)

    # sutun kontrol
    for i in range(size):
        if sudoku[i][y] == n:
            return False

    return True

def isRowTrue(n, x, y, sudoku):

    size = len(sudoku)

    # satir kontrol
    for i in range(size):
        if sudoku[x][i] == n:
            return False

    return True

def isAreaTrue(n, x, y, sudoku):

    size = len(board)

    # bolge kontrol
    x_range_first = (x // 3) * 3
    x_range_last = x_range_first + 3
    y_range_first = (y // 3) * 3
    y_range_last = y_range_first + 3

    # x = 4, y = 7 olsun
    # aralik x icin = 3,6
    # aralik y icin = 6,9
    for i in range(x_range_first, x_range_last):
        for c in range(y_range_first, y_range_last):
            if sudoku[i][c] == n:
                return False

    return True

def sudoku_solve():

    global board
    size = len(board)

    # tum bosluklar icin sudoku uygunlugunu kontrol eden recursi
    for i in range(size):
        for c in range(size):
            if board[i][c] == 0:

                # bosluklara tum rakamlari deniyor
                for rakam in range(1, 10):
                    if isColumnTrue(rakam, i, c, board) and isRowTrue(rakam, i, c, board) and isAreaTrue(rakam, i, c, board):
                        board[i][c] = rakam
                        sudoku_solve()
                        board[i][c] = 0

                    else:
                        pass

                return

            else:
                pass

    print("Sudoku Çözüm:")
    print(board)



####### programların çalıştırılması

# baslangıç sudoku ekrana yazdırmak
print('Örnek Sudoku Problemi ')
print(board)
print("\n\n")

# Çözülmüş sudoku haritasınu ekrana yazdırmak
sudoku_solve()
