import unittest
from lib.ship import Ship

class TestShip(unittest.TestCase):
  def setUp(self):
    self.cruiser = Ship("Cruiser", 3)

  def test_exists(self):
    self.assertIsInstance(self.cruiser, Ship)

  def test_has_readable_attributes(self):
    self.assertEqual(self.cruiser.name, "Cruiser")
    self.assertEqual(self.cruiser.length, 3)
    self.assertEqual(self.cruiser.health, 3)

  def test_hit(self):
    self.assertEqual(self.cruiser.health, 3)
    self.cruiser.hit()
    self.assertEqual(self.cruiser.health, 2)

  def test_sunk(self):
    self.assertFalse(self.cruiser.sunk())
    self.cruiser.hit()
    self.cruiser.hit()
    self.cruiser.hit()
    self.assertTrue(self.cruiser.sunk())