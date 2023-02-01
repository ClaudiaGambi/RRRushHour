
# ----------------------- Import packages and code ----------------------------

import random
import pandas as pd

# -----------------------------------------------------------------------------

class Random():
    """
    This class initializes a Random search for a Rushhour game. As input is a
    starting board in the form of a Board() instance needed.
    """

    def __init__(self, starting_board):

        self.board = starting_board
        self.steps_df = pd.DataFrame()
        self.move_count = 0
        
        
    def run(self):
        """
        Runs a random search algorithm untill a solution is found. This solution
        is stored in the board history of the input board. The move count, amount
        of moves taken, are returned.
        """
        
        # Keep on making random steps until the red car has reached the exit
        while self.board.cars_list[-1].coordinates_list[0] != self.board.exit:
            
            # Choose a random car on the board
            random_car = random.choice(self.board.cars_list)
            
            # Choose a random move of one step to the left or to the right
            random_move = random.choice([1, -1])
            
            # Propose a random move
            new_coords = random_car.propose_move(random_move)

            # Check the availablity of the proposed move
            availability = self.board.check_availability(random_car, new_coords)

            # If available, make the move for real
            if availability == True:

                # By updating the car coordinates
                random_car.update_coordinates(new_coords)

                # And by updating the board coordinates
                self.board.update_coordinates_board_state()

                # Finally, save the amount of steps taken
                self.move_count += 1

        
        
    

                


