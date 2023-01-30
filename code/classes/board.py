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
        self.step_history = pd.DataFrame(columns = ["car", "move"])
        self.cars_list = []
        self.exit = ()
        self.coordinates_list = []
        self.distance_to_exit = 0
        self.distance_total = 0
        

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
            overlap = final_destination.intersection(coords)
            
            #If there's no overlap, go to next car:
            if len(overlap) < 1:
                continue
        
            #Overlap? Availibilty not approved:
            return False
        
        # if there is no overlap and the car stays on the board:
        return True

    def update_board_history(self, carName, move):
        new_row = pd.DataFrame({'car': [carName], 'move': [move]})
        self.step_history = pd.concat([self.step_history, new_row],ignore_index = True)
        
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

    def distance_calculator(self):

        #Red car > Back coordinate > Column coordinate:
        X_coord = self.coordinates_list[-1][0][0]

        #Exit > Column coordinate:
        exit = self.exit[0]

        #Distance:
        distance = exit - X_coord

        #Added for BF_NearExit algorithm:
        self.distance_to_exit = distance

    def blocking_number_calculator(self):

        # Select column coordinates between red car and the exit:
        highway = set()
        red_car = self.cars_list[-1]
        red_coords_front = red_car.coordinates_list[1]

        for i in range(self.board_size - red_coords_front[0]):
            coord = (red_coords_front[0] + i, red_coords_front[1])
            highway.add(coord)

        # Flatten coordinates list:
        loose_coords = set(itertools.chain(*self.coordinates_list))

        # Overlap:
        self.blocking_number = len(loose_coords.intersection(highway))



    def distance(self, car, end_cars_list):
        # self.distance_totale = 0

        i = self.cars_list.index(car)
        self.distance_total += car.distance_calculator_star(end_cars_list[i])
            # print(distance)
        
        return self.distance_total
    
    def cost_star(self, end_cars_list):
        """
        Function that calculates the cost for every board instance based on distance from current spot to end destination 
        and the amount of cars blocking the red car. The function returns the computed cost. 
        """

        #set variables for distance and the red car's way
        distance_total = 0
        highway = set()

        # loop over cars list
        for car in self.cars_list:
            
            # get index of car
            i = self.cars_list.index(car)

            # calculate distance with function in car class and sum up
            distance_total += car.distance_calculator_star(end_cars_list[i])
            
            # get red car
            red_car = self.cars_list[-1]

            # get fron coordinates of red car
            red_coords_front = red_car.coordinates_list[1]

            # loop over distance from red car to exit 
            for i in range(self.board_size - red_coords_front[0]):

                # get coordinates in front of red car and add to highway set
                coord = (red_coords_front[0] + i, red_coords_front[1])
                highway.add(coord)

        # Flatten coordinates list:
            loose_coords = set(itertools.chain(*self.coordinates_list))

        # Overlap:
            blokkage = len(loose_coords.intersection(highway))
        

        # compute cost
        cost = distance_total + blokkage 
        
        return cost 



                
                    


    