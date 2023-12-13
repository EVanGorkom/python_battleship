from lib.cell import Cell
from lib.ship import Ship
import pdb

class Board:
  def __init__(self):
    self.cells = self.create_cells()

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
    return all(self.valid_coordinate(coor) and self.cells[coor].empty_cell() for coor in coordinates) and self.consecutive(coordinates)

  def consecutive(self, coordinates):
    chars_array = [coor[0] for coor in coordinates]
    nums_array = [int(coor[1]) for coor in coordinates]
    if len(set(chars_array)) == 1:
      return all(nums_array[i] + 1 == nums_array[i + 1] for i in range(len(nums_array) - 1))
    elif len(set(nums_array)) == 1:
      return all(ord(chars_array[i] + 1 == chars_array[i + 1] for i in range(len(chars_array) - 1)))
    else:
      return False

  def place(self, ship, coordinates):
    if self.valid_placement(ship, coordinates):
      for coordinate in coordinates:
        self.cells[coordinate].place_ship(ship)

  def render(self, reveal_ships=False):
    board_render = "  " + ' '.join('ABCD') + "\n"
    for row in range(1, 5):
      board_render += str(row) + " "
      for column in 'ABCD':
        coordinate = f"{column}{row}"
        cell = self.cells[coordinate]
        board_render += cell.render(reveal_ships) + " "
      board_render += "\n"
    print(board_render)

  def all_ships_sunk(self):
    return all(cell.empty_cell() or cell.ship.sunk() for cell in self.cells.values())