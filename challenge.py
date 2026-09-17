"""
CODING CHALLENGE

Validate a sudoku for the following rules:

- each row has every number between 1 and 9 exactly once
- each column has every number between 1 and 9 exactly once
- each 3x3 block has every number between 1 and 9 exactly once

Example input:
  "974236158638591742125487936316754289742918563589362417867125394253649871491873625"

Example return:
  True

Test cases can be found in test_challenge.py.

"""

def validate(puzzle: str) -> bool:
    if not has_valid_format(puzzle):
        return False
    return rows_are_valid(puzzle) and columns_are_valid(puzzle) and blocks_are_valid(puzzle)


def has_valid_format(puzzle: str) -> bool:
    return len(puzzle) == 81 and puzzle.isdigit() and "0" not in puzzle


def rows_are_valid(puzzle: str) -> bool:
    for row in range(9):
        row_chars = puzzle[row*9:(row+1)*9]
        if len(set(row_chars)) != 9:
            return False
    return True


def columns_are_valid(puzzle: str) -> bool:
    for col in range(9):
        col_chars = puzzle[col::9]
        if len(set(col_chars)) != 9:
            return False
    return True


def blocks_are_valid(puzzle: str) -> bool:
    blocks = [[] for _ in range(9)]          # one bucket per block, B0..B8
    for row in range(9):                     # outer loop: every row of the puzzle
        row_start = row * 9                  # index where this row begins in the flat string
        section = (row // 3) * 3             # which section this row belongs to: 0, 3, or 6
        for block_col in range(3):           # inner loop: the 3 blocks across this row
            col_start = row_start + block_col * 3
            blocks[section + block_col].extend(puzzle[col_start:col_start + 3])
    return all(len(set(block)) == 9 for block in blocks)