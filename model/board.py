from pickle import EMPTY_DICT
import copy


class Board:
  """This is a board class. Creates the gaming board
  """
  EMPTY_CELL = 0

  def __init__(self, size) -> None:
    self.size = size
    self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]


  def get_cell(self, row, col):
    """finds the matrix cell by given coordinates

    Args:
        row (int): x coordinate
        col (int): y coordinate
    """
    return self.mat[row][col]

  def update_cell(self, row, col, player):
    """Puts player's disk on the given cell

    Args:
        row (int): x coordinate
        col (int): y coordinate
        player (int): player number
    """
    self.mat[row][col] = player
  

  def copy_board(self):
    copy_board = copy.deepcopy(self.mat)
    return copy_board

