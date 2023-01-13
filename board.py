import pandas as pd
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random
import cars

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
        self.cars_list = []

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
    def add_cars(self):

        df = pd.read_csv('gameboards/Rushhour6x6_1.csv')

        for row, column in df.iterrows():
            col = column[2]
            row = column[3]
            length = column[4]
            orientation = column[1]
            type = column[0]
            self.cars_list.append(cars.Cars(col, row, length, orientation, type))

        for car in self.cars_list:

            if car.orientation == 'H':
                self.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = (random.random(), random.random(), random.random())))
                if car.type == 'X':
                    self.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = 'r' ))

            else:
                self.ax.add_patch(mpatches.Rectangle((car.x, car.y), 1, car.length, facecolor = (random.random(), random.random(), random.random())))

        plt.gca().invert_yaxis()
        plt.show()

        car = random.choice(self.cars_list)
        cars.move(car, 1)
