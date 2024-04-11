#!/usr/bin/python3
"""
N queens
"""
import sys


def is_safe(board, row, col):
    """
    This is to check if there is a queen in the same column
    """
    for i in range(row):
        if board[i] == col:
            return False
    """
    This is to check upper diagonal on left side
    """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    """
    Check upper diagonal on left side
    """
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False
    return True


def solve_nqueens(board, row):
    """
    This is to solve the nqueens
    """
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1


def print_solution(board):
    """
    This is to print the output
    """
    solution = []
    for i in range(N):
        solution.append([i, board[i]])
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    solve_nqueens(board, 0)
