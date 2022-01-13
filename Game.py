from Board import Board

class Game:
  def __init__(self, player1, player2):
    self.p1 = player1
    self.p2 = player2
    self.gameEnd = False
  
  def run(self):
    print("Game is about to run:")
    board = Board()
    board.makeBoard()
    board.printBoard()

    nextPlayer = self.p1
    while self.gameEnd == False:
      if board.isUnplayable():#check if board is unplayable
        print("Game over. No more moves can be made.")
        return

      nextColumn = input(nextPlayer.name + ", what column do you want to play next? ")
      if not board.nextMove(nextColumn, nextPlayer.symbol):
        continue
      board.printBoard()
      if board.playerWins(nextPlayer):
        print(nextPlayer.name, "wins!")
        return
      nextPlayer = self.playerSwap(nextPlayer)

  def playerSwap(self, player):
    if player == self.p1:
      return self.p2
    return self.p1