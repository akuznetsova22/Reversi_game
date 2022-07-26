from view.game_view import GameView
from model.game import Game
from datetime import datetime

class GameController:
    """Game Controller class. Connects view with model
    """
    def __init__(self, view: GameView, model: Game) -> None:
        self.view = view
        self.model = model

    def run_game_pvp(self): 
        """Runs the Reversi game player vs player
        """
        #creating the board with starting player positions and displaying it to the user   
        self.model.initialize_board()
        while True:
            self.view.draw_board()
            row, col = self.view.get_move(self.model.curr_player)
            while not self.model.is_valid_move(row, col, self.model.curr_player):
                #check if the move isnt valid due to no possible moves left:
                #if yes - switch to another player. if not - offer user a hint
                if len(self.model.get_available_moves(self.model.curr_player)):
                    self.view.display_invalid_move()
                    if self.view.display_options() == 'yes':
                        print(self.model.show_moves(self.model.curr_player))
                    row, col = self.view.get_move(self.model.curr_player)
                else:
                    self.view.no_moves()
                    self.model.change_player()
                    self.view.get_move(self.model.curr_player)
            self.model.make_move(row, col)
            self.model.change_player()
            #terminate game if not moves left for both players
            if self.model.is_terminated():
                break
        #checks the winner of the game
        player = self.model.check_winner()
        if player:
            self.view.display_winner(player)
    def run_game_AI(self): 
        """Runs the Reversi game with a simple AI
        """
        #creating the board with starting player positions and displaying it to the user   
        self.model.initialize_board()
        while not self.model.is_terminated():
            self.view.draw_board()
            row, col = self.view.get_move_with_AI()
            while not self.model.is_valid_move(row, col, self.model.curr_player):
                #check if the move isnt valid due to no possible moves left:
                #if yes - switch to another player. if not - offer user a hint
                if len(self.model.get_available_moves(self.model.curr_player)):
                    self.view.display_invalid_move()
                    if self.view.display_options() == 'yes':
                        print(self.model.show_moves(self.model.curr_player))
                    row, col = self.view.get_move(self.model.curr_player)
                else:
                    self.view.no_moves()
                    self.model.change_player()
                    self.view.get_move(self.model.curr_player)
            self.model.make_move(row, col)
            self.model.change_player()
            self.view.draw_board()
            #terminate game if not moves left for both players
            if self.model.is_terminated():
                break
            else:
                self.view.display_computer_move()
                AI_move = self.model.select_best_move(self.model.curr_player)
                if AI_move:
                    self.model.make_move(AI_move[0], AI_move[1])
                    self.model.change_player()
                else:
                    break
        #checks the winner of the game
        player = self.model.check_winner()
        if player:
            self.view.display_winner(player)
    
    def save_winner(self):
        """Saves the information (date, winner, scores) about the game in a text file
        """
        winner = self.model.check_winner()
        scores = self.model.keep_score()
        date = datetime.now()
        game_date = f'{date.year}-{date.month}-{date.day}  {date.hour}:{date.minute}'
        with open('Reversi_scores.txt', 'w') as f:
            print(f'Date: {game_date}, Winner: {winner}, Scores: {scores}', file = f)


