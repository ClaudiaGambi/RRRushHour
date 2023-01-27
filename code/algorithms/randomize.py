import random
import pandas as pd
from code.classes import board
from code.classes  import plots



class Random():
    '''
    Implementation of random algorithm 
    '''
    def __init__(self, board_size, starting_board):
        self.board = starting_board
        self.board_size = board_size
        self.new_cars_list = []
        self.steps_df = pd.DataFrame()
        self.new_board_df = pd.DataFrame() 
        self.csv = None

        
        
    def run(self):

        
        self.new_cars_list = self.board.cars_list
        lst = []
        lst_total = []
        
        # move count
        move_count = 0
    
        exit = (self.board_size - 1 ,self.new_cars_list[-1].coordinates_list[0][1])
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
                move_count += 1
                # plot = plots.Plot_board()
                # plot.create_board()
                # plot.plot_dotted_cars(self.new_cars_list)
            

                # Keep track of the game steps:
                lst.append([random_car.type, random_direction])
                
        print(f'amount of steps till sollution: {move_count}')
        df = pd.DataFrame(lst, columns = ["car", "move"])
        self.steps_df = pd.concat([self.steps_df, df])

        for car in self.new_cars_list:
            coord = car.coordinates_list[0]
            col = coord[0]
            row = (self.board_size + 1) - coord[1] 
            lst_total.append([car.type, car.orientation, col, row, car.length])
        new_board_df = pd.DataFrame(lst_total, columns = ['car', 'orientation', 'col', 'row', 'length'])
        self.new_board_df = pd.concat([self.new_board_df, new_board_df])
        
        self.new_board_df.to_csv('gameboards/end_board7.csv', index = False)
        
    

                


