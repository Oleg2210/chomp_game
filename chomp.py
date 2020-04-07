#!/usr/bin/python3
import os


class Chomp:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cookie_field = [0 for i in range(0, row*column)]
        self.cookie_field[0] = 'X'

    def draw_field(self):
        index = 1
        for cookie in self.cookie_field:
            print(f"{cookie}  ", end='')
            if not(index % self.row):
                print("\n")
            index += 1


def input_chop_number(input_string):
    min_value = 2
    while True:
        os.system("clear")
        print(input_string)
        try:
            chop_number = int(input())
            if chop_number >= min_value:
                return chop_number
        except:
            continue


def chomp_run():
    rows_number = input_chop_number("Please input a number of rows:")
    column_number = input_chop_number("Please input a number of columns:")
    chomp = Chomp(rows_number, column_number)
    chomp.draw_field()


if __name__ == "__main__":
    chomp_run()

