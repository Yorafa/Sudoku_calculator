# @School: University of Toronto
# @Author: Tianle Wang
# @File: sudoku.py
# @Interpreter: python 3.9.
# @IDE: PyCharm
# Copyright 2021 by Tianle Wang
# All copyright reserved
"""
Specific notation:
The calculation should have the basic condition that the sudoku could be solved
else will raise can't solve information. All blank should not be written.
"""

from typing import List, TextIO, Optional


class Sudoku:
    """A sudoku is a game with specific gaming rule, where each number from
    1 - 9 should appear only once in one row or column or 'room'.

    ======= Attribute =======
    solution: the list contain 1 - 9 so that can be choose to test if satisfied
    the condition
    """
    sudoku: List[list]

    def __init__(self, sudoku: List[list]) -> None:
        """"""
        self.sudoku = sudoku

    def __str__(self) -> str:
        """"""
        line = ''
        for i in range(len(self.sudoku)):
            if i % 3 == 0:
                line += '-' * 25 + '\n'
            for j in range(len(self.sudoku[i])):
                if j % 3 == 0:
                    line += '| '
                line += self.sudoku[i][j] + ' '
            line += '|'
            line += '\n'
        line += '-' * 25 + '\n'
        return line

    def can_solve(self) -> bool:
        """"""
        if is_valid_numeric_data(self.sudoku):
            return True
        return False

    def write(self, sol: str, row: int, col: int) -> None:
        """"""
        self.sudoku[row][col] = sol

    def is_valid(self, sol: str, curr_row: int, curr_col: int) -> bool:
        """"""
        for i in range(len(self.sudoku[curr_row])):
            if sol == self.sudoku[curr_row][i]:
                return False
        for j in range(len(self.sudoku[0])):
            if sol == self.sudoku[j][curr_col]:
                return False
        room_row = curr_row // 3
        room_col = curr_col // 3
        for i in range(3):
            for j in range(3):
                if self.sudoku[3 * room_row + i][3 * room_col + j] == sol:
                    return False
        return True

    def zero_index(self) -> Optional[tuple]:
        """Return the index of first zero"""
        if not self.sudoku:
            return None
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == '0':
                    return i, j
        return None

    def print_result(self) -> str:
        """return a solution if can be solved, else print result"""
        if solve(self) and self.sudoku:
            return str(self)
        else:
            return '请检查你的数独是否可解'

    def write_solution(self, file: TextIO) -> None:
        """write solution into a file"""
        if not solve(self):
            file.write('This sudoku could not be solved\n\n')
        for i in range(len(self.sudoku)):
            line = ''
            if i % 3 == 0:
                line += '-' * 25 + '\n'
                file.write(line)
                line = ''
            for j in range(len(self.sudoku[i])):
                if j % 3 == 0:
                    line += '| '
                line += self.sudoku[i][j] + ' '
            line += '|\n'
            file.write(line)
        line = '-' * 25 + '\n'
        file.write(line)


def solve(sudoku: Sudoku):
    """return True iff sudoku can solve and be solved"""
    zero = sudoku.zero_index()
    if zero is None:
        return True
    for i in range(1, 10):
        if sudoku.is_valid(str(i), zero[0], zero[1]):
            sudoku.write(str(i), zero[0], zero[1])
            if solve(sudoku):
                return True
            sudoku.write('0', zero[0], zero[1])
    return False


def col_data(lst: List[list]) -> List[list]:
    """return the column of nested list lst"""
    col_lst =[]
    for i in range(9):
        col = []
        for j in range(9):
            col.append(lst[j][i])
        col_lst.append(col)
    return col_lst


def room_contain(item: any, row: int, col: int, lst: List[list]) -> bool:
    """"""
    room_row = row // 3
    room_col = col // 3
    for i in range(3):
        for j in range(3):
            if lst[3 * room_row + i][3 * room_col + j] == item and \
                    (3 * room_row + i != row) and (3 * room_col + i != col):
                return True
    return False


def is_valid_numeric_data(lst: List[list]) -> bool:
    """Check the data of list if numeric string and if repeat already

    pre-condition:
    lst is a 9x9 equally nested list
    """
    col_lst = col_data(lst)
    for i in range(9):
        for j in range(9):
            if not lst[i][j].isnumeric():
                print(1)
                return False
            if lst[i][j] in lst[i][j+1:] and lst[i][j] != '0':
                print(2)
                return False
            if lst[j][i] in col_lst[i][j+1:] and lst[j][i] != '0':
                print(3)
                return False
            if room_contain(lst[i][j], i, j, lst) and lst[i][j] != '0':
                print(4)
                return False
    return True


def read_data(file: TextIO) -> Sudoku:
    """Read sudoku data from file"""
    line = file.readline().strip().split(',')
    sudoku = []
    while line != ['']:
        for i in range(0, len(line)):
            line[i] = line[i].strip()
            if line[i] == '':
                line[i] = '0'
        sudoku.append(line)
        line = file.readline().strip().split(',')
    return Sudoku(sudoku)


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()
    pass
