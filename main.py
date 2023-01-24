from code.classes import board
from code.algorithms import randomize
from code.algorithms import BreadthFirst
from code.classes import plots
import argparse


def main(input_file, algorithm, output_file):
   """
   This function takes the input from the argument parser, which are the filename and the 
   algorithm that de file needs to be run on. The algorithm is then called on the file
   accordingly. 
   """

   board_size = input_file.split('Rushhour')
   print(board_size)
   board_size = board_size[1].split('x')
   board_size = int(board_size[0])

   # Checks which algorithm is given as input
   if algorithm == 'randomize':

      #creates the random object 
      random_algo = randomize.Random(input_file, board_size)
      

      # runs the experiment
      random_algo.run()

      # plots the visualisation 
      plot = plots.Plot_board(board_size)
      plot.create_board()
      plot.plot_cars(random_algo.new_cars_list)
   
   elif algorithm == "BreadthFirst":
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()

      #Run algorithm:
      bread_first = BreadthFirst.Breadth_first(starting_board)
      bread_first.run()

      print(f'HISTORY{bread_first.current_node.step_history.head(30)}')
      bread_first.current_node.step_history.to_csv('output.csv', index =False)


if __name__ == '__main__':
   """
   Creates argument parser with values it takes. 
   """

   # create parser
   parser = argparse.ArgumentParser(description = 'import dataframe with board values')

   # add arguments to parser

   parser.add_argument('output', help = 'output file (csv)')
   parser.add_argument('input', help = 'input_file (csv')
   parser.add_argument('-algo', '--algorithm')

   # reads arguments from commandline
   args = parser.parse_args()

   # run main with arguments from parser
   main(args.input, args.algorithm, args.output)