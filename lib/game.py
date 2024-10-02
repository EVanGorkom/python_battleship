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

  def play(self):
    os.system('clear')
    print("Your opponent has placed their ships. Now it's your turn soldier.")
    print("==============Player Board==============\n")
    self.player_board.render(True)
    self.computer_place_ships()
    self.player_place_ships()
    os.system('clear')
    while self.game_over == False:
      self.player_turn()
      if self.game_over == True:
        break
      self.computer_turn()
      if self.game_over == True:
        break

  def play_again(self):
    os.system('clear')
    attempt_count = 1
    while True:
      user_input = input("Do you want to play again?\nPress 'y' for Yes\nPress 'n' for No\n")
      if user_input.lower() == 'y':
        self.play()
        break
      elif user_input.lower() == 'n':
        print("See around soldier!")
        time.sleep(2)
        os.system('clear')
        break

      if attempt_count >= 6:
        print(". . . . bruh")
        time.sleep(2)
        os.system('clear')
        print("You're welcome")
      elif attempt_count >= 2:
        print("Oh, no thank you. \n'y' or 'n' will work fine.")
      else:
        attempt_count += 1

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
        # pdb.set_trace() 
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
    # print(f"Generated Coordinates for {ship.name}: {coordinates}")
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
        else:
          print("An invalid placement of a ship, soldier. Try again.")

  def get_users_coors(self, ship):
    input(f"Where shall we put our {ship.name} soldier?\nEnter the {ship.length} coordinates you'd like separated with a space. \nEX: a2 b2 or A3 A4\n").upper()

  def player_turn(self):
    return # add code here
  
  def computer_turn(self):
    return # add code here
