from Game import Game #from the file Game.py, import the class Game
from Player import Player #from the file Player.py, import the class Player

def main():
  player1 = Player("Bob", "x")
  player2 = Player("Alice", "o")
  game = Game(player1, player2)
  game.run()

main()