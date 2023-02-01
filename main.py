
# ----------------------- Import packages and code ----------------------------

from code.algorithms import randomize
from code.algorithms import A_Star
from code.algorithms import BreadthFirst
from code.algorithms import BF_NearExit 
from code.algorithms import BF_Blocking
# from code.algorithms import game

from code.classes import board as brd
# from code.classes import plots
# from code.classes import visuals

import argparse
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import re
import csv

# -----------------------------------------------------------------------------

def main(algorithm, input_file, output_file1, output2):
   """
   This function takes the input from the argument parser, which are the
   filename and the algorithm that de file needs to be run on. The algorithm is
   then called on the file accordingly. 
   """
   
   # Extract the boardsize from the output file name:
   board_size = int(re.findall(r'\d+', input_file)[0])
   board_number = int(re.findall(r'\d+', input_file)[-1])

# ---------------------------------- Random ----------------------------------
   
   if algorithm == 'Random':
      
      # A list of the amount of steps taken untill the solution is found per run:
      move_counts_list = []

      # A dictionary that retains the occurence of each endboard state found:
      solution_boards_count = {}

      # The board instance with the highest occurence: 
      most_found_endstate = "Will be written over by board instances"

      # Run the experiment 100 times:
      # count = 0
      # for i in range(100):
         # count += 1
         # print(count)

      # Create starting board Board instance:
      starting_board = brd.Board(input_file, board_size)

      # Add carslist to instance:
      starting_board.df_to_object()

      # Creates the random algorithm instance:
      random_algo = randomize.Random(board_size, starting_board)

      #Run the experiment:
      random_algo.run()

      # Save the move count in a list (for creating a histogram plot):
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
   
      # Look at each car in the most found endstate:
      lst_total = []
      for car in most_found_endstate.cars_list:
         #  And save the needed attributes:
         coord = car.coordinates_list[0]
         col = coord[0]
         row = (most_found_endstate.board_size + 1) - coord[1] 
         lst_total.append([car.type, car.orientation, col, row, car.length])

      # Make csv of most found endstate (to be used in A*):
      new_board_df = pd.DataFrame(lst_total, columns = ['car', 'orientation', 'col', 'row', 'length'])
      new_board_df.to_csv(f'output/end_board{board_number}.csv', index = False)

      # Move count list:
      data = ",".join([str(i) for i in move_counts_list])
      with open(f"output/RandomOutput_Board{board_size}x{board_size}.csv", "w", newline = "") as fou:
         fou.write(data)

      # Print information about the amount of steps:
      mean = np.mean(move_counts_list)
      max_value = max(move_counts_list)
      min_value = min(move_counts_list)

      print("Amount of steps untill solution:")
      print(f"Mean: {mean}\nMax: {max_value}\nMin: {min_value}")

# ------------------------------ Breadth First -------------------------------

   elif algorithm == "BreadthFirst":
      
      # Create starting board Board instance:
      starting_board = brd.Board(input_file, board_size)
      
      # Add carslist to instance:
      starting_board.df_to_object()
      
      # Add board state to instance:
      starting_board.update_coordinates_board_state()

      #Run algorithm:
      breadth_first = BreadthFirst.Breadth_first(starting_board)
      breadth_first.run()

      # Print information about algorithm tree:
      print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")

      # Export the step history of the solution board to a csv file:
      breadth_first.current_node.step_history.to_csv('output.csv', index = False)

# --------------- Breadth First with heuristic: # blocking cars --------------

   elif algorithm == "BF_Blocking":
      
      # Create starting board Board instance:
      starting_board = brd.Board(input_file, board_size)
      
      # Add carslist to instance
      starting_board.df_to_object()
      
      # Add board state to instance
      starting_board.update_coordinates_board_state()

      # Run algorithm:
      breadth_first = BF_Blocking.BF_Blocking(starting_board)
      breadth_first.run()

      # Print information about algorithm tree:
      print(f'HISTORY{breadth_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {breadth_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {breadth_first.expanded_nodes}")

      # Export the step history of the solution board to a csv file:
      breadth_first.current_node.step_history.to_csv('output.csv', index =False)

# --------------- Breadth First with heuristic: distance to exit -------------

   elif algorithm == "BF_NearExit":
      
      # Create starting board Board instance:
      starting_board = brd.Board(input_file, board_size)
      
      # Add carslist to instance:
      starting_board.df_to_object()
      
      # Add board state to instance:
      starting_board.update_coordinates_board_state()

      # Run algorithm:
      best_first = BF_NearExit.BF_NearExit(starting_board)
      best_first.run()

      print(f'HISTORY{best_first.current_node.step_history.head(30)}')
      print(f"Number of evaluated nodes: {best_first.evaluated_nodes}")
      print(f"Number of expanded nodes: {best_first.expanded_nodes}")
      best_first.current_node.step_history.to_csv('output.csv', index =False)

      # Export the step history of the solution board to a csv file:
      best_first.current_node.step_history.to_csv('output.csv', index =False)

# --------------------------------- A* ---------------------------------------

   elif algorithm == "Astar":

      # Create starting board Board instance:
      starting_board = brd.Board(input_file, board_size)
      
      # Add carslist to instance:
      starting_board.df_to_object()
      
      # Add board state to instance:
      starting_board.update_coordinates_board_state()

      # Create end board instance:
      end_board = brd.Board('gameboards/end_board7.csv', board_size)
      end_board.df_to_object()

      # Run the algorithm:
      Astar = A_Star.A_star(end_board, starting_board)
      Astar.run()

      # Export the step history of the solution board to a csv file:
      Astar.current_node.step_history.to_csv('output.csv', index = False)
      print(Astar.expanded_nodes)
      print(Astar.evaluated_nodes)

# ---------------------------- Visualisation ---------------------------------

   elif algorithm == "Visual":


      starting_board = board.Board(input_file, board_size)
      starting_board.df_to_object()
      df = pd.read_csv('output.csv')

   elif algorithm == "plotHist":
      "Creates a histogram plot based on the input files and returns it as a png."

      # Bin colors:
      trafic_light = ["red", "orange", "green"]

      # Input:
      lsts = [output2, output_file1, input_file]

      for i in range(len(lsts)):
         
         # Define board number:
         board_size = int(re.findall(r'\d+', lsts[i])[0])

         # Read in file:
         file = open(lsts[i], "r")
         board = list(csv.reader(file, delimiter = ","))[0]
         file.close()

         # Convert strings to integers:
         for j in range(len(board)):
            board[j] = int(board[j])

         # Plot:
         plt.hist(board, alpha = 0.8, color = trafic_light[i], label= f'Board {board_size}x{board_size}')
      
      plt.legend(loc='upper right')
      plt.show()

# ------------------------ Interactive simulation ----------------------------

   elif algorithm == "game":
      starting_board = board.Board(input_file, board_size)
      starting_board.df_to_object()
      df = pd.read_csv(output_file1)
      print(df)

      visuals.Visual(starting_board, df, board_size)

# --------------------------- Argument parser --------------------------------

if __name__ == '__main__':
   """
   Creates argument parser with values it takes. 
   """

   # Create parser:
   parser = argparse.ArgumentParser(description = 'import dataframe with board values')

   # Add arguments to parser:
   parser.add_argument('-algo', '--algorithm', help = "fill in algoritm/mode")
   parser.add_argument('-i','--input', help = 'input_file (csv)')
   parser.add_argument('-o1', '--output1', help = 'output file1 (csv)')
   parser.add_argument('-o2', '--output2', help = '[output file2 (csv)]') #optional

   # Reads arguments from commandline:
   args = parser.parse_args()

   # Run main with arguments from parser:
   main(args.algorithm, args.input, args.output1, args.output2)