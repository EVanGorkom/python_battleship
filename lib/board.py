from cell import Cell
import pdb

class Board:
  def __init__(self, cells):
    self.cells = self.create_cells

  def create_cells(self):
    cells = {}
    for letter in "A", "B", "C", "D":
      for num in range(1, 5):
        coordinate = f"{letter}{num}"
        cells[coordinate] = Cell(coordinate)
    pdb.set_trace()
    return cells