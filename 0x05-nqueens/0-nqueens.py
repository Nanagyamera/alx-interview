#!/usr/bin/python3
"""
N queens solution module.
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if there is a queen in the same column
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solves the N Queens problem and returns a list of all valid solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """
        Backtracking function to explore valid solutions for the
        N Queens problem.
        """
        if row == N:
            solutions.append([(row, col) for col in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
