import random
import pandas as pd
from code.classes import board
# from code.classes import car
from code.classes.car import Car
from code.classes  import plots
# from car import Car.step

class Random():
    '''
    Implementation of random algorithm 
    '''
    def __init__(self, filename):
        self.board = board.Board(filename)
        
        self.new_cars_list = []
        
        
    def run(self):
        self.board.df_to_object()
        self.new_cars_list = self.board.cars_list
        lst = []
        # print(self.new_cars_list)
        # move count
        move_count = 0
        while self.new_cars_list[-1].coordinates_list[0] != (5, 4):
            # for car in self.new_cars_list:
        
            # choose randomly from car dictionary
            random_car = random.choice(self.new_cars_list)
            # print(random_car)

            # choose direction randomly
            random_direction = random.choice([1, -1])
            
            # propose a random step:
            # random_car = Car()
            # print("---")
            # print(random_car.coordinates_list)
            random_car.step(random_direction)
            # print(random_car.updated_coordinates)

            #Check availablity:
            availability = self.board.check_availability(random_car)

            #If available, save the step in (updated) dictionary:
            if availability == True:
                # print('True')
                # self.new_coordinates = random_car.updated_coordinates
                random_car.coordinates_list = random_car.updated_coordinates
                # random_car.updated_coordinates = []
                # print(random_car.coordinates_list)
                # print("+++")
                move_count += 1
                plot = plots.Plot_board()
                plot.create_board()
                plot.plot_dotted_cars(self.new_cars_list)

                # self.new_cars_list = self.board.cars_list
            
            # Keep track of the game steps:
            lst.append([random_car.type, random_direction])

                    
            steps_df = pd.DataFrame(lst, columns = ["car", "move"])
                # print(steps_df.head())

                


