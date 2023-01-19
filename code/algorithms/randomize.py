import random
import pandas as pd
from classes import board
from classes.car import step 

class Random():
    '''
    Implementation of random algorithm 
    '''
    def __init__(self, filename):
        self.board = board.Board(filename)
        self.new_cars_list = []
        
        
    def run(self):
        self.board.df_to_object()
        lst = []
        for car in self.board.cars_list:
             #While not not solved:
            while car.type == 'X' and car.coordinates_list[0] != (5, 4):
   
                 # move count
                move_count = 0

                # choose randomly from car dictionary
                random_car = random.choice(self.board.cars_list)

                # choose direction randomly
                random_direction = random.choice([1, -1])
                
                # propose a random step:
                random_car.step(random_direction)

                #Check availablity:
                availability = self.board.check_availability(random_car)

                #If available, save the step in (updated) dictionary:
                if availability == True:
                    self.new_coordinates = random_car.updated_coordinates
                    random_car.coordinates_list = random_car.updated_coordinates
                    move_count += 1
                    
                
                # Keep track of the game steps:
                lst.append([random_car.type, random_direction])

                    
            steps_df = pd.DataFrame(lst, columns = ["car", "move"])
            print(steps_df.head())

                


