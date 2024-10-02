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
    if not all(self.valid_coordinate(coor) and self.cells[coor].empty_cell() for coor in coordinates):
      return False
    return self.consecutive(coordinates)

  def consecutive(self, coordinates):
    rows = [coor[0] for coor in coordinates]
    cols = [int(coor[1:]) for coor in coordinates]
    same_row = all(row == rows[0] for row in rows)
    same_col = all(col == cols[0] for col in cols)
    consecutive_in_row = sorted(cols) == list(range(min(cols), max(cols) + 1))
    consecutive_in_col = sorted([ord(row) for row in rows]) == list(range(ord(min(rows)), ord(max(rows)) + 1))
    return (same_row and consecutive_in_row) or (same_col and consecutive_in_col)

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