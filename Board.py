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

  def nextMove(self, column, gamePiece):
    canPlace = True
    columnNum = ord(column) - 65
    bottom = 5
    while self.spaces[bottom][columnNum] != '_':
      bottom -= 1
      if bottom == -1:
        break
    
    if bottom == -1:
      canPlace = False
      print("Column full. Choose a new column to play.")
    if canPlace:
      self.spaces[bottom][columnNum] = gamePiece
    return canPlace
  
  def playerWins(self, player):
    four = 4*[str(player.symbol)]
    for i in range(self.rows):
      for j in range(self.columns - len(four) + 1):
        if four == self.spaces[i][j:j+4]:
          return True

    for i in range(self.columns):
      for j in range(self.rows - len(four) + 1):
        count = 0 # count number of similarities
        for k in range(j, j + 4):
          if self.spaces[k][i] == four[k - j]:
            count += 1
        if count == 4:
          return True

    # for i in range(self.columns - len(four) + 1):
    #   for j in range(self.rows - len(four) + 1):
    #     count = 0
    #     for k in range(j, j + 4):
    #       if self.spaces[k - j][k] == four[k - j]:
    #         count += 1
    #     if count == 4:
    #       return True

    for i in range(self.columns - len(four) + 1):
      for j in range():

    return False
    
  def isUnplayable(self):
    if not '_' in self.spaces[0]:
      return True
    return False