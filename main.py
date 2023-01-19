# from code.classes import board
from code.classes  import plots
from code.algorithms import randomize
# import random
# import pandas as pd

filename = 'gameboards/Rushhour6x6_1.csv'

if __name__ == '__main__':

   random_algo = randomize.Random(filename)
   random_algo.run()
#    new_car_list = random_algo.new_cars_list
#    plot = plots.Plot_board()
#    plot.create_board()
#    plot.plot_dotted_cars(new_car_list)

    