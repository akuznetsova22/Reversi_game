from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game import Game

class GameConsoleView(GameView):
  def __init__(self, game: Game) -> None:
    super().__init__(game)
    self.board_view = BoardConsoleView(game.board)

  def get_move(self,player):
    print(f'Player {player}: It\'s your turn.')
    s = input('Enter your move (row, col):').split(',')
    row, col = int(s[0])-1, int(s[1])-1
    return row, col
  
  def no_moves(self):
    print('You ran out of moves.')
  
  def display_invalid_move(self):
      print('This is not a valid move! Try again.')

  def display_options(self):
    choice = input('Would you like to see possible moves? Enter Yes or No ')
    return choice.lower()
  
  def draw_board(self):
    self.board_view.draw_board()

  def display_winner(self, player):
    print(f'The winner is: {player}')
  
  
  
  