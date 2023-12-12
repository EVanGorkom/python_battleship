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
    board_instance = Board()
    cells = board_instance.create_cells()
    # self.assertDictContains(cells, "A1")