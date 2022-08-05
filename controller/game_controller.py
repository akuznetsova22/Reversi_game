from view.game_view import GameView
from model.game import Game
from datetime import datetime

class GameController:
    """Game Controller class. Connects view with model
    """
    def __init__(self, view: GameView, model: Game) -> None:
        self.view = view
        self.model = model
   
    def run_game(self):
        #Initialising the board and choosing game_mode (PvP or PvAI)
        game_mode = self.view.menu()
        self.model.initialize_board()
        while not self.model.is_terminated():
            #printing updated board with scores
            self.view.draw_board()
            self.view.display_scores(self.model.keep_score())
            #If moves available for current player - get move
            if len(self.model.get_available_moves(self.model.curr_player)):    
                row, col = self.view.get_move(self.model.curr_player)
                while not self.model.is_valid_move(row, col, self.model.curr_player):
                    #offer user a hint in case of invalid input
                    self.view.display_invalid_move()
                    if self.view.display_options() == 'yes':
                        print(self.model.show_moves(self.model.curr_player))
                    row, col = self.view.get_move(self.model.curr_player)
                #when input is valid - make the move and switch another player
                self.model.make_move(row, col)
                self.model.change_player(game_mode)
            #Switches player if no available moves left. 
            else:
                self.view.no_moves(self.model.curr_player)
                self.model.change_player(game_mode)
            #in case of computer mode, make computer move:
            if game_mode != 1:
                self.view.draw_board()
                self.view.display_computer_move()
                if game_mode == 2:
                    AI_move = self.model.select_best_move(self.model.curr_player)
                elif game_mode == 3:
                    if self.model.get_available_moves(self.model.curr_player):
                        AI_move = self.model.select_move_serious_AI()
                #if moves available - make the move and switch to human player.
                if AI_move:
                    self.model.make_move(AI_move[0], AI_move[1])
                    self.model.change_player(game_mode)
                else:
                       break

 

    def save_winner(self):
        """Saves the information (date, winner, scores) about the game in a text file
        """
        winner = self.model.check_winner()
        scores = self.model.keep_score()
        date = datetime.now()
        game_date = f'{date.year}-{date.month}-{date.day}  {date.hour}:{date.minute}'
        with open('Reversi_scores.txt', 'w') as f:
            print(f'Date: {game_date}, Winner: {winner}, Scores: {scores}', file = f)

    def end_game(self):
        #checks, displays and saves winner and scores of the game
        self.view.draw_board()
        player = self.model.check_winner()
        if player:
            self.view.display_winner(player)
        scores = self.model.keep_score()
        self.view.display_scores(scores)
        self.save_winner()
