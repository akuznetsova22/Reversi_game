import unittest
from model.board import Board
from model.game import Game
from model.moves import Move

class TestIsValidCoordinates(unittest.TestCase):
    def test_negative_coordinates(self):
        self.assertEqual(Move.is_valid_coordinates(Move(8), -10, 10), False)
    def test_coordinates_not_on_board(self):
        self.assertEqual(Move.is_valid_coordinates(Move(8), 100, 100), False)
    def test_acceptable_coordinates(self):
        self.assertEqual(Move.is_valid_coordinates(Move(8), 0, 1), True)

class TestIsValidMove(unittest.TestCase):
    
    def test_returns_flips(self):
        #initialising the board to test
        board = Move(5)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        #test
        self.assertEqual(Move.is_valid_move(board, 1, 3, 1), [[1,2]])

    def test_no_disks_to_flip(self):
        #initialising the board to test
        board = Move(5)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        #test
        self.assertEqual(Move.is_valid_move(board, 0, 1, 1), False)
    def test_not_allowed_move(self):
        #initialising the board to test
        board = Move(5)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        #test
        self.assertEqual(Move.is_valid_move(board, 4, 4, 1), False)
    
    def test_available_flips(self):
        #initialising the board to test
        board = Game(5)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        self.assertEqual(board.get_available_moves(1),[[0, 2], [1, 3], [2, 0], [3, 1]])

class  TestAIMoves(unittest.TestCase):

    def test_best_move_simple_AI(self):
        #initialising the board to test
        board = Game(8)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        #test
        self.assertEqual(board.select_best_move(1),[2,4])
    
    def test_best_move_advanced_AI(self):
        #initialising the board to test
        board = Game(8)
        player = 1
        for i in range(board.board.size//2-1, board.board.size//2+1):
            for j in range(board.board.size//2-1, board.board.size//2+1):
                board.board.mat[i][j] = player
                player = 3 - player
            player = 3 - player
        #test
        self.assertEqual(board.select_move_serious_AI(4),[2,3])


        
    

