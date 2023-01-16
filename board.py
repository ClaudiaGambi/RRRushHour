import pandas as pd
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random
# import cars
import numpy as np

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
        self.cars_dict = {}
        self.step_dict = {}

    def read_board_size(self, file_name):

        # get the size of board from filename
        return int(file_name[19])

    def df_to_dict(self, file_name):
        df = pd.read_csv(file_name)

        for row, column in df.iterrows():
            x_coord = column[2]
            y_coord = column[3]
            length = column[4]
            orientation = column[1]
            car_type = column[0]

            # self.cars_list.append(cars.Cars(col, row, length, orientation, type))
            self.cars_dict[car_type] = [(x_coord, y_coord), length, orientation]

            self.step_dict[car_type] = []
        return self.cars_dict, self.step_dict


    

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


    def add_cars(self):

        self.df = pd.read_csv('gameboards/Rushhour6x6_1.csv')

        for row, column in self.df.iterrows():
            col = column[2]
            row = column[3]
            length = column[4]
            orientation = column[1]
            type = column[0]
            # self.cars_list.append(cars.Cars(col, row, length, orientation, type))

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


    def check_availability(self, new_coordinates, car_dict):

        for car in car_dict:
            if new_coordinates != car[0]:
                return True

        return False




    # def board_in_array(self, df, filename):
    #     '''
    #     Create an array with the spots where the cars are
    #     '''

    #     # zeros matrix
    #     grid_matrix = np.zeros((size, size))

    #     # loop over df to get coordinates for zeros matrix
    #     for index, row in df.iterrows():

    #         # Start coordinates:
    #         x_co = row[3] - 1
    #         y_co = row[2] - 1
            
    #         # Vertical cars:
    #         if row[1] == 'V':
    #             for i in range(row[4]):
    #                 # Save coordinate:
    #                 grid_matrix[x_co][y_co] = 1
    #                 # Next coordinate:
    #                 x_co += 1
            
    #         # Horizontal cars:
    #         else:
    #             for i in range(row[4]):
    #                 # Save coordinate:
    #                 grid_matrix[x_co][y_co] = 1
    #                 # Next coordinate:
    #                 y_co += 1
    

file_name = 'gameboards/Rushhour6x6_1.csv'
bord = Board()

dict = bord.df_to_dict(file_name)

print(dict)