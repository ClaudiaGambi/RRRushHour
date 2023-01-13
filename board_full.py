import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import random

class Cars():

    def __init__(self, x_coord, y_coord, length, orientation, type):
        self.x = x_coord - 1
        self.y = y_coord - 1
        self.length = length
        self.orientation = orientation
        self.type = type

    def set(self, direction):
        if self.orientation == 'H':
            self.x += direction
        else:
            self.y += direction


class Board():
    def __init__(self, column = 6, row = 6):
        self.column = column
        self.row = row
        self.fig = plt.figure(figsize = [self.column, self.row])
        self.ax = self.fig.add_subplot(111)


    def create_board(self):
        for x in range(self.column + 1):
            self.ax.plot([x, x], [0, self.column], 'k')
        for y in range(self.row + 1):
            self.ax.plot([0, self.row], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.column + 1)
        self.ax.set_ylim(-1, self.row + 1)

        # maak array aan  van board o te bepalen waar auto's heen gaan

# if name == __main__():


Board = Board()
Board.create_board()
# Board.create_car()

cars_list = []
df = pd.read_csv('gameboards/Rushhour6x6_1.csv')
# print(df)
for row, column in df.iterrows():
    col = column[2]
    row = column[3]
    length = column[4]
    orientation = column[1]
    type = column[0]
    cars_list.append(Cars(col, row, length, orientation, type))

for car in cars_list:

    if car.orientation == 'H':
        Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = (random.random(), random.random(), random.random())))
        if car.type == 'X':
            Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = 'r' ))

    else:
        Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), 1, car.length, facecolor = (random.random(), random.random(), random.random())))
    car.set(1)
plt.gca().invert_yaxis()
plt.show()
