from view.board_view import BoardView
from model.board import Board
from model.players import Player

class BoardConsoleView(BoardView):

    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board):
        super().__init__(board)
    

    def draw_board(self):
        board_size = self.board.size
        print('  | ', end='')
        for i in range (board_size):
            print(i+1,'|', end=' ')
        print()
        header = '--+'+'---+' * (board_size)
        print(header)
        for i in range(board_size):
            print('',i+1, end='')
            for j in range(board_size):
                cell = self.board.get_cell(i, j)
                print(f'| {self.symbols[cell]} ', end='')
            print('|')
            print(header)


  #Test 