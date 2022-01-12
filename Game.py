from Board import Board

class Game:
  def __init__(self, player1, player2):
    self.p1 = player1
    self.p2 = player2
  
  def run(self):
    print("Game is about to run:")
    board = Board()
    board.makeBoard()
    board.printBoard()

    nextPlayer = self.p1
    nextColumn = input(nextPlayer.name + ", what column do you want to play next?")
    board.nextMove(nextColumn, nextPlayer.symbol)