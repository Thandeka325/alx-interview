#!/usr/bin/python3
"""Solves the N Queens problem for N >= 4 using backtracking"""
import sys


def is_safe(row, col, queens):
    """Check if a queen can be placed at (row, col)"""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """Recursively solve the N queens problem"""
    if row == n:
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """Main entry point of the program"""
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

    solutions = []
    solve_nqueens(n, solutions=solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
