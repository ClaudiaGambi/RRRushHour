
# ----------------------- Import packages and code ----------------------------

import pandas as pd
import random
import numpy as np
import itertools
import re

from code.classes import car

# -----------------------------------------------------------------------------

class Board():
    """
    This class initializes a Board object representing a Rushhour gameboard. To 
    initialize an instance a file with information about the location and
    attributes about the cars on the board is needed.
    """
    
    def __init__(self, file_name):
        
        self.file = file_name
        self.board_size = int(re.findall(r'\d+', file_name)[0])
        self.step_history = pd.DataFrame(columns = ["car", "move"])
        self.cars_list = []
        self.exit = ()
        self.coordinates_list = []
        
    def read_input_file(self):
        """
        Method to read the input file and convert all the relevant information
        to Class attributes.
        """

        # Read the csv file into a dataframe
        df = pd.read_csv(self.file)

        # Read the file row by row, each row contains information about one car
        # on the board
        for row, columns in df.iterrows():
            
            # For vertical cars this coordinate is trunck coordinate,
            # for horizontal cars this is the front coordinate
            car_coordinate = (columns[2], (self.board_size + 1) - columns[3])

            # Cars (length = 2) and trucks (length = 3) can be present
            car_length = columns[4]

            # The car can drive horizontally or vertically
            car_orientation = columns[1]

            # The cartype is unique for each car
            car_type = columns[0]

            # A list containing all the coordinates the car occupies
            car_coordinates_list = []

            # The car with the name 'X' should always be a red car
            if car_type == 'X':
                car_color = 'r'

                # The exit has the same row coordinate as the red car,
                # and is located at the side of the board
                self.exit = (self.board_size - 1, car_coordinate[1])
            
            # Assign random colors to the other cars
            else:
                car_color = (random.random(), random.random(), random.random())
                
            # Create list of coordinates that are covered by the car,
            # updating the coordinates (- or +) is dependent of the car orientation
            # (see Car.propose_move(move) method comments)
            if car_orientation == "V":

                # Repeat for the length of the car
                for i in range(car_length):

                    # Save current coordinate to the list
                    car_coordinates_list.append(car_coordinate)

                    # Update coordinate
                    row = car_coordinate[1] - 1
                    car_coordinate = (car_coordinate[0], row)

            else:
                # Repeat for the length of the car
                for i in range(car_length):

                    #Save coordinate to list
                    car_coordinates_list.append(car_coordinate)

                    #Update coordinate
                    column = car_coordinate[0] + 1
                    car_coordinate = (column, car_coordinate[1])

            # Make a Car() instance and add this car in the board
            self.cars_list.append(car.Car(car_coordinates_list, car_length, car_orientation, car_type, car_color))

    def check_availability(self, moving_car, proposed_coords):
        """
        Method that checks whether the proposed coordinates (input) are not
        taken by another car yet. It also checks that the car is not going of
        the board yet. Outputs boolean that is True when the proposed
        coordinates are a possibility.
        """

        # Make a list of all the loose unique coordinate numbers
        flat_coords = list(set(itertools.chain(*proposed_coords)))
        
        # Check whether each coordinate number is still on the board
        for number in flat_coords:
            if number > self.board_size or number < 1:
                # Return False if this is not the case
                return False
    
        # Check whether the proposed destination doesn't cause accidents with
        # any car on the board
        for car in self.cars_list:

            # Don't check with self
            if car.type == moving_car.type:
                continue
            
            # Check whether there is overlap
            overlap = set(proposed_coords).intersection(set(car.coordinates_list))
            
            # If there's no overlap, go to next car
            if len(overlap) < 1:
                continue
        
            # Overlap? Availibilty not approved
            return False
        
        # If there is no overlap and the car stays on the board return True
        return True

    def update_board_history(self, carName, move):
        """
        Method that updates the board history dataframe. As input it needs the
        carname (e.g. "A") and the move (e.g. -2). These are then in a new row
        added to the step history attribute.
        """

        # Make a new dataframe of one row
        new_row = pd.DataFrame({'car': [carName], 'move': [move]})

        # Add this to the old dataframe
        self.step_history = pd.concat([self.step_history, new_row],ignore_index = True)
        
    def update_coordinates_board_state(self):
        """
        Method to update the coordinates list of the board. Uses the current
        cars object in the cars list attribute of the board. Extracts the
        coordinates per car and adds those to the list.
        """

        # A list of lists with all the car coordinates in the board
        self.coordinates_list = []

        # Loop through the cars on the board and update the list of lists
        for car in self.cars_list:
            self.coordinates_list.append(car.coordinates_list)

    def distance_to_exit(self):
        """
        Method to calculate the distance (number of coordinates) between the red 
        car and the exit. The coordinates list and the exit attributes are
        herefore used. The distance is returned as an integer.
        """

        # From the coordinates list the red car is selected (last one on the list),
        # then the back coordinate is selected, then the column number is selected
        column_coordinate = self.coordinates_list[-1][0][0]

        # From the exit the column number is selected as well
        exit = self.exit[0]

        # Calculate the difference
        distance = exit - column_coordinate

        return distance

    def blocking_cars(self):
        """
        Method to calculate the number of cars that are blocking the red car from
        the exit. It uses the .. attribute. The number of cars in the way is
        returned as an integer.
        """

        # Select the red car Car() instance and the front coordinates
        red_car = self.cars_list[-1]
        red_coords_front = red_car.coordinates_list[1]

        # A set of the coordinates between the red car and the exit
        red_road = set()

        # Repeat for the number of coordinates between the red car and the exit
        for i in range(self.board_size - red_coords_front[0]):

            # Update coords and add to the road set
            coord = (red_coords_front[0] + i, red_coords_front[1])
            red_road.add(coord)

        # Create a set of all the coordinates occupied in the board
        loose_coords = set(itertools.chain(*self.coordinates_list))

        # The overlap between the two is equal to the blocking cars number
        blocking_number = len(loose_coords.intersection(red_road))
        
        return blocking_number

    def cost_star(self, end_cars_list):
        """
        Function that calculates the cost for a board instance based on
        distance from current spot to end destination and the amount of cars
        blocking the red car. The function returns the computed cost.
        """

        # The total distance is the calculated distance of each car summed
        distance_total = 0

        # Calculate the distance 
        for car in self.cars_list:
            
            # Get index of car
            i = self.cars_list.index(car)

            # Calculate distance with function in car class and sum up
            distance_total += car.distance_to_endstate(end_cars_list[i])

        # The number of cars that block the red car
        blocking_number = self.blocking_cars()

        # The A* cost is the blocking number and the total distance to endstate
        # summed
        cost = distance_total + blocking_number
        
        return cost 



                
                    


    