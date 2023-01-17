import pandas as pd
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random
# import cars
import numpy as np
import itertools

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

    def check_availability(self, new_coordinates, car_dict):
        """Method that checks whether the proposed coordinates (input) are not taken by another car yet.
        It also checks that the car is not going of the board yet. Outputs boolean that is True when 
        the proposed coordinates are a possibility."""

        #Make set of car coordinates:
        set_new_coordinates= set(new_coordinates)

        #Check whether the car coordinates are not of the board yet:
        flat_coords = list(itertools.chain(*set_new_coordinates))

        mask = np.all(flat_coords) <= 6 & np.all(flat_coords) > 0
        if mask == False:
            return False
        
        #Loop through cars list:
        for car in car_dict.keys():
            #Make a set of the car coordinates:
            coords = set(car_dict[car][0])
            #Check whether there is overlap:
            overlap = set_new_coordinates.intersection(coords)
            #If there's overlap, stop:
            if overlap != set():
                return False
        #No overlap? Availibilty approved:
        return True

    def step(self, car, dictionary, direction = 1):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1). Outputs list of new coordinates.
        '''

        orientation = dictionary[car][2]
        coordinates = dictionary[car][0]
        updated_coordinates = []

        for coordinate in coordinates:
            coordinate = list(coordinate)

            if orientation == 'H':
                updated_x = coordinate[0] + direction
                updated_coordinate = (updated_x, coordinate[1])
                updated_coordinates.append(updated_coordinate)

            if orientation == 'V':
                updated_y = coordinate[1] + direction
                updated_coordinate = (coordinate[0], updated_y)
                updated_coordinates.append(updated_coordinate)
        
        return updated_coordinates
