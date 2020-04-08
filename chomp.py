#!/usr/bin/python3
import os


class Chomp:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cookie_field = ['0' for i in range(0, row*column)]
        self.cookie_field[0] = 'X'
        self._whose_turn = '1'

    def run(self):
        loose_state = None
        while loose_state is None:
            loose_state = self._check_loose()
            self._take_move()
            self._whose_turn = '2' if (self._whose_turn == '1') else '1'

    @staticmethod
    def input_number(output_string, min_value):
        while True:
            os.system("clear")
            print(output_string)
            try:
                chop_number = int(input())
                if chop_number >= min_value:
                    return chop_number
            except Exception:
                continue

    def _take_move(self):
        print(f"Turn of the {self._whose_turn} player. Please choose your cookie(Input format is \"row/column\"):")

    def draw_field(self):
        index = 1
        for cookie in self.cookie_field:
            print(f"{cookie}  ", end='')
            if not(index % self.row):
                print("\n")
            index += 1

    def _check_loose(self):
        if (self.cookie_field[1] != '0') and (self.cookie_field[self.row] != '0'):
            return self._whose_turn
        return None


def chomp_run():
    rows_number = Chomp.input_number(output_string="Please input a number of rows:", min_value=2)
    column_number = Chomp.input_number(output_string="Please input a number of columns:", min_value=2)
    chomp = Chomp(rows_number, column_number)
    chomp.draw_field()


if __name__ == "__main__":
    chomp_run()

