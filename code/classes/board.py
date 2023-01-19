import pandas as pd
import random
from code.classes import car
import numpy as np
import itertools

class Board():
    '''
    The board class creates a grid that will function as the playing board.
    The default size of the board is 6x6, like it is for the first game.
    '''
    def __init__(self, file_name):
        self.column = int(file_name[19])
        self.row = int(file_name[19])
        self.file = file_name
        # verander eventueel als we algoritme implementeren 
        self.step_dict = {}
        self.cars_list = []


    def df_to_object(self):
        df = pd.read_csv(self.file)

        for row, column in df.iterrows():
            coord = (column[2],7 - column[3])
            length = column[4]
            orientation = column[1]
            car_type = column[0]
            list_coordinates = []

            #Check what is the red one:
            if car_type == 'X':
                color = 'r'
            
            #Assign random colors to the others:
            else:
                color = (random.random(), random.random(), random.random())
                
            #Check orientation:
            if orientation == "V":
                #Create list of coordinates that are covered by the car:
                for i in range(length):
                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    row = coord[1] - 1
                    coord = (coord[0], row)

            else:
                #Create list of coordinates that are covered by the car:
                for i in range(length):
                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    column = coord[0] + 1
                    coord = (column, coord[1])

            self.step_dict[car_type] = []
            self.cars_list.append(car.Car(list_coordinates, length, orientation, car_type, color))

    def check_availability(self, random_car):
        """Method that checks whether the proposed coordinates (input) are not taken by another car yet.
        It also checks that the car is not going of the board yet. Outputs boolean that is True when 
        the proposed coordinates are a possibility."""

        #Make set of car coordinates:
        
        set_new_coordinates= set(random_car.updated_coordinates)

        #Check whether the car coordinates are not of the board yet:
        flat_coords = list(itertools.chain(*set_new_coordinates))

        for number in flat_coords:
            if number > self.column or number < 1:
               
                return False

        count = 0
        #Loop through cars list:
        for car in self.cars_list:

            #Don't check with self:
            if car.type == random_car.type:
                
                continue
            
            #Count cars:
            count +=1
            #Make a set of the car coordinates:
            coords = set(car.coordinates_list)
            
            #Check whether there is overlap:
            overlap = set_new_coordinates.intersection(coords)
            
            
            #If there's no overlap, go to next car:
            if len(overlap) < 1:
                
                continue
        
            #Overlap? Availibilty not approved:
            
            return False
        
        return True

   