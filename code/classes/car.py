import random 
import pandas as pd 

class Car():
    '''
    This class transforms the values for each car into a class object.
    These values include coordinates, size , type and orientation of the car.
    '''

    def __init__(self, coordinates_list, length, orientation, type, color):
        self.coordinates_list = coordinates_list
        self.length = length
        self.orientation = orientation
        self.type = type
        self.color = color
        self.updated_coordinates = []

    
    def step(self, direction = 1):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1). Outputs new coordinates.
        '''
        
       
        if self.orientation == 'H':
            for coordinate in self.coordinates_list:

                updated_x = coordinate[0] + direction
                updated_coordinate = (updated_x, coordinate[1])
                self.updated_coordinates.append(updated_coordinate)

        if self.orientation== 'V':
            for coordinate in self.coordinates_list:
                updated_y = coordinate[1] + direction
                updated_coordinate = (coordinate[0], updated_y)
                self.updated_coordinates.append(updated_coordinate)
        
        

        
