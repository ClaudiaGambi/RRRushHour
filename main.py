from code.classes import board
from code.algorithms import randomize
from code.algorithms import BreadthFirst
from code.algorithms import BF_Blocking
from code.classes import plots
# from code.algorithms import game
# from code.classes import visuals
import argparse
import matplotlib.pyplot as plt
import pandas as pd 
from code.algorithms import BF
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
      lst = []
      # for i in range(100):
         #Create starting board Board instance:
      starting_board = board.Board(input_file, board_size)
         #add carslist to instance
      starting_board.df_to_object()
      #creates the random object 
      random_algo = randomize.Random(board_size, starting_board)
      

      # runs the experiment
      
      random_algo.run()
         
         # lst.append([i, random_algo.move_count])
         # df = pd.DataFrame(lst, columns = ['iterations', 'moves'])
      
      # df.plot(kind = 'barh', title = 'Random', ylabel = 'Iterations' , xlabel = 'Amount of moves', figsize = (20,18))
    
      # plt.show()
      # plt.savefig('histo_random_1.png')

      # plots the visualisation 
      plot = plots.Plot_board(board_size)
      plot.create_board()
      plot.plot_cars(random_algo.new_cars_list)


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

   # elif algorithm == "game":
   #    starting_board = board.Board(input_file, board_size)
   #    starting_board.df_to_object()
   #    df = pd.read_csv('steps.csv')

   #    game.game(starting_board, board_size)

   # elif algorithm == "visual":
   #    starting_board = board.Board(input_file, board_size)
   #    starting_board.df_to_object()
   #    df = pd.read_csv('output.csv')


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