import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import random

class Cars():
    '''
    This class transforms the values for each car into a class object.
    These values include coordinates, size , type and orientation of the car.
    '''
    def __init__(self, x_coord, y_coord, length, orientation, type):
        self.x = x_coord - 1
        self.y = y_coord - 1
        self.length = length
        self.orientation = orientation
        self.type = type

class Board():
    '''
    The board class creates a grid that will function as the playing board.
    The default size of the board is 6x6, like it is for the first game.
    '''
    def __init__(self, column = 6, row = 6):
        self.column = column
        self.row = row
        self.fig = plt.figure(figsize = [self.column, self.row])
        self.ax = self.fig.add_subplot(111)

    def create_board(self):
        # the k is for the lines!!!
        for x in range(self.column + 1):
            self.ax.plot([x, x], [0, self.column], 'k')
        for y in range(self.row + 1):
            self.ax.plot([0, self.row], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.column + 1)
        self.ax.set_ylim(-1, self.row + 1)

'''
Alles hieronder beter nog in class/objects/functie oid voor overzicht.
Dat werkte eerst niet want we kregen de error dat de Board class referenced
before assignment was.
'''


Board = Board()
Board.create_board()

cars_list = []

# load the data from the game into dataframe

# filenames als input in terminal geven
filename = 'Rushhour6x6_1.csv'
df = pd.read_csv(filename)
print(df)

# loop over the rows in the df and select the right values
for row, column in df.iterrows():
    col = column[2]
    row = column[3]
    length = column[4]
    orientation = column[1]
    type = column[0]

    # for each row (each car), make it into a Cars class and append this to the cars list
    cars_list.append(Cars(col, row, length, orientation, type))

# for each car in the car list, plot them in the board grid
for car in cars_list:

    # if the car moves horizontally, plot car in a rondom color
    if car.orientation == 'H':
        Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = (random.random(), random.random(), random.random())))

        # if car is type X, make the color red
        if car.type == 'X':
            Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = 'r' ))

    # if the car moves vertically, plot car in random color
    else:
        Board.ax.add_patch(mpatches.Rectangle((car.x, car.y), 1, car.length, facecolor = (random.random(), random.random(), random.random())))

# flip the board so it matches the game picture
plt.gca().invert_yaxis()

plt.show()
