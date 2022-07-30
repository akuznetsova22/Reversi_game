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
#   def keep_score(self):
#     """Counts number of disks for each player on board
#     Returns:
#         dict: dictionary of players scores
#     """
#     player1_score = 0
#     player2_score = 0
#     for i in range(self.board.size):
#       for j in range(self.board.size):
#         if  self.board.mat[i][j] == HumanPlayer.X:
#           player1_score += 1
#         elif self.board.mat[i][j] == HumanPlayer.O:
#           player2_score += 1
#     score_board = {'X': player1_score, 'O': player2_score}
#     return score_board
#   def get_available_moves(self, player):
#     """ Lists all possible moves for the player. Used to give player a hint
#     Args:
#         player (int): player
#     Returns:
#         list: coordinates of possible moves for a given player
#     """
#     moves = []
#     for row in range(self.board.size):
#       for col in range(self.board.size):
#         if self.is_valid_move(row, col, player):
#           moves.append([row, col])
#     return moves
  
#   def select_best_move(self, player):
#     """selects the best move available for player (1 turn look-ahead)
#     Args:
#         player (int): player number
#     Returns:
#         list: coordinates of the best move
#         bool: False if there are no moves available
#     """
#     moves = self.get_available_moves(player)  
#     score_moves = []
#     #for each valid move check updated scores for each player
#     #current scores are updated by 1 move + potential flips
#     for move in moves:
#       scores = self.keep_score() 
#       new_disks = 1 + len(self.is_valid_move(move[0], move[1], self.curr_player))
#       if player == HumanPlayer.X:
#         scores['X'] += new_disks
#         scores['O'] -= (new_disks-1)
#         score_moves.append(scores['X']-scores['O'])
#       else:
#         scores['O'] += new_disks
#         scores['X'] -= (new_disks-1)
#         score_moves.append(scores['O']-scores['X'])
#     #Choosing the move that will result in more flipped disks. If none - returns False
#     if len(score_moves)>0:
#       ind_best_move = score_moves.index(max(score_moves))
#       best_move = moves[ind_best_move]
#       return best_move
#     else: 
#       return False


#   def show_moves(self, player):
#     """Gives coordinates of possible moves in a user-friendly way. 
#     Coordinates start from 1, not 0
#     Args:
#         player (int): player
#     Returns:
#         list: coordinates of possible moves for a given player
#     """
#     moves = self.get_available_moves(player)
#     user_moves = []
#     for move in moves:
#       user_moves.append([move[0]+1, move[1]+1])
#     return user_moves
  
  