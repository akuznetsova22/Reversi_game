from pickle import EMPTY_DICT


class Board:
  """This is a board class. Creates the gaming board
  """
  EMPTY_CELL = 0

  def __init__(self, size) -> None:
    self.size = size
    self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]


  def get_cell(self, row, col):
    return self.mat[row][col]

  def update_cell(self, row, col, player):
    self.mat[row][col] = player
  



#Test
