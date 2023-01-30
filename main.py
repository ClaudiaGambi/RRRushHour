from code.classes import board
from code.algorithms import randomize
from code.algorithms import BreadthFirst
from code.algorithms import BF_Blocking
from code.classes import plots
from code.algorithms import game
from code.classes import visuals
import argparse
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from code.algorithms import BF_NearExit 
from code.algorithms import A_Star
import time 
import subprocess 

def main(input_file, algorithm, output_file):
   """
   This function takes the input from the argument parser, which are the filename and the 
   algorithm that de file needs to be run on. The algorithm is then called on the file
   accordingly. 
   """

   board_size = input_file.split('Rushhour')
   board_size = board_size[1].split('x')
   board_size = int(board_size[0])

   # Checks which algorithm is given as input:
   if algorithm == 'randomize':
      
   #1. Create empty starting lists of values we want to save (per run):

      move_counts_list = []
      solution_boards_count = {}
      most_found_endstate = "Will be written over by board instances"

      count = 0

      # Run the experiment 100 times:
      for i in range(100):
         count += 1
         print(count)
   #2. Create an instance of the algorithm with the right starting board:
         
         # Create starting board Board instance:
         starting_board = board.Board(input_file, board_size)
         # Add carslist to instance:
         starting_board.df_to_object()
         # Creates the random algorithm instance:
         random_algo = randomize.Random(board_size, starting_board)
         
   #3. Run the experiment:
         
         random_algo.run()
   
   #4. Save the results:

         # Save all the move counts in a list (for creating a histogram plot):
         move_counts_list.append(random_algo.move_count)

         # Save occurance of each solution board:
         board_coords = str(random_algo.board.coordinates_list)

         if board_coords not in solution_boards_count.keys():
            solution_boards_count[board_coords] = 1
         
         else:
            solution_boards_count[board_coords] +=1

         # Apoint most found endstate:
         highest_occurence = max(solution_boards_count.values())

         if solution_boards_count[board_coords] == highest_occurence:
            most_found_endstate = random_algo.board
      
      print(solution_boards_count.values())
      
   #5. Return the most found endstate:
      
      lst_total = []
      for car in most_found_endstate.cars_list:
         coord = car.coordinates_list[0]
         col = coord[0]
         row = (most_found_endstate.board_size + 1) - coord[1] 
         lst_total.append([car.type, car.orientation, col, row, car.length])
         
      new_board_df = pd.DataFrame(lst_total, columns = ['car', 'orientation', 'col', 'row', 'length'])
      new_board_df.to_csv('gameboards/end_board1.csv', index = False)

   #6. Print values:

      gemiddelde = np.mean(move_counts_list)
      max_value = max(move_counts_list)
      min_value = min(move_counts_list)

      print(f'het gemiddelde is {gemiddelde}', f'maximum is {max_value} en minimum is {min_value}.')
      print(move_counts_list)
      
      # df.plot(kind = 'barh', title = 'Random', ylabel = 'Iterations' , xlabel = 'Amount of moves', figsize = (20,18))
    
      # plt.show()
      # plt.savefig('histo_random_1.png')

      # plots the visualisation 
      # plot = plots.Plot_board(board_size)
      # plot.create_board()
      # plot.plot_cars(random_algo.new_cars_list)


      # random_algo.steps_df.to_csv('output.csv', index = False)
   
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

      print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")
      breadth_first.current_node.step_history.to_csv('output.csv', index =False)
   
   elif algorithm == "BF_Blocking":
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()
      
      starting_board.blocking_number_calculator()

      #Run algorithm:
      breadth_first = BF_Blocking.BF_Blocking(starting_board)
      breadth_first.run()

      print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")
      breadth_first.current_node.step_history.to_csv('output.csv', index =False)
   
   elif algorithm == "BF_NearExit":
      #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()
      
      starting_board.blocking_number_calculator()

      #Run algorithm:
      breadth_first = BF_NearExit.BF_NearExit(starting_board)
      breadth_first.run()

      print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")
      breadth_first.current_node.step_history.to_csv('output.csv', index =False)



   elif algorithm == "Astar":

     #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
      #add carslist to instance
      starting_board.df_to_object()
      #add board state to instance
      starting_board.update_coordinates_board_state()

      #create end board instance
      end_board = board.Board('gameboards/end_board7.csv', board_size)
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