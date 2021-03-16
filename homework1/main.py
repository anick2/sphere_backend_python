from termcolor import colored
import random
import time


class TicTac:

    def __init__(self):
        self.is_active = True
        self.player = False
        self.size = None
        self.board = None
        self.mode = None

    def setup_game(self):
        print("Enter a board size")
        self.size = self.validate_input('size')
        self.board = list(range(1, self.size * self.size + 1))

        print('Choose a game mode:')
        print(colored('1. Player vs Player', 'yellow'))
        print(colored('2. Player vs Computer', 'magenta'))
        print(colored('3. Computer vs Computer', 'blue'))
        self.mode = self.validate_input('mode')

    def start_game(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.setup_game()
            while self.is_active:
                self.show_board()
                self.make_move()
                if self.check_winner() or self.check_tie():
                    self.show_board()
                    s = 'Computer' \
                        if self.mode == 3 or self.mode == 2 and self.player\
                        else "Player"
                    s += ' ' + str(int(self.player) + 1) \
                        if self.mode in (1, 3) else ''
                    s += ", you win!" \
                        if self.check_winner() else "GAME OVER. Tie!"
                    print(s)
                    self.is_active = False
                self.player = not self.player

            print('Play again? +/-')
            s = self.validate_input('end')
            if s == '+':
                self.is_active = True
                self.player = False
            elif s == '-':
                print('Bye, see you soon!')
                break

    def show_board(self):
        print('-' * self.size * 6 + '-')
        for i in range(len(self.board)):
            if self.board[i] == 'X':
                print("|  " + colored(self.board[i], 'blue') + ' ', end=' ')
            elif self.board[i] == 'O':
                print("|  " + colored(self.board[i], 'magenta') + ' ', end=' ')
            else:
                print("| {:^3}".format(self.board[i]), end=' ')
            if (i + 1) % self.size == 0:
                print('|')
                print('-' * self.size * 6 + '-')

    def get_cell(self):
        time.sleep(1)
        tmp_board = [x for x in self.board if not x == 'X' and not x == 'O']
        cell = random.choice(tmp_board)
        return cell

    def make_move(self):
        if self.mode == 1:
            print("Player " + str(int(self.player) + 1) +
                  ", your turn. Please, enter a cell number: ")
            cell = self.validate_input('cell')
        elif self.mode == 2:
            if not self.player:
                print("Your turn. Please, enter a cell number: ")
                cell = self.validate_input('cell')
            else:
                print("Computer: ")
                cell = self.get_cell()
        elif self.mode == 3:
            print("Computer " + str(int(self.player) + 1) + ':')
            cell = self.get_cell()

        self.board[int(cell) - 1] = 'X' if self.player else 'O'

    def validate_input(self, case):
        while True:
            inp = input()

            if case == 'cell':
                try:
                    cell = int(inp)
                except ValueError:
                    print("Wrong input. It must be a number from 1 to "
                          + str(self.size * self.size))
                    continue
                if cell <= 0 or cell > self.size * self.size:
                    print("The input must be a number from 1 to "
                          + str(self.size * self.size))
                    continue
                elif self.board[cell - 1] == 'O' or \
                        self.board[cell - 1] == 'X':
                    print("This cell is busy. Please, choose another cell")
                    continue
                else:
                    return cell
            elif case == 'size':
                try:
                    size = int(inp)
                except ValueError:
                    print("Wrong input. It must be a number.")
                    continue
                else:
                    return size
            elif case == 'mode':
                if inp not in ('1', '2', '3'):
                    print("Wrong input. It must be 1, 2 or 3.")
                    continue
                else:
                    return int(inp)
            elif case == 'end':
                if inp not in ('+', '-'):
                    print("Wrong input. It must be + or -.")
                    continue
                else:
                    return inp

    def check_winner(self):
        # rows and columns
        for i in range(self.size):
            num_x_row = num_x_colm = 0
            num_o_row = num_o_colm = 0
            for j in range(self.size):
                num_x_row += 1 if self.board[i * self.size + j] == 'X' else 0
                num_o_row += 1 if self.board[i * self.size + j] == 'O' else 0
                num_x_colm += 1 if self.board[j * self.size + i] == 'X' else 0
                num_o_colm += 1 if self.board[j * self.size + i] == 'O' else 0

            if num_x_row == self.size or num_o_colm == self.size \
                    or num_o_row == self.size or num_x_colm == self.size:
                return True

        # diagonal
        num_x_diag1 = num_x_diag2 = 0
        num_o_diag1 = num_o_diag2 = 0

        for i in range(self.size):
            num_x_diag1 += 1 if self.board[i * self.size + i] == 'X' else 0
            num_o_diag1 += 1 if self.board[i * self.size + i] == 'O' else 0
            num_x_diag2 += 1 if self.board[i * self.size +
                                           (self.size - i - 1)] == 'X' else 0
            num_o_diag2 += 1 if self.board[i * self.size +
                                           (self.size - i - 1)] == 'O' else 0

        if num_x_diag1 == self.size or num_x_diag2 == self.size \
                or num_o_diag1 == self.size or num_o_diag2 == self.size:
            return True

        return False

    def check_tie(self):
        for i in range(1, self.size * self.size + 1):
            if i in self.board:
                return False
        return True


if __name__ == '__main__':
    game = TicTac()
    game.start_game()
