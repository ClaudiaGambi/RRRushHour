import tkinter as tk
class Board(tk.Frame):
    def __init__(self, parent, columns, rows, size = 32):
        self.columns = columns
        self.rows = rows
        self.size = size

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0,
        width = canvas_width, height = canvas_height, background = 'bisque')
        self.canvas.pack(side = 'top', fill = 'both', expand = True, padx = 2, pady = 2)

        self.canvas.bind('<Configure>', self.refresh)

if __name__ ==' __main__':
    root = tk.TK()
    board = Board(root)
    board.pack(side = 'top', fill = 'both', expand = True, padx = 4, pady = 4)
