from model.game import Game
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController


model = Game(board_size=6)
view = GameConsoleView(model)
controller = GameController(view, model)
game_mode = controller.view.menu()
if  game_mode == 1:
    controller.run_game_pvp()
else:
    controller.run_game_simple_AI()

controller.end_game()

    
