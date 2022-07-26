from model.game import Game
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController


model = Game(board_size=5)
view = GameConsoleView(model)
controller = GameController(view, model)
if controller.view.menu() == 1:
    controller.run_game_pvp()
else:
    controller.run_game_AI()
controller.save_winner()

    
