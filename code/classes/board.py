import pandas as pd
import random
from code.classes import car
import numpy as np
import itertools

class Board():
    '''
    The Board class has two functions: df_to_object and check_availability.
    The df_to_object reads the file containing the initial board state and 
    saves this in a Car object.

    The check availability function checks for every propsed move if this 
    move can be done: whether another car is in the way or wheter the car 
    will move of the board.
    '''
    def __init__(self, file_name, board_size):
        self.board_size = board_size
        self.file = file_name
        self.step_history = pd.DataFrame(columns = ["carName", "move"])
        self.cars_list = []
        self.exit = ()
        self.coordinates_list = []

    def df_to_object(self):

        # read the csv file into a dataframe
        df = pd.read_csv(self.file)

        for row, column in df.iterrows():
            coord = (column[2], (self.board_size + 1) - column[3])
            length = column[4]
            orientation = column[1]
            car_type = column[0]
            list_coordinates = []

            #Check what is the red one:
            if car_type == 'X':
                color = 'r'
                self.exit = (self.board_size - 1, coord[1])
            
            #Assign random colors to the others:
            else:
                color = (random.random(), random.random(), random.random())
                
            #Check orientation:
            if orientation == "V":

                #Create list of coordinates that are covered by the car:
                #loop over the length of the car to append each taken coordinate to the coordinates list
                for i in range(length):

                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    row = coord[1] - 1
                    coord = (coord[0], row)

            else:
                #Create list of coordinates that are covered by the car:
                #loop over the length of the car to append each taken coordinate to the coordinates list
                for i in range(length):

                    #Save coordinate to list:
                    list_coordinates.append(coord)

                    #Update coordinate:
                    column = coord[0] + 1
                    coord = (column, coord[1])

            self.cars_list.append(car.Car(list_coordinates, length, orientation, car_type, color))

    def check_availability(self, moving_car, new_coords):
        """
        Method that checks whether the proposed coordinates (input) are not taken by another car yet.
        It also checks that the car is not going of the board yet. Outputs boolean that is True when 
        the proposed coordinates are a possibility.
        """
        
        # #1. Define the route the car wants to drive: ------------------------------------------------

        # car_current_spot = list(moving_car.coordinates_list)
        # orientation = moving_car.orientation

        # # Amount of steps:
        # if orientation == "V":
        #     steps = new_coords[0][1] - car_current_spot[0][1]
        # else:
        #     steps = new_coords[0][0] - car_current_spot[0][0]

        # # Travel directions (for loop):
        # travel_directions = list()
        # for i in range(1, abs(steps)+1):

        #     # Move to the right:
        #     if abs(steps) == steps:
        #         travel_directions.append(i)

        #     # Move to the left:
        #     else:
        #         travel_directions.append(0-i)

        # # Coordinates the car needs to pass:
        # proposed_route = set()
        # for i in travel_directions:
        #     if orientation == "V":
        #         new_coord = (car_current_spot[-1][0], car_current_spot[-1][1] + i)
        #         proposed_route.add(new_coord)
        #     else:
        #         new_coord = (car_current_spot[-1][0] + i, car_current_spot[-1][1])
        #         proposed_route.add(new_coord)

        #2. Check whether the car stays on the board: -----------------------------------------------

        final_destination = set(new_coords)

        # Check whether the car coordinates are not of the board yet: -------------------------------
        flat_coords = list(itertools.chain(*final_destination))

        for number in flat_coords:
            if number > self.board_size or number < 1:
                return False
    
        #3. Check whether the proposed route doesn't generate driving accidents with any car on the board:

        #Loop through cars list:
        for car in self.cars_list:

            #Don't check with self:
            if car.type == moving_car.type:
                continue
            
            #Make a set of the car coordinates:
            coords = set(car.coordinates_list)
            
            #Check whether there is overlap:
            overlap = proposed_route.intersection(coords)
            
            #If there's no overlap, go to next car:
            if len(overlap) < 1:
                continue
        
            #Overlap? Availibilty not approved:
            return False
        
        # if there is no overlap and the car stays on the board:
        return True

    def update_board_history(self, carName, move):
        new_row = pd.DataFrame({'carName': [carName], 'move': [move]})
        self.step_history = pd.concat([self.step_history, new_row], ignore_index=True)

    def update_coordinates_board_state(self):
        """
        Method to update the coordinates list of the board. Uses the current
        cars object in the cars list attribute of the board. Extracts the
        coordinates per car and adds those to the list.
        """
        self.coordinates_list = []
        for car in self.cars_list:
            self.coordinates_list.append(car.coordinates_list)


    def array_plot(self, coordinates_list):
        """
        An easy 'plot' consistng of an arry to help debugging
        """
        array_board = np.zeros((self.board_size, self.board_size))
        count = 0
        for coordinate in coordinates_list:
            count += 1

            for coord in coordinate:
                column = coord[0]-1
                row = coord[1]-1
                array_board[row][column] = count
        print(f"\n {array_board} \n")
