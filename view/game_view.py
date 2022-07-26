from abc import ABC, abstractmethod
from model.game import Game

class GameView(ABC):
  """Abstract class Game View to be called by the controller
  """
  def __init__(self, game) -> None:
    self.game = game

  @abstractmethod
  def get_move(self):
    pass
  @abstractmethod
  def no_moves(self):
    pass
  @abstractmethod
  def display_invalid_move(self):
    pass
  @abstractmethod
  def draw_board(self):
    pass
  @abstractmethod
  def display_options(self):
    pass
  @abstractmethod
  def display_winner(self, player):
    pass

#Test