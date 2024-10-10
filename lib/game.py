from lib.board import Board
from lib.cell import Cell
from lib.ship import Ship
import random
import time
import os
import pdb

class Game:
  def __init__(self):
    self.player_board = Board()
    self.computer_board = Board()
    self.game_over = False
    self.targeting_mode = False
    self.targeting_mode_coordinates = []
    # self.ships = [Ship("Cruiser", 3), Ship("Submarine", 2), Ship("Battleship", 4)]

  def start(self):
    os.system('clear')
    time.sleep(1)
    art_folder = os.path.join(os.path.dirname(__file__), 'ascii_art')
    title_file = os.path.join(art_folder, 'title.txt')
    with open(title_file, 'r') as file:
      content = file.read()
      print(content)
    print("Welcome to BATTLESHIP soldier!")
    self.require_user_input()

  def require_user_input(self):
    time.sleep(0.8)
    attempt_count = 1
    while True:
      user_input = input("Press 'p' to Play. \nPress 'q' to Quit.\n")
      if user_input.lower() == 'p':
        self.play()
        break
      elif user_input.lower() == 'q':
        print("Jeez, if you didn't want to play, why did you wake me up then?")
        break
      else:
        attempt_count += 1

      if user_input != 'p' and user_input != 'q' and attempt_count >= 7:
        print("\n\nYou leave me no choice.")
        time.sleep(0.8)
        print("I'm ending this for both of us.")
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        os.system('clear')
        break
      elif user_input != 'p' and user_input != 'q' and attempt_count >= 6:
        print("\n\nOh look, here we are again.")
      elif user_input != 'p' and user_input != 'q' and attempt_count >= 5:
        print("\n\nSurely you could be doing something else with your time.")
      elif user_input != 'p' and user_input != 'q' and attempt_count >= 4:
        print("\n\nHaving a laugh are we?")
      elif user_input != 'p' and user_input != 'q' and attempt_count >= 3:
        print("\n\nReally? Try again.")
      else:  
        print("\n\nWell that wasn't the letter 'p' or 'q' now was it? \nAre you sure you're qualified to operate a vessel of mass destruction soldier? \nTry agin, but watch what you type.")

  def check_game_over(self):
    if self.player_board.all_ships_sunk():
      print("All you ships have been sunk!\n")
      art_folder = os.path.join(os.path.dirname(__file__), 'ascii_art')
      game_over_file = os.path.join(art_folder, 'game_over.txt')
      with open(game_over_file, 'r') as file:
        content = file.read()
        print(content)
      self.game_over = True
      time.sleep(4)

    elif self.computer_board.all_ships_sunk():
      print("You've sunk all the computer's ships!\n")
      art_folder = os.path.join(os.path.dirname(__file__), 'ascii_art')
      victory_file = os.path.join(art_folder, 'victory.txt')
      with open(victory_file, 'r') as file:
        content = file.read()
        print(content)
      self.game_over = True
      time.sleep(4)

  def play(self):
    os.system('clear')
    print("Your opponent has placed their ships. Now it's your turn.")
    print("==============Player Board==============\n")
    self.player_board.render(True)
    self.computer_place_ships()
    self.player_place_ships()
    os.system('clear')
    
    while not self.game_over:
      self.player_turn()
      self.check_game_over()
      if self.game_over:
        self.play_again()

      self.computer_turn()
      self.check_game_over()
      if self.game_over:
        self.play_again()

  def play_again(self):
    os.system('clear')
    attempt_count = 1
    while True:
      user_input = input("\nDo you want to play again?\nPress 'p' for Play\nPress 'q' for Quit\n")
      if user_input.lower() == 'p':
        self.play()
        break
      elif user_input.lower() == 'q':
        print("See around soldier!")
        time.sleep(2)
        os.system('clear')
        break

      if attempt_count >= 6:
        print(". . . . bruh")
        time.sleep(2)
        os.system('clear')
        print("You're welcome")
        break
      elif attempt_count >= 2:
        print("\nOh, no thank you. \n'p' or 'q' will work fine.")
        attempt_count += 1
      else:
        attempt_count += 1

  def full_board_render(self):
    print("\n=============Computer Board=============\n")
    self.computer_board.render(True)
    # Toggle to False after testing is complete
    print("\n==============Player Board==============\n")
    self.player_board.render(True)

  def computer_place_ships(self):
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Submarine", 2)
    ships = [cruiser, submarine]
    for ship in ships:
      coordinates = []
      while not self.computer_board.valid_placement(ship, coordinates):
        coordinates = self.generate_ship_coors(ship)
      self.computer_board.place(ship, coordinates)

  def generate_ship_coors(self, ship):
    starting_coor = self.generate_random_coordinate()
    direction = random.randint(0, 1)
    coordinates = [starting_coor]
    times_looped = 0
    if direction == 0:
      for _ in range(ship.length - 1):
        letter = starting_coor[0]
        number = int(starting_coor[1]) + 1 + times_looped
        next_coor = f'{letter}{number}'
        coordinates.append(next_coor)
        times_looped += 1
    elif direction == 1:
      for _ in range(ship.length - 1):
        ord_letter = (ord(starting_coor[0]) + 1 + times_looped)
        letter = chr(ord_letter)
        number = starting_coor[1]
        next_coor = f'{letter}{number}'
        coordinates.append(next_coor)
        times_looped += 1
    return coordinates

  def generate_random_coordinate(self):
    rdm_coor = random.choice(list(self.player_board.cells.keys()))
    return rdm_coor

  def player_place_ships(self):
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Submarine", 2)
    ships = [cruiser, submarine]

    for ship in ships:
      valid_placement = False
      while not valid_placement:
        coordinates = self.get_users_coors(ship)
        if self.player_board.valid_placement(ship, coordinates):
          self.player_board.place(ship, coordinates)
          print(f"\n{ship.name} placed successfully!")
          print("==============Player Board==============\n")
          self.player_board.render(True)
          valid_placement = True 
          time.sleep(0.8)
        else:
          print("An invalid placement of a ship, soldier. Try again.\n")

  def get_users_coors(self, ship):
    while True:
      user_input = input(f"Where shall we put our {ship.name}, soldier?\nEnter {ship.length} coordinates separated by a space. Example: a2 b2 or A3 A4\n").upper()
      coordinates = user_input.split()
      if len(coordinates) == ship.length:
        return coordinates
      else:
        print(f"Invalid input! You need to provide {ship.length} coordinates. Try again.")

  def player_turn(self):
    os.system('clear')
    time.sleep(0.8)

    self.full_board_render()
    coordinate_to_fire = input("\nWhere shall we fire? (Enter any valid coordinate, EX: A1 or b3)\n").upper()
    if self.computer_board.valid_coordinate(coordinate_to_fire):
      target_cell = self.computer_board.cells[coordinate_to_fire]

      if target_cell.fired_upon_status():
        print(f"\nYou've already fired at {coordinate_to_fire}. Try another target soldier.")
      else:
        target_cell.fire_upon()

        if target_cell.empty_cell():
          print(f"\nMiss! {coordinate_to_fire} was empty!")
        else:
          if target_cell.ship.sunk():
            print(f"\nDirect hit! You've sunk the enemy's {target_cell.ship.name}!")
          else:
            print(f"\nDirect hit at {coordinate_to_fire}! The enemy's ship has sustained damage.")
    else:
      print("\nInvalid coordinate soldier! Try again.")
      self.player_turn()

  def computer_turn(self):
    time.sleep(0.8)
    print("\n\n\n")
    print("Computer's Turn")
    print("", end="", flush=True)

    for _ in range(3):
      time.sleep(0.8)
      print(".  ", end='', flush=True)
    print()

    if self.targeting_mode and len(self.targeting_mode_coordinates) != 0:
      coordinate_to_fire = random.choice(self.
      targeting_mode_coordinates)
      self.targeting_mode_coordinates.remove(coordinate_to_fire)
    else:
      coordinate_to_fire = None
      while coordinate_to_fire is None or self.player_board.cells[coordinate_to_fire].fired_upon_status():
        coordinate_to_fire = self.generate_random_coordinate()
          
    print(f"\nComputer fires at {coordinate_to_fire}!")
    target_cell = self.player_board.cells[coordinate_to_fire]
    target_cell.fire_upon()

    if target_cell.empty_cell():
      print(f"\nMiss! {coordinate_to_fire} was an empty cell.")
    else:
      if target_cell.ship.sunk():
        print(f"\nDirect hit! The computer sunk your {target_cell.ship.name}!")
        self.targeting_mode = False
      else:
        print(f"\nDirect hit at {coordinate_to_fire}! One of your ships was damaged.")
        self.targeting_mode = True
        self.find_adjacent_coordinates(coordinate_to_fire)
    
    time.sleep(0.8)
    time.sleep(0.8)

  def find_adjacent_coordinates(self, coordinate: str):
    letter = coordinate[0]
    letter_ord = ord(letter)
    number = int(coordinate[1])
    
    # I can add an additional check to make sure I'm not adding the same coordinate to the array more than once. something like `and not adjacent_coordinate in self.targeting_mode_coordinates`
    if number > 1:
      adjacent_coordinate = f"{letter}{number - 1}"
      if self.player_board.valid_coordinate(adjacent_coordinate) and not self.player_board.cells[adjacent_coordinate].fired_upon:
        self.targeting_mode_coordinates.append(adjacent_coordinate)

    if number < 4:
      adjacent_coordinate = f"{letter}{number + 1}"
      if self.player_board.valid_coordinate(adjacent_coordinate) and not self.player_board.cells[adjacent_coordinate].fired_upon:
        self.targeting_mode_coordinates.append(adjacent_coordinate) 

    if letter_ord > 65:
      adjacent_coordinate = f"{chr(letter_ord - 1)}{number}"
      if self.player_board.valid_coordinate(adjacent_coordinate) and not self.player_board.cells[adjacent_coordinate].fired_upon:
        self.targeting_mode_coordinates.append(adjacent_coordinate)

    if letter_ord < 69:
      adjacent_coordinate = f"{chr(letter_ord + 1)}{number}"
      if self.player_board.valid_coordinate(adjacent_coordinate) and not self.player_board.cells[adjacent_coordinate].fired_upon:
        self.targeting_mode_coordinates.append(adjacent_coordinate) 

