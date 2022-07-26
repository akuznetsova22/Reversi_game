from abc import ABC, abstractmethod
from model.board import Board

class BoardView(ABC):
  """Abstract class Board View to be called by the controller
  """
  def __init__(self, board: Board):
    self.board = board

  @abstractmethod
  def draw_board(self):
    pass

