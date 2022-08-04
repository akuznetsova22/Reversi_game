from model.board import Board
from model.players import HumanPlayer, AIPlayer

class Move:
  """This is a Move class. Contains methods to check validity of the move
  """
  def __init__(self, board_size):
    self.board = Board(board_size)
    self.curr_player = HumanPlayer.X

  def is_valid_coordinates(self, row, col):
    """Checks whether coordinates are within the board size
    Args:
        row (int): x coordinate
        col (_type_): y coordinate
    Returns:
        bool: True if the coordinates are < the board size and >= 0
    """
    return row >= 0 and row <= self.board.size-1 and col >= 0 and col <= self.board.size-1
  
  def is_valid_move(self, row, col, player):
    """  #Checks validity of coordinates.
    Args:
        row (_type_): _description_
        col (_type_): _description_
        player (_type_): _description_
    Returns:
        bool: returns False if the move is invalid
        list: returns the coordinates of all possible disks to flip if the move is valid
    """
    #Checking if coordinates are on board and contain no players disks
    if self.board.mat[row][col] != Board.EMPTY_CELL or not self.is_valid_coordinates(row,col):
      return False
    #Temporary placing player and checking if other player disks can be flipped
    self.board.mat[row][col] = player
    possible_flips = []
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for i, j in directions:
      new_row, new_col = row, col
      new_row += i 
      new_col += j
      if self.is_valid_coordinates(new_row,new_col) and self.board.mat[new_row][new_col] == 3-player:
        new_row += i
        new_col += j

        while self.is_valid_coordinates(new_row, new_col) and self.board.mat[new_row][new_col] == 3-player:
          new_row += i
          new_col += j
        if not self.is_valid_coordinates(new_row, new_col):
          continue
        if self.board.mat[new_row][new_col] == player:
          while True:
            new_row -= i
            new_col -= j
            if new_row == row and new_col == col:
              break
            possible_flips.append([new_row, new_col])
    #Restoring the initial empty cell
    self.board.mat[row][col]= Board.EMPTY_CELL 
    # Returns false if no opponent disks to be flipped are found.
    # if found - returns list of disks coordinates
    if not len(possible_flips): 
      return False
    return possible_flips

  
  