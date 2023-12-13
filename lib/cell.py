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
    if self.ship is not None and not self.fired_upon:
      self.ship.hit()
    self.fired_upon = True

  def render(self, reveal_ship=False):
    if self.fired_upon:
      if self.empty():
        return "M"
      elif self.ship.sunk():
        return "X"
      elif reveal_ship and not self.empty():
        return "S"
      else:
        return "*"
    else:
      return " "