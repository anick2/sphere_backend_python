import unittest.mock
import sys
from contextlib import contextmanager
from io import StringIO

from main import TicTac


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestTicTac(unittest.TestCase):

    def setUp(self):
        self.game = TicTac()

    def test_tie(self):
        self.game.size = 3

        self.game.board = [1, 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        self.assertEqual(self.game.check_tie(), False)

        self.game.board = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O']
        self.assertEqual(self.game.check_tie(), True)

        self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 'X']
        self.assertEqual(self.game.check_tie(), False)

        self.game.size = 4

        self.game.board = [1, 'X', 3, 'O', 'O', 'X', 7, 'O',
                           'X', 'O', 11, 12, 'O', 14, 'X', 'X']
        self.assertEqual(self.game.check_tie(), False)

        self.game.board = ['O', 'X', 'X', 'O', 'O', 'X', 'X', 'O',
                           'X', 'O', 'X', 'O', 'O', 'X', 'X', 'X']
        self.assertEqual(self.game.check_tie(), True)

    def test_winner(self):
        self.game.size = 3

        self.game.board = [1, 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['X', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['X', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'X']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O']
        self.assertEqual(self.game.check_winner(), False)

        self.game.board = ['O', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'O']
        self.assertEqual(self.game.check_winner(), True)

        self.game.size = 4

        self.game.board = ['O', 'O', 'O', 'O', 'X', 'X', 'X', 'O',
                           'O', 'X', 'X', 'O', 'X', 'X', 'X', 'O']
        self.assertEqual(self.game.check_winner(), True)

        self.game.board = ['O', 'O', 'O', 'X', 'X', 'O', 'X', 'O',
                           'X', 'X', 'O', 'X', 'O', 'O', 'X', 'X']
        self.assertEqual(self.game.check_winner(), False)

    def test_get_cell(self):
        self.game.size = 3

        self.game.board = ['X', 2, 3, 'O', 'X', 6, 'X', 'O', 9]
        self.assertIn(self.game.get_cell(), [2, 3, 6, 9])

        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 8, 'O']
        self.assertIn(self.game.get_cell(), [8])

        self.game.board = [1, 'O', 3, 'O', 5, 'O', 'X', 8, 9]
        self.assertIn(self.game.get_cell(), [1, 3, 5, 8, 9])

    @unittest.mock.patch('builtins.input', side_effect=['5', '3'])
    def test_setup1(self, mock_input):
        with captured_output() as (out, err):
            self.game.setup_game()
        self.assertEqual(self.game.size, 5)
        self.assertEqual(self.game.mode, 3)

    @unittest.mock.patch('builtins.input', side_effect=['3w', '3', '2'])
    def test_setup2(self, mock_input):
        with captured_output() as (out, err):
            self.game.setup_game()

        lines = out.getvalue().splitlines()
        self.assertIn('Enter a board size', lines)
        self.assertIn('Wrong input. It must be a number.', lines)
        self.assertEqual(self.game.size, 3)
        self.assertEqual(self.game.mode, 2)

    @unittest.mock.patch('builtins.input',
                         side_effect=['wjendk', '3', '709', '2'])
    def test_validation_cell(self, mock_input):
        self.game.size = 3
        self.game.board = [1, 2, 'X', 'O', 5, 'X', 7, 8, 'O']

        with captured_output() as (out, err):
            outp = self.game.validate_input('cell')

        lines = out.getvalue().splitlines()

        self.assertIn("Wrong input. It must be a number from 1 to 9", lines)
        self.assertIn("This cell is busy. Please, choose another cell", lines)
        self.assertIn("The input must be a number from 1 to 9", lines)
        self.assertEqual(outp, 2)

    @unittest.mock.patch('builtins.input', side_effect=[' 2a', '5'])
    def test_validation_size(self, mock_input):
        with captured_output() as (out, err):
            outp = self.game.validate_input('size')

        lines = out.getvalue().splitlines()

        self.assertIn('Wrong input. It must be a number.', lines)
        self.assertEqual(outp, 5)

    @unittest.mock.patch('builtins.input', side_effect=['5', 'ed3', '2'])
    def test_validation_mode(self, mock_input):
        with captured_output() as (out, err):
            outp = self.game.validate_input('mode')

        lines = out.getvalue().splitlines()

        self.assertIn("Wrong input. It must be 1, 2 or 3.", lines)
        self.assertIn("Wrong input. It must be 1, 2 or 3.", lines)
        self.assertEqual(outp, 2)

    @unittest.mock.patch('builtins.input', side_effect=['q', '3', '+'])
    def test_validation_end(self, mock_input):
        with captured_output() as (out, err):
            outp = self.game.validate_input('end')

        lines = out.getvalue().splitlines()

        self.assertIn("Wrong input. It must be + or -.", lines)
        self.assertIn("Wrong input. It must be + or -.", lines)
        self.assertEqual(outp, '+')

    @unittest.mock.patch('builtins.input', side_effect=['3', '2'])
    def test_move(self, mock_input):
        self.game.size = 3
        self.game.mode = 1
        self.game.player = False
        self.game.board = [1, 2, 'X', 4, 'O', 6, 7, 'X', 9]

        with captured_output() as (out, err):
            self.game.make_move()

        lines = out.getvalue().splitlines()
        self.assertIn("This cell is busy. Please, choose another cell", lines)
        self.assertIn("Player 1, your turn. "
                      "Please, enter a cell number: ", lines)
        self.assertEqual(self.game.board, [1, 'O', 'X', 4, 'O', 6, 7, 'X', 9])

    @unittest.mock.patch('builtins.input', side_effect=['3', '2', '-'])
    def test_start_game(self, mock_input):
        self.game.is_active = False

        with captured_output() as (out, err):
            self.game.start_game()

        lines = out.getvalue().splitlines()

        self.assertIn('Welcome to Tic Tac Toe!', lines)
        self.assertIn('Enter a board size', lines)
        self.assertIn('Choose a game mode:', lines)
        self.assertIn('Play again? +/-', lines)
        self.assertIn('Bye, see you soon!', lines)

    def test_show_board(self):
        self.game.size = 3
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        with captured_output() as (out, err):
            self.game.show_board()

        lines = out.getvalue().splitlines()

        self.assertIn('-' * 3 * 6 + '-', lines)
        self.assertIn('|  1  |  2  |  3  |', lines)
        self.assertIn('|  4  |  5  |  6  |', lines)
        self.assertIn('|  7  |  8  |  9  |', lines)
