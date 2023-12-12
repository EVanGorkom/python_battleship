from lib.cell import Cell
from lib.ship import Ship
import pdb

class Board:
  def __init__(self):
    self.cells = self.create_cells

  def create_cells(self):
    cells = {}
    for letter in "A", "B", "C", "D":
      for num in range(1, 5):
        coordinate = f"{letter}{num}"
        cells[coordinate] = Cell(coordinate)
    return cells
  
  def valid_coordinate(self, coordinate):
    return coordinate in self.cells
  
  def valid_placement(self, ship, coordinates):
    if not (isinstance(ship, Ship) and isinstance(coordinates, list) and len(coordinates) == ship.length):
      return False
    
    return all(self.valid_coordinate(coor) and self.cells[coor].empty() for coor in coordinates)
  # still need to add in the consecutive? method from the ruby version