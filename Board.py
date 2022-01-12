class Board:
  def __init__(self):
    self.rows = 6
    self.columns = 7
    self.spaces = []

  def makeBoard(self):
    for i in range(self.rows):
      row = []
      for j in range(self.columns):
        row.append("_")
      self.spaces.append(row)
    
    lastRow = ["A", "B", "C", "D", "E", "F", "G"]
    self.spaces.append(lastRow)

  def printBoard(self):
    for i in range(self.rows+1):
      print(self.spaces[i])

  #def nextMove(self, column, gamePiece):