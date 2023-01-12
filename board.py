import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

class Cars():
    def __init__(self, x_coord, y_coord, length):
        self.x = x_coord
        self.y = y_coord
        car = ((self.x, self.y), 1, length)

class Board():
    def __init__(self, column = 6, row = 6):
        self.column = column
        self.row = row
        self.fig = plt.figure(figsize = [self.column, self.row])
        self.ax = self.fig.add_subplot(111)
        self.cars_list = []


    def create_board(self):
        for x in range(self.column + 1):
            self.ax.plot([x, x], [0, self.column], 'k')
        for y in range(self.row + 1):
            self.ax.plot([0, self.row], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.column + 1)
        self.ax.set_ylim(-1, self.row + 1)

        for car in self.cars_list:
            self.ax.add_patch(plt.Rectangle())

        plt.show()

    def create_car(self):
        df = pd.read_csv('gameboards/Rushhour6x6_1.csv')
        print(df)
        for row, column in df.iterrows():
            col = column[2]
            print(col)
            row = column[3]
            length = column[4]
            self.cars_list.append(Cars(col,row, length))



Board = Board()
Board.create_board()
Board.create_car()
