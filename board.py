import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

class Cars():
    # create the rectangle for a single car
    def __init__(self, x_coord, y_coord, length):
        self.x = x_coord
        self.y = y_coord
        plt.Rectangle((self.x, self.y), 1, length)

class Board():
    # create grid with matplotlib
    
    def __init__(self, column = 6, row = 6):
        self.column = column
        self.row = row
        self.fig = plt.figure(figsize = [self.column, self.row])
        self.ax = self.fig.add_subplot(111)
        self.cars_list = []


    def create_board(self):
        # draw the grid
        
        for x in range(self.column + 1):
            self.ax.plot([x, x], [0, self.column], 'k')
        for y in range(self.row + 1):
            self.ax.plot([0, self.row], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.column + 1)
        self.ax.set_ylim(-1, self.row + 1)
        plt.show()

    def create_car(self):
        
        # get car info from csv and turn into df
        df = pd.read_csv('gameboards/Rushhour6x6_1.csv')
        print(df)
        
        # loop over dataframe and append each car in a list
        for row, column in df.iterrows():
            col = column[2]
            print(col)
            row = column[3]
            length = column[4]
            self.cars_list.append(Cars(col,row, length))

Board = Board()
# Board.create_board()
Board.create_car()
