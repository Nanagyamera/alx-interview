N Queens Problem Solver

This is a Python program that solves the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard. The program uses a backtracking algorithm to find and print all possible solutions to the problem.

Requirements

Python 3.x

Error Handling

The program handles the following error cases:

If the user provides the wrong number of arguments, it will display an error message: Usage: nqueens N, followed by a new line, and exit with status 1.

If the provided N is not an integer, it will display an error message: N must be a number, followed by a new line, and exit with status 1.

If N is smaller than 4, it will display an error message: N must be at least 4, followed by a new line, and exit with status 1.

Implementation Details

The program utilizes a backtracking algorithm to find valid configurations for placing queens on the chessboard. The function is_safe(board, row, col, N) checks if it is safe to place a queen at a particular position on the board, ensuring that no other queens attack it horizontally, vertically, or diagonally.

The solve_nqueens(N) function finds all possible solutions by recursively exploring the chessboard and placing queens in safe positions. When a solution is found, it is stored in the solutions list.

The program prints each solution as a string representation of the chessboard, where 'Q' represents a queen and '.' represents an empty cell.

License

This program is provided under the MIT License.
