from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game import Game

class GameConsoleView(GameView):
  """Console View Class.  Handles the interactions with the players
  """
  def __init__(self, game: Game) -> None:
    super().__init__(game)
    self.board_view = BoardConsoleView(game.board)

  def get_move(self,player):
    """gets the move coordinates from the player
    Args:
        player (int): player
    """
    if player == 1:
      curr_player = 'X'
    else:
      curr_player = 'O'
    print(f'Player {curr_player}: It\'s your turn.')
    while True:
      try:
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0])-1, int(s[1])-1
        break
      except:
        print('\nCoordinates should be two numbers, separated by comma. Try again')
    return row, col
  
  def get_move_with_AI(self):
    """gets the move coordinates from the player
    """
    while True:
      try:
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0])-1, int(s[1])-1
        break
      except:
        print('\nCoordinates should be two numbers, separated by comma. Try again')
    return row, col
  
  def no_moves(self, player):
    """Prints message to user if they have no moves left
    """
    print(f'\nPlayer {player}, you ran out of moves.')
  
  def display_invalid_move(self):
    """Prints message to user if the move is invalid
    """

    print('\nThis is not a valid move! Try again.')

  def display_options(self):
    """Prints message asking whether they want a hint 
    """
    print()
    choice = input('Would you like to see possible moves?\nYes for hint, or No to continue ')
    return choice.lower()
  
  def draw_board(self):
    """calls draw board method from Board View class
    """
    print()
    self.board_view.draw_board()

  def display_winner(self, player):
    """prints the winner of the game message
    """
    print(f'Game Over! The winner is: {player}')

  def menu(self):
    """inputs users choice of game mode. PvP or simple AI
    """
    while True:
      try:
        choice = int(input('\nWelcome to Reversi. Select mode:\
        \n\n1: to play against another player      2: to play against simple computer \
        \n3: to play against advanced computer   4: to play against hardcore AI\nYour choice:   '))              
        if choice in range (1,5):
          return choice
        else:
          print('Please choose option 1, 2, 3 or 4')
          choice = int(input('1: to play against another player, 2: to play against simple computer, 3: to play against advanced computer, 4: to play against hardcore AI:  '))
      except ValueError:
        print('Please choose option 1, 2, 3 or 4')
        # choice = int(input('1: to play against another player, 2: to play against simple computer, 3: to play against hardcore AI:  '))


  
  def display_computer_move(self):
    """prints message about computers turn
    """
    print('\nIt is computer\'s turn now. Thinking...')
  
  def display_scores(self, scores):
    """displays scores of the game

    Args:
        scores (dict): scores of the players
    """
    player1 = scores['X']
    player2 = scores['O']
    print(f'X score: {player1}, O score: {player2}')
    print()

  