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
    return True