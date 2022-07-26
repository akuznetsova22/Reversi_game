from model.board import Board
from model.players import Player

class Game:
  """This is a Game class. Contains methods to run the game
  """
  def __init__(self, board_size):
    self.board = Board(board_size)
    self.curr_player = Player.X
  
  #placing starting player positions on board
  def initialize_board(self):
    player = Player.X
    for i in range(self.board.size//2-1, self.board.size//2+1):
      for j in range(self.board.size//2-1, self.board.size//2+1):
        self.board.mat[i][j] = player
        player = 3 - player
      player = 3 - player

  def change_player(self):
    self.curr_player = 3 - self.curr_player
    
  def make_move(self, row, col):
    available_flips = self.is_valid_move(row, col, self.curr_player)
    if available_flips:
      self.board.update_cell(row, col, self.curr_player)
      for row, col in available_flips:
        self.board.update_cell(row, col, self.curr_player)
  #Checks whether coordinates are within the board size
  def is_valid_coordinates(self, row, col):
    return row >= 0 and row <= self.board.size-1 and col >= 0 and col <= self.board.size-1
  
  #Checks validity of coordinates. If valid, stores the possible disks to flip, returns False if invalid
  def is_valid_move(self, row, col, player):
    #Checking if coordinates are on board and contain no players
    if self.board.mat[row][col] != Board.EMPTY_CELL or not self.is_valid_coordinates(row,col):
      return False
    #Temporary placing player and checking if other player can be flipped
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
        if not self.is_valid_coordinates(new_row,new_col):
          continue
        while self.board.mat[new_row][new_col] == 3-player:
          new_row += i
          new_col += j
          if not self.is_valid_coordinates(new_row, new_col): 
            break
        if not self.is_valid_coordinates(new_row, new_col):
          continue
        if self.board.mat[new_row][new_col] == player:
          while True:
            new_row -= i
            new_col -= j
            if new_row == row and new_col == col:
              break
            possible_flips.append([new_row, new_col])
    #Restoring the empty cell
    self.board.mat[row][col]= Board.EMPTY_CELL 
    if not len(possible_flips): 
      return False
    return possible_flips
  
  #lists all possible moves for the player
  def get_available_moves(self, player):
    moves = []
    for row in range(self.board.size):
      for col in range(self.board.size):
        if self.is_valid_move(row, col, player):
          moves.append([row, col])
    return moves
  

  def show_moves(self, player):
    moves = self.get_available_moves(player)
    user_moves = []
    for move in moves:
      user_moves.append([move[0]+1, move[1]+1])
    return user_moves
  
  #Checks whether there are moves left for both players
  def is_terminated(self):
    is_terminated = True
    player1 = 0
    player2 =0
    # if no disks left for either player returns True. Else checks whether both players have moves left
    for i in range(self.board.size-1):
      for j in range(self.board.size-1):
        if self.board.mat[i][j] == self.curr_player:
          player1 +=1
        elif self.board.mat[i][j] == 3- self.curr_player:
          player2 +=1
    if player1 > 0 and player2 > 0:
      is_terminated = False
    else:
      moves_left=len(self.get_available_moves(self.curr_player))
      if moves_left:
        return False
      else:
        moves_left=len(self.get_available_moves(3-self.curr_player))
        if moves_left:
          return False  
    return is_terminated
  
  def keep_score(self):
    player1_score = 0
    player2_score = 0
    for i in range(self.board.size):
      for j in range(self.board.size):
        if  self.board.mat[i][j] == Player.X:
          player1_score += 1
        elif self.board.mat[i][j] == Player.O:
          player2_score += 1
    score_board = {'X': player1_score, 'O': player2_score}
    return score_board
 
  def check_winner(self):
    scores = self.keep_score()
    if scores['X'] == scores['O']:
      winner = 'It was a draw'
    else:
      winner = max(scores)
    return winner 


    
  #Test