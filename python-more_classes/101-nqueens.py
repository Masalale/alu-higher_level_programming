#!/usr/bin/python3
"""N-Queens Puzzle Solution"""
import sys


def is_safe(board, row, col, n):
    """Check if queen can be placed at position [row][col]"""
    """Check this column"""
    for i in range(row):
        if board[i] == col:
            return False

    """Check upper left diagonal"""
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    """Check upper right diagonal"""
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(n):
    """Find and print all solutions to N-queens puzzle"""
    solutions = []
    board = [-1] * n

    def solve_util(board, row):
        """If all queens placed, add solution"""
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        """Try placing queen in each column"""
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve_util(board, row + 1)
                """Backtrack"""
                board[row] = -1

    solve_util(board, 0)

    """Print solutions"""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """Validate input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
