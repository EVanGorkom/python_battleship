import unittest
import pdb
from lib.board import Board
from lib.cell import Cell
from lib.ship import Ship

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = Board()

  def test_existence(self):
    self.assertIsInstance(self.board, Board)

  def test_has_readable_attributes(self):
    board_instance = Board()
    cells = board_instance.create_cells()
    self.assertIsInstance(cells, dict)

  def test_creates_cells(self):
    expected_coordinates = set(f"{letter}{num}" for letter in "ABCD" for num in range(1, 5))
    cells = self.board.create_cells()
    self.assertIsInstance(cells, dict)
    self.assertEqual(set(cells.keys()), expected_coordinates)

  def test_valid_placement(self):
    ship = Ship("TestShip", 2)
    valid_coordinates = ["A1", "A2"]
    self.assertTrue(self.board.valid_placement(ship, valid_coordinates))

  def test_place_ship(self):
    ship = Ship("TestShip", 2)
    coordinates = ["A1", "A2"]
    self.board.place(ship, coordinates)
    for coordinate in coordinates:
      cell = self.board.cells[coordinate]
      self.assertEqual(cell.ship, ship)

  def test_render(self):
    ship = Ship("TestShip", 2)
    coordinates = ["A1", "A2"]
    self.board.place(ship, coordinates)

  def test_all_ships_sunk(self):
    ship = Ship("TestShip", 2)
    coordinates = ["A1", "A2"]
    self.board.place(ship, coordinates)
    self.assertFalse(self.board.all_ships_sunk())
    ship.hit()
    ship.hit()
    self.assertTrue(self.board.all_ships_sunk())
