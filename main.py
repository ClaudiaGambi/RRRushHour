from code.classes import board
from code.classes  import plots
from code.algorithms import randomize
import random
import pandas as pd

filename = 'gameboards/Rushhour6x6_1.csv'

if __name__ == '__main__':

    #Create starting board:
    Board = board.Board(filename)

     # create object of cars
    Board.df_to_object()

    
    step_dictionary = Board.step_dict

    #Plot situation:
    plot = plots.Plot_board()
    #plot.create_board()
    #plot.add_cars_in_plot(cars_dictionary)
    plot.plot_dotted_cars(cars_dictionary)

    #List to keep track of steps:
    


