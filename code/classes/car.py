import random 
import pandas as pd 

class Car():
    '''
    This class initiates a car object. In this object attributes with the coordinates,
    length of car, orientation, identification, and color are created.

    In this class, the function step is created too. This function lets a car take a step.
    '''
    def __init__(self, coordinates_list, length, orientation, type, color):
        self.coordinates_list = coordinates_list
        self.length = length
        self.orientation = orientation

        # identification of car
        self.type = type
        self.color = color

    def step(self, direction = 1):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1). The function outputs new coordinates.
        '''

        self.updated_coordinates = []

        # if the car moves horizontally, add the direction to the current x coordinate
        if self.orientation == 'H':

            # loop over all coordinates the car is on
            for coordinate in self.coordinates_list:

                updated_x = coordinate[0] + direction
                updated_coordinate = (updated_x, coordinate[1])

                # update the coordinate list
                self.updated_coordinates.append(updated_coordinate)

        # if the car moves vertically, add the direction to the current y coordinate
        if self.orientation== 'V':

            # loop over all coordinates the car is on
            for coordinate in self.coordinates_list:
                updated_y = coordinate[1] + direction
                updated_coordinate = (coordinate[0], updated_y)

                # update the coordinate list
                self.updated_coordinates.append(updated_coordinate)
        
        

        
