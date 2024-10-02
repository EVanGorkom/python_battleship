import unittest
from unittest.mock import patch
from lib.board import Board
from lib.ship import Ship
from lib.game import Game

class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  # @patch('builtins.input', side_effect=['p'])
  # def test_start(self, mock_input):
#     self.game.start()

  # @patch('builtins.input', side_effect=['q'])
  # def test_require_user_input_quit(self, mock_input):
#     # Test if require_user_input handles 'q' input correctly
#     with self.assertRaises(SystemExit):
#         self.game.require_user_input()

  # @patch('builtins.input', side_effect=['z'] * 7)
  # def test_require_user_input_invalid_input(self, mock_input):
#     # Test if require_user_input handles invalid input after 7 attempts
#     with self.assertRaises(SystemExit):
#         self.game.require_user_input()

  def test_generate_random_coordinate(self):
    # Test if generate_random_coordinate returns a valid coordinate
    coordinate = self.game.generate_random_coordinate()
    self.assertIn(coordinate, self.game.player_board.cells)

  @patch('random.choice', side_effect=['A1'])
  @patch('random.randint', return_value=0)
  def test_generate_ship_coors_direction_0(self, mock_randint, mock_choice):
    cruiser = Ship("Cruiser", 3)
    coordinates = self.game.generate_ship_coors(cruiser)
    expected_coordinates = ['A1', 'A2', 'A3']
    self.assertEqual(coordinates, expected_coordinates)

  @patch('random.choice', side_effect=['B2'])
  @patch('random.randint', return_value=1)
  def test_generate_ship_coors_direction_1(self, mock_randint, mock_choice):
    cruiser = Ship("Cruiser", 3)
    coordinates = self.game.generate_ship_coors(cruiser)
    expected_coordinates = ['B2', 'C2', 'D2']
    self.assertEqual(coordinates, expected_coordinates)

# if __name__ == '__main__':
#     unittest.main()
