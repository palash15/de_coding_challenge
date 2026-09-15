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
    if not _has_valid_format(puzzle):
        return False
    return _rows_are_valid(puzzle) and _columns_are_valid(puzzle) and _blocks_are_valid(puzzle)


def _has_valid_format(puzzle: str) -> bool:
    return len(puzzle) == 81 and puzzle.isdigit() and "0" not in puzzle


def _rows_are_valid(puzzle: str) -> bool:
    for i in range(9):
        row = puzzle[i*9:(i+1)*9]
        if len(set(row)) != 9:
            return False
    return True


def _columns_are_valid(puzzle: str) -> bool:
    for j in range(9):
        column = puzzle[j::9]
        if len(set(column)) != 9:
            return False
    return True


def _blocks_are_valid(puzzle: str) -> bool:
    for section in range(3):
        row_shift = section * 3
        blocks = [[], [], []]
        for i in range(3):
            row = row_shift + i
            row_start = row * 9
            for col_shift in range(3):
                start = row_start + col_shift * 3
                blocks[col_shift].extend(puzzle[start:start + 3])
        for block in blocks:
            if len(set(block)) != 9:
                return False
    return True