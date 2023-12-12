import unittest
from lib.ship import Ship
from lib.cell import Cell

class TestCell(unittest.TestCase):
  def setUp(self):
    self.cell = Cell("B4")
    self.cruiser = Ship("Cruiser", 3)

  def test_exists(self):
    self.assertIsInstance(self.cell, Cell)

  def has_readable_attributes(self):
    self.assertEqual(self.cell.coordinate, "B4")
    self.assertIsNone(self.cell.ship)

  def test_empty(self):
    self.cell.place_ship(self.cruiser)
    self.assertEqual(self.cell.ship, self.cruiser)
    self.assertFalse(self.cell.empty_cell())

  def test_place_ship(self):
    self.assertTrue(self.cell.empty_cell())
    self.cell.place_ship(self.cruiser)
    self.assertEqual(self.cell.ship, self.cruiser)
    self.assertFalse(self.cell.empty_cell())

  def test_fired_upon(self):
    self.cell.place_ship(self.cruiser)
    self.assertFalse(self.cell.fired_upon)

  def test_fire_upon(self):
    self.cell.place_ship(self.cruiser)
    self.cell.fire_upon()
    self.assertEqual(self.cell.ship.health, 2) 