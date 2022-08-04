# import tkinter as tk
# from tkinter import scrolledtext
# from model.game import Game
# from view.game_console_view import GameConsoleView
# from controller.game_controller import GameController
# model = Game(board_size=8)
# view = GameConsoleView(model)
# controller = GameController(view, model)

# controller.run_game()
# controller.end_game()
# class ReversiGUI:
#     def __init__(self, game, playerX, playerO):
#         self.model = Game(board_size=8)
#         self.view = GameConsoleView(model)
#         self.controller = GameController(view, model)
#         self.playerX = playerX
#         self.playerO = playerO
#         self.offset = 3
#         self.cell_size = 40

#         window = tk.Tk()
#         window.wm_title("Reversi")
#         window.lift()
#         window.attributes("-topmost", True)
#         self.window = window
#         self.canvas = Canvas(window,height = self.cell_size * self.height + self.offset,width = self.cell_size * self.width + self.offset)
#         self.move_label = Label(window)
#         self.score_label = Label(window)
#         self.text = scrolledtext.ScrolledText(root, width=70, height=10)
#         self.move_label.pack(side="top")
#         self.score_label.pack(side="top")
#         self.canvas.pack()
#         self.text.pack()
#         self.draw_board()
