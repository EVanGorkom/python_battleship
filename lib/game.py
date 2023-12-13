from lib.board import Board
from lib.cell import Cell
from lib.ship import Ship
import time
import os

class Game:
  def __init__(self):
    self.player_board = Board()
    self.computer_board = Board()
    # self.ships = [Ship("Cruiser", 2), Ship("Battleship", 3)]

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
        print("\n\nAlright, I'm ending this for both our sake's.")
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
        print("\n\nReally?")
      else:  
        print("\n\nWell that wasn't the letter 'p' or 'q' now was it? Are you sure you're qualified to operate a vessel of mass destruction soldier? \nTry agin, but watch what you type.")

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
        print("Your welcome")
      elif attempt_count >= 2:
        print("Oh, no thank you. \n'y' or 'n' will work fine.")
      else:
        attempt_count += 1

  def computer_place_ships(self):
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Cruiser", 2)
    ships = [cruiser, submarine]
    

  def player_place_ships(self):
    return # add code here
  
  def player_turn(self):
    return # add code here
  
  def computer_turn(self):
    return # add code here
