#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def nqueens(board, row, n):
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print(f'[{i}, {j}]', end=' ')
        print()
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            nqueens(board, row + 1, n)
            board[row][col] = 0

def solve_nqueens(n):
    if not n.isnumeric():
        print("N must be a number")
        sys.exit(1)
    
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])

