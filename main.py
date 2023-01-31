from code.classes import board
from code.algorithms import randomize
from code.algorithms import BreadthFirst
from code.algorithms import BF_Blocking
# from code.classes import plots
# from code.algorithms import game
# from code.classes import visuals
import argparse
import matplotlib.pyplot as plt
import pandas as pd 
from code.algorithms import BF_NearExit 
from code.algorithms import A_Star




def main(input_file, algorithm, output_file):
   """
   This function takes the input from the argument parser, which are the filename and the 
   algorithm that de file needs to be run on. The algorithm is then called on the file
   accordingly. 
   """

   board_size = input_file.split('Rushhour')
   board_size = board_size[1].split('x')
   board_size = int(board_size[0])

   # Checks which algorithm is given as input
   if algorithm == 'randomize':
      # lst = []
      # moves_list = []
      # coordinates_list = []
      # total_moves = 0
      # # key = 0
      # board_dict = {}
      # for i in range(100):
         #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
         #add carslist to instance
      starting_board.df_to_object()
      #creates the random object 
      random_algo = randomize.Random(board_size, starting_board)
      

      # runs the experiment
      
      random_algo.run()
      
   elif algorithm == "BreadthFirst":
      
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()

      #Run algorithm:
      #breadth_first = BF_NearExit.BF_NearExit(starting_board)
      breadth_first = BreadthFirst.Breadth_first(starting_board)
      breadth_first.run()

      
      
      # while time.time() - start < 600:
      #    print(f'run: {n_runs}')
      #    subprocess.call(["python3", "code/algorithms/BreadthFirst.py"])
         
      #    n_runs += 1

      # print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      # print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      # print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")
      breadth_first.current_node.step_history.to_csv('output.csv', index =False)

   
   elif algorithm == "BF_Blocking":
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()
      
      # starting_board.blocking_number_calculator()

      #Run algorithm:
      best_first_bl = BF_Blocking.BF_Blocking(starting_board)
      best_first_bl.run()

      print(f'HISTORY{best_first_bl.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {best_first_bl.evaluated_nodes}")
      print(f"Number of expanded nodes: {best_first_bl.expanded_nodes}")
      best_first_bl.current_node.step_history.to_csv('output.csv', index =False)
   
   elif algorithm == "BF_NearExit":
      
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()
      
      # starting_board.blocking_number_calculator()

      #Run algorithm:
      best_first = BF_NearExit.BF_NearExit(starting_board)
      best_first.run()

      print(f'HISTORY{best_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {best_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {best_first.expanded_nodes}")
      best_first.current_node.step_history.to_csv('output.csv', index =False)

   

   elif algorithm == "Astar":

     #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()

      #create end board instance
      end_board = board.Board('gameboards/end_board4.csv', board_size)
      end_board.df_to_object()

      Astar = A_Star.A_star(end_board, starting_board)
      Astar.run()
      print(f'{Astar.current_node.step_history.head(30)}')
      Astar.current_node.step_history.to_csv('output.csv', index = False)
      # print()

   elif algorithm == "game":
      starting_board = board.Board(input_file, board_size)
      starting_board.df_to_object()
      df = pd.read_csv('steps.csv')

      game.game(starting_board, board_size)

   elif algorithm == "visual":
      starting_board = board.Board(input_file, board_size)
      starting_board.df_to_object()
      df = pd.read_csv('output.csv')


if __name__ == '__main__':
   """
   Creates argument parser with values it takes. 
   """

   # create parser
   parser = argparse.ArgumentParser(description = 'import dataframe with board values')

   # add arguments to parser

   parser.add_argument('output', help = 'output file (csv)')
   # parser.add_argument('output', help = 'output file (png)')
   parser.add_argument('input', help = 'input_file (csv')
   parser.add_argument('-algo', '--algorithm')

   # reads arguments from commandline
   args = parser.parse_args()

   # run main with arguments from parser
   main(args.input, args.algorithm, args.output)