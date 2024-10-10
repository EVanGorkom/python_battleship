from lib.ship import Ship

class Cell:
  def __init__(self, coordinate):
    self.coordinate = coordinate
    self.ship = None
    self.fired_upon = False
  
  def empty_cell(self):
    return self.ship is None

  def place_ship(self, boat):
    self.ship = boat

  def fired_upon_status(self):
    return self.fired_upon
  
  def fire_upon(self):
    if self.ship != None and not self.fired_upon:
      self.ship.hit()
    self.fired_upon = True

  def render(self, reveal_ship=True):
    if self.fired_upon:
      if self.empty_cell():
        return "M"
      elif self.ship.sunk():
        return "X"
      elif self.ship and self.fired_upon:
        return "H"
      elif reveal_ship and not self.empty_cell():
        return "S"
    else:
      if reveal_ship and not self.empty_cell():
        return "S"
      else:
        return "*"
