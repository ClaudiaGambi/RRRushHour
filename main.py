from code.classes import board
from code.algorithms import randomize
from code.algorithms import BreadthFirst
from code.algorithms import BF_Blocking
from code.algorithms import BF_NearExit 
from code.algorithms import A_Star
# from code.classes import plots
# from code.algorithms import game
# from code.classes import visuals
import argparse
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import re
import csv



def main(input_file, algorithm, output_file1, output2):
   """
   This function takes the input from the argument parser, which are the filename and the 
   algorithm that de file needs to be run on. The algorithm is then called on the file
   accordingly. 
   """
   
   # Extract the boardsize from the output file name:
   board_size = int(re.findall(r'\d+', input_file)[0])
   board_number = board_size = int(re.findall(r'\d+', input_file)[-1])

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
      
      #5. Return csv's:

      # Most found endstate:
      lst_total = []
      for car in most_found_endstate.cars_list:
         coord = car.coordinates_list[0]
         col = coord[0]
         row = (most_found_endstate.board_size + 1) - coord[1] 
         lst_total.append([car.type, car.orientation, col, row, car.length])

      new_board_df = pd.DataFrame(lst_total, columns = ['car', 'orientation', 'col', 'row', 'length'])
      new_board_df.to_csv(f'output/end_board{board_number}.csv', index = False)

      # Move count list:
      data = ",".join([str(i) for i in move_counts_list])
      with open(f"output/RandomOutput_Board{board_size}x{board_size}.csv", "w", newline = "") as fou:
         fou.write(data)

      #6. Print values:

      mean = np.mean(move_counts_list)
      max_value = max(move_counts_list)
      min_value = min(move_counts_list)

      print("Amount of steps untill solution:")
      print(f"Mean: {mean}\nMax: {max_value}\nMin: {min_value}")

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
      
      # starting_board.blocking_number_calculator()

      #Run algorithm:
      best_first = BF_NearExit.BF_NearExit(starting_board)
      best_first.run()

      # print(f'HISTORY{best_first.current_node.step_history.head(30)}')
      # print(f"Number of evaluated nodes: {best_first.evaluated_nodes}")
      # print(f"Number of expanded nodes: {best_first.expanded_nodes}")
      # best_first.current_node.step_history.to_csv('output.csv', index =False)

   

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

   # Create parser:
   parser = argparse.ArgumentParser(description = 'import dataframe with board values')

   # Add arguments to parser:
   parser.add_argument('input', help = 'input_file (csv')
   parser.add_argument('-algo', '--algorithm')
   parser.add_argument('output1', help = 'output file1 (csv)')
   parser.add_argument('output2', help = 'output file2 (csv)')

   # Reads arguments from commandline:
   args = parser.parse_args()

   # Run main with arguments from parser:
   main(args.input, args.algorithm, args.output1, args.output2)