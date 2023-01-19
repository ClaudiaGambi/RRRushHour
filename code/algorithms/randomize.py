import random
import pandas as pd
from code.classes import board
from code.classes  import plots


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
        
        # move count
        move_count = 0
        #(5,4)
        while self.new_cars_list[-1].coordinates_list[0] != (8,5 ):
            
        
            # choose randomly from car list
            random_car = random.choice(self.new_cars_list)
            

            # choose direction randomly
            random_direction = random.choice([1, -1])
            
            # propose a random step:
            # print(f'----{random_car.type}------')
            # print(random_car.coordinates_list)
            random_car.step(random_direction)

            # print(random_car.updated_coordinates)
            
            #Check availablity:
            availability = self.board.check_availability(random_car)

            #If available, save the step in (updated) dictionary:
            if availability == True:
                random_car.coordinates_list = random_car.updated_coordinates
                move_count += 1
                # plot = plots.Plot_board()
                # plot.create_board()
                # plot.plot_dotted_cars(self.new_cars_list)

            # Keep track of the game steps:
            lst.append([random_car.type, random_direction])
            # print(move_count)
        print(f'amount of steps till sollution: {move_count}')
        steps_df = pd.DataFrame(lst, columns = ["car", "move"])
        print(steps_df.head(20))

                


