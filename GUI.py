import tkinter as tk
from tkinter import ttk
from model.game import Game
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from view.game_view import GameView
from model.game import Game
from datetime import datetime

def select_gm(option):
    return int(option)


model = Game(board_size=5)
view = GameConsoleView(model)
controller = GameController(view, model)

# start_game = controller.run_game()
# controller.end_game()


root = tk.Tk()
root.title('Reversi Game')
window_width = 300
window_height = 450
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
greeting = tk.Label(text='Hello, Player. Welcome to Reversi\n\nSelect game mode below: ',\
    foreground="yellow", background="purple", width=30, height = 20)
greeting.pack()
gm_button1 = ttk.Button(root,text='Player vs Player', command=lambda: select_gm(1)).pack()
gm_button2 = ttk.Button(root,text='Player vs Computer. Easy', command=lambda: select_gm(2)).pack()
gm_button3 = ttk.Button(root,text='Player vs Tought AI. Hardcore', command=lambda: select_gm(3)).pack()
root.mainloop()


