from model.board import Board
from model.players import HumanPlayer, AIPlayer
from model.moves import Move

class Game(Move):
  """This is a Game class. Contains methods to run the game
  """
  def __init__(self, board_size):
    self.board = Board(board_size)
    self.curr_player = HumanPlayer.X
  
  def initialize_board(self):
    """Placing starting 4 player disks on the centre of the board
    """
    player = HumanPlayer.X
    for i in range(self.board.size//2-1, self.board.size//2+1):
      for j in range(self.board.size//2-1, self.board.size//2+1):
        self.board.mat[i][j] = player
        player = 3 - player
      player = 3 - player

  def change_player(self):
    """Switches the active player
    """
    # if game_mode == 1:
    #   if self.curr_player == HumanPlayer.X:
    #     self.curr_player = HumanPlayer.O
    #   else:
    #     self.curr_player = HumanPlayer.X
    # elif game_mode == 2 or game_mode == 3:
    #   if self.curr_player == HumanPlayer.X:
    #     self.curr_player = AIPlayer.O
    #   else:
    #     self.curr_player == HumanPlayer.X
    self.curr_player = 3 - self.curr_player

  def make_move(self, row, col):
    """Updates the given board cell with players disk \
      if the move is valid and flips the opponents disks in between
    Args:
        row (int): x coordinate
        col (int): y coordinate
    """
    available_flips = self.is_valid_move(row, col, self.curr_player)
    if available_flips:
      self.board.update_cell(row, col, self.curr_player)
      for row, col in available_flips:
        self.board.update_cell(row, col, self.curr_player)

  
  def get_available_moves(self, player):
    """ Lists all possible moves for the player. Used to give player a hint
    Args:
        player (int): player
    Returns:
        list: coordinates of possible moves for a given player
    """
    moves = []
    for row in range(self.board.size):
      for col in range(self.board.size):
        if self.is_valid_move(row, col, player):
          moves.append([row, col])
    return moves
  
  def select_best_move(self, player):
    """selects the best move available for player (1 turn look-ahead)
    Args:
        player (int): player number
    Returns:
        list: coordinates of the best move
        bool: False if there are no moves available
    """
    moves = self.get_available_moves(player)  
    score_moves = []
    #for each valid move check updated scores for each player
    #current scores are updated by 1 move + potential flips
    for move in moves:
      scores = self.keep_score() 
      new_disks = 1 + len(self.is_valid_move(move[0], move[1], self.curr_player))
      if player == HumanPlayer.X:
        scores['X'] += new_disks
        scores['O'] -= (new_disks-1)
        score_moves.append(scores['X']-scores['O'])
      else:
        scores['O'] += new_disks
        scores['X'] -= (new_disks-1)
        score_moves.append(scores['O']-scores['X'])
    #Choosing the move that will result in more flipped disks. If none - returns False
    if len(score_moves)>0:
      ind_best_move = score_moves.index(max(score_moves))
      best_move = moves[ind_best_move]
      return best_move
    else: 
      return False



  def select_move_serious_AI(self):
    """Functions implements minimax algorithm to compute the best move for the AI player
    """
    moves = self.get_available_moves(self.curr_player)
    board_values = []
    for move in moves:
      new_board = self.board.copy_board()
      board_values.append(self.minimax(new_board, self.curr_player, 3-self.curr_player))
    if len(board_values):
      best_value = max(board_values)
      ind = 0
      for i in range(len(board_values)):
        if board_values[i] == best_value:
          ind = i
          break
      best_move = moves[ind]
    else:
      best_move = moves[0]
    return best_move


  def minimax(self, board, max_player, min_player):
    """Function recursively calculates the best move on the current board for given player
    Returns:
        list: coordinates of the best move
    """
    if self.is_terminated:
      return self.calculate_utility(HumanPlayer.O)
    moves = self.get_available_moves()
    move_scores = []
    for move in moves:
      new_board = self.copy_board()
      new_board[move[0]][move[1]] = HumanPlayer.O
      board_value = self.minimax(new_board, min_player, max_player)
      move_scores.append(board_value)
    if HumanPlayer.O == max_player:
      return max(move_scores)
    elif HumanPlayer.X == max_player:
      return min(move_scores)
  
  def show_moves(self, player):
    """Gives coordinates of possible moves in a user-friendly way. 
    Coordinates start from 1, not 0
    Args:
        player (int): player
    Returns:
        list: coordinates of possible moves for a given player
    """
    moves = self.get_available_moves(player)
    user_moves = []
    for move in moves:
      user_moves.append([move[0]+1, move[1]+1])
    return user_moves
  
  def is_terminated(self):
    """  Checks whether there are moves left for both players 
    and there are disks of both players on board
    Returns:
        bool: True if the game should be terminated
    """
    is_terminated = True
    player1 = 0
    player2 =0
    empty_cells = 0
    # Checks if no disks left for either player. 
    # Else: checks whether both players have moves left
    for i in range(self.board.size-1):
      for j in range(self.board.size-1):
        if self.board.mat[i][j] == self.curr_player:
          player1 +=1
        elif self.board.mat[i][j] == 3- self.curr_player:
          player2 +=1
        else:
          empty_cells+=1
    if player1 > 0 and player2 > 0 and empty_cells>0:
      is_terminated = False
    else:
      moves_left=len(self.get_available_moves(self.curr_player))
      if moves_left>0:
        return False
      else:
        moves_left=len(self.get_available_moves(3-self.curr_player))
        if moves_left>0:
          return False  
    return is_terminated
  
  def keep_score(self):
    """Counts number of disks for each player on board
    Returns:
        dict: dictionary of players scores
    """
    player1_score = 0
    player2_score = 0
    for i in range(self.board.size):
      for j in range(self.board.size):
        if  self.board.mat[i][j] == HumanPlayer.X:
          player1_score += 1
        elif self.board.mat[i][j] == HumanPlayer.O:
          player2_score += 1
    score_board = {'X': player1_score, 'O': player2_score}
    return score_board
  
  def weighted_scores(self):
    """Assignes weights to the board cells, based on their advantage to player and calculates scores

    Returns:
        dict: weighted scores of players disks
    """
    cell_scores = [[1] * self.board.size for _ in range(self.board.size)]
    
    for i in range(1,self.board.size-1):
      for j in range(1,self.board.size-1):
        cell_scores[i][0] = 10
        cell_scores[i][self.board.size-1] = 10
        cell_scores[0][j] = 10
        cell_scores[self.board.size-1][j] = 10
    cell_scores[0][0] = 100
    cell_scores[0][self.board.size-1] = 100
    cell_scores[self.board.size-1][0] = 100
    cell_scores[self.board.size-1][self.board.size-1] = 100
    cell_scores[1][0]= -10
    cell_scores[1][self.board.size-1] = -10
    cell_scores[self.board.size-2][0] = -10
    cell_scores[self.board.size-2][self.board.size-1] = -10
    cell_scores[0][self.board.size-2] = -10
    cell_scores[0][1] = -10
    cell_scores[self.board.size-1][1] = -10
    cell_scores[self.board.size-1][self.board.size-2] = -10  

    player1_score = 0
    player2_score = 0

    for i in range(self.board.size):
      for j in range(self.board.size):
        if  self.board.mat[i][j] == HumanPlayer.X:
          player1_score += cell_scores[i][j]
        elif self.board.mat[i][j] == HumanPlayer.O:
          player2_score += cell_scores[i][j]
    weighted_scores = {'X_weighted': player1_score, 'O_weighted': player2_score}
    return weighted_scores
  
  def calculate_utility(self, player):
    """Function calculates the utility for a given player
    """
    X_score = self.weighted_scores()['X_weighted']
    O_score = self.weighted_scores()['O_weighted']
    if player == HumanPlayer.X:
      utility = X_score-O_score
    else:
      utility = O_score - X_score
    return utility

  def check_winner(self):
    """Checks the winner of the game

    Returns:
        int: winner player
    """
    scores = self.keep_score()
    if scores['X'] == scores['O']:
      winner = 'It was a draw'
    else:
       winner_score = max(scores.values())
    if scores['X'] == winner_score:
        winner = 'X'
    else:
        winner = 'O'
    return winner 

  
    

    
