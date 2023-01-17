import board
import random
import pandas as pd
import plots

filename = 'gameboards/Rushhour6x6_1.csv'

if __name__ == '__main__':

    #Create starting board:
    Board = board.Board()
    Board.read_board_size(filename)
    
    # Board.board_in_array()
    Board.df_to_dict(filename)

    cars_dictionary = Board.cars_dict
    step_dictionary = Board.step_dict

    #Plot situation:
    plot = plots.Plot_board()
    plot.create_board()
    # plot.add_cars_in_plot(cars_dictionary)

    # #List to keep track of steps:
    # lst = []

    # #While not not solved:
    # while cars_dictionary['X'][0] != (5, 3):
    #     # move count
    #     move_count = 0

    #     # choose randomly from car dictionary
    #     random_car = random.choice(list(cars_dictionary.keys()))

    #     # choose direction randomly
    #     random_direction = random.choice([1, -1])
        
    #     # propose a random step:
    #     new_coordinates = Board.step(random_car, cars_dictionary, random_direction)

    #     #Check availablity:
    #     availability = Board.check_availability(new_coordinates, cars_dictionary)

    #     #If available, save the step in (updated) dictionary:
    #     if availability == True:
    #         cars_dictionary[random_car][0] = new_coordinates
    #         move_count += 1

    #         #Plot current situation:
    #         plot.add_cars_in_plot(cars_dictionary)
        
    #     # Keep track of the game steps:
    #     lst.append([random_car, random_direction])

            
    # steps_df = pd.DataFrame(lst, columns = ["car", "move"])
    # print(steps_df.head())

        


