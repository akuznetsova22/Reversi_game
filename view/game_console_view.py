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
    print(f'Player {player}: It\'s your turn.')
    while True:
      try:
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0])-1, int(s[1])-1
        break
      except:
        print('Coordinates should be two numbers, \
          separated by comma. Try again')
    return row, col
  def get_move_with_AI(self):
    """gets the move coordinates from the player
    Args:
        player (int): player
    """
    while True:
      try:
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0])-1, int(s[1])-1
        break
      except:
        print('Coordinates should be two numbers, \
          separated by comma. Try again')
    return row, col
  
  def no_moves(self):
    """Prints message to user if they have no moves left
    """
    print('You ran out of moves.')
  
  def display_invalid_move(self):
    """Prints message to user if the move is invalid
    """
    print('This is not a valid move! Try again.')

  def display_options(self):
    """Prints message asking whether they want a hint 
    """
    choice = input('Would you like to see possible moves?\nYes for hint, or No to continue ')
    return choice.lower()
  
  def draw_board(self):
    """calls draw board method from Board View class
    """
    self.board_view.draw_board()

  def display_winner(self, player):
    """prints the winner of the game message
    """
    print(f'The winner is: {player}')

  def menu(self):
    while True:
      try:
        choice = int(input('Welcome to Reversi. Select mode:\n1: to play against another player, 2: to play against computer: '))
        break
      except TypeError:
        print('Choose option 1 or 2')
      return choice
  def display_computer_move(self):
    print('It is computer turn now. Thinking...')
  
  