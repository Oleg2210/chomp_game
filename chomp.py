#!/usr/bin/python3
import os
import re


class Chomp:#dawd
    def __init__(self, row_number, column_number):
        self.row_number = row_number
        self.column_number = column_number
        self._cookie_field = ['0' for i in range(0, row_number*column_number)]
        self._cookie_field[0] = 'X'
        self._whose_turn = '1'

    def run(self):
        loose_state = None
        while loose_state is None:
            self._take_move()
            self._whose_turn = '2' if (self._whose_turn == '1') else '1'
            loose_state = self._check_loose()
        os.system("clear")
        print(f"{loose_state} player has loosed")

    @classmethod
    def get_size_numbers(cls):
        row_number = int(cls.get_input("Please input a number of rows(min=2, max=9):", "^[2-9]$"))
        column_number = int(cls.get_input("Please input a number of columns(min=2, max=9):", "^[2-9]$"))
        return row_number, column_number

    @staticmethod
    def get_input(output_string, string_format, clear=True):
        while True:
            if clear:
                os.system("clear")
            print(output_string)
            inp_string = input()
            if re.match(string_format, inp_string):
                return inp_string

    def _draw_field(self):
        index = 1
        for cookie in self._cookie_field:
            print(f"{cookie}  ", end='')
            if not(index % self.column_number):
                print("\n")
            index += 1

    def _check_loose(self):
        if (self._cookie_field[1] != '0') and (self._cookie_field[self.row_number] != '0'):
            return self._whose_turn
        return None

    def _take_move(self):
        while True:
            os.system("clear")
            self._draw_field()
            cookie_number = self._get_cookie_number()
            if self._eat_cookies(cookie_number):
                return

    def _get_cookie_number(self):
        while True:
            output_string = f"Turn of the {self._whose_turn} player. " \
                            f"Please choose your cookie(Input format is \"row/column\"):"
            row, column = self.get_input(output_string, "^[1-9]/[1-9]$", False).split('/')
            cookie_number = ((int(row) - 1) * self.column_number) + int(column) - 1
            if cookie_number < len(self._cookie_field):
                return cookie_number

    def _eat_cookies(self, cookie_number):
        if self._cookie_field[cookie_number] == '0':
            cookie_column = self._get_cookies_column(cookie_number)

            while cookie_number < (self.row_number * self.column_number):
                if self._cookie_field[cookie_number] == '0':
                    current_column = self._get_cookies_column(cookie_number)
                    if current_column >= cookie_column:
                        self._cookie_field[cookie_number] = self._whose_turn
                cookie_number += 1
            return True
        else:
            return False

    def _get_cookies_column(self, cookie_number):
        cookie_column = (cookie_number + 1) % self.column_number
        return cookie_column if cookie_column else self.column_number


if __name__ == "__main__":
    while True:
        row_number, column_number = Chomp.get_size_numbers()
        chomp = Chomp(row_number, column_number)
        chomp.run()

        again = Chomp.get_input("Do you want to play again?(y/n)", "^[yn]$", False)
        if again == 'n':
            break

