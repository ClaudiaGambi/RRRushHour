import random
import pandas as pd
from code.classes import board
from code.classes  import plots


class Random():
    '''
    Implementation of random algorithm 
    '''
    def __init__(self, filename, board_size):
        self.board = board.Board(filename, board_size)
        self.board_size = board_size
        self.new_cars_list = []
        
        
    def run(self):
        self.board.df_to_object()
        self.new_cars_list = self.board.cars_list
        lst = []
        
        # move count
        move_count = 0
       
        exit = (self.board_size - 1 ,self.new_cars_list[-1].coordinates_list[0][1])
        while self.new_cars_list[-1].coordinates_list[0] != exit:
            
        
            # choose randomly from car list
            random_car = random.choice(self.new_cars_list)
            

            # choose direction randomly
            random_direction = random.choice([1, -1])
            
            # propose a random step:
            # print(f'----{random_car.type}------')
            # print(random_car.coordinates_list)
            new_coords = random_car.step(random_direction)

            # print(random_car.updated_coordinates)
            
            #Check availablity:
            availability = self.board.check_availability(random_car, new_coords)

            #If available, save the step in (updated) dictionary:
            if availability == True:
                random_car.update_coordinates(new_coords)
                move_count += 1
                # plot = plots.Plot_board()
                # plot.create_board()
                # plot.plot_dotted_cars(self.new_cars_list)
                # print('++++True+++++')

            # Keep track of the game steps:
            lst.append([random_car.type, random_direction])
            # print(move_count)
        print(f'amount of steps till sollution: {move_count}')
        steps_df = pd.DataFrame(lst, columns = ["car", "move"])
        print(steps_df.head(20))

                


