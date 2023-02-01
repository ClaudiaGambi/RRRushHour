import random
import pandas as pd
#from code.classes import board
#from code.classes  import plots

class Random():
    '''
    This class initializes a Random search for a Rushhour game. As input is a starting
    board (Class: Board()) needed and the boardsize
    '''
    def __init__(self, board_size, starting_board):
        self.board = starting_board
        self.board_size = board_size
        self.new_cars_list = []
        self.steps_df = pd.DataFrame() 
        self.csv = None
        self.move_count = 0
        
    def run(self):
        
        self.new_cars_list = self.board.cars_list
    
        #exit = (self.board_size - 1 ,self.new_cars_list[-1].coordinates_list[0][1])
        exit = self.board.exit
        while self.new_cars_list[-1].coordinates_list[0] != exit:
            
            # choose randomly from car list
            random_car = random.choice(self.new_cars_list)
            

            # choose direction randomly
            random_direction = random.choice([1, -1])
            
            # propose a random step:
            new_coords = random_car.step(random_direction)

            
            #Check availablity:
            availability = self.board.check_availability(random_car, new_coords)

            #If available, save the step in (updated) dictionary:
            if availability == True:
                random_car.update_coordinates(new_coords)
                self.move_count += 1
                self.board.update_coordinates_board_state()
                # plot = plots.Plot_board()
                # plot.create_board()
                # plot.plot_dotted_cars(self.new_cars_list)
            

                # Keep track of the game steps:
                # lst.append([random_car.type, random_direction])
                
        # print(f'amount of steps till sollution: {move_count}')
        # df = pd.DataFrame(lst, columns = ["car", "move"])
        # self.steps_df = pd.concat([self.steps_df, df])

        
        
    

                


