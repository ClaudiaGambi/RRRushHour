from code.classes  import plots
from code.algorithms import randomize
import argparse


def main(input_file, algorithm):
   """
   This function takes the input from the argument parser, which are the filename and the 
   algorithm that de file needs to be run on. The algorithm is then called on the file
   accordingly. 
   """
   #checks which algorithm is given as input
   if algorithm == 'randomize':

      #creates the random object 
      random_algo = randomize.Random(input_file)

      # runs the experiment
      random_algo.run()

      # plots the visualisation 
      plot = plots.Plot_board()
      plot.create_board()
      plot.plot_dotted_cars(random_algo.new_cars_list)

"""
ADD ARGUMENT PARSER 
"""

if __name__ == '__main__':
   """
   Creates argument parser with values it takes. 
   """

   # create parser
   parser = argparse.ArgumentParser(description = 'import dataframe with board values')

   # add arguments to parser
   parser.add_argument('input', help = 'input_file (csv')
   parser.add_argument('-algo', '--algorithm')

   # reads arguments from commandline
   args = parser.parse_args()

   # run main with arguments from parser
   main(args.input, args.algorithm)