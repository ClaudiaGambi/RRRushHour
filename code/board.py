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
        # self.fig = plt.figure(figsize = [self.column, self.row])
        # self.ax = self.fig.add_subplot(111)
        self.cars_dict = {}
        self.step_dict = {}

    def read_board_size(self, file_name):

        # get the size of board from filename
        return int(file_name[19])

    def df_to_dict(self, file_name):
        df = pd.read_csv(file_name)

        for row, column in df.iterrows():
            coord = (column[2],column[3])
            length = column[4]
            orientation = column[1]
            car_type = column[0]
            list_coordinates = []

            #Check orientation:
            if orientation == "V":
                #Create list of coordinates that are covered by the car:
                for i in range(length):
                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    new_y = coord[1] - 1
                    coord = (coord[0], new_y)

            else:
                #Create list of coordinates that are covered by the car:
                for i in range(length):
                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    new_x = coord[0] + 1
                    coord = (new_x, coord[1])

            # self.cars_list.append(cars.Cars(col, row, length, orientation, type))
            self.cars_dict[car_type] = [list_coordinates, length, orientation]

            self.step_dict[car_type] = []
        return self.cars_dict, self.step_dict

    # def add_cars(self):

        # self.df = pd.read_csv('gameboards/Rushhour6x6_1.csv')

        # for row, column in self.df.iterrows():
        #     col = column[2]
        #     row = column[3]
        #     length = column[4]
        #     orientation = column[1]
        #     type = column[0]
            # self.cars_list.append(cars.Cars(col, row, length, orientation, type))

        # for car in self.cars_list:

        #     if car.orientation == 'H':
        #         self.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = (random.random(), random.random(), random.random())))
        #         if car.type == 'X':
        #             self.ax.add_patch(mpatches.Rectangle((car.x, car.y), car.length, 1, facecolor = 'r' ))

        #     else:
        #         self.ax.add_patch(mpatches.Rectangle((car.x, car.y), 1, car.length, facecolor = (random.random(), random.random(), random.random())))

        # plt.gca().invert_yaxis()
        # plt.show()

    def check_availability(self, new_coordinates, car_dict):
        """Method that checks whether the proposed coordinates (input) are not taken by another car yet.
        It also checks that the car is not going of the board yet. Outputs boolean that is True when 
        the proposed coordinates are a possibility."""

        for car in car_dict.keys():
            #Check whether coordinates cars are not of the board:
            if new_coordinates != car_dict[car][0]:
                #Check whether the coordinates are not of the grid:
                if new_coordinates[0] <= 6 and new_coordinates[0] >= 0 and new_coordinates[1] <= 6 and new_coordinates[1] >= 0:
                    return True

        return False

    def step(self, car, dictionary, direction = 1):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1). Outputs new coordinates.
        '''

        orientation = dictionary[car][2]
        
        coordinates = dictionary[car][0]

        print(coordinates)

        if orientation == 'H':
            coordinates[0] += direction

        if orientation == 'V':
            coordinates[1] += direction

        return coordinates
