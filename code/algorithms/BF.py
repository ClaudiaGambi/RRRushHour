import copy
import numpy as np
from code.classes import plots

class Breadth_first():
    """The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board). It evaluates each root node and adds
    their root nodes to the queue of nodes to be evaluated. When the evaluated node
    is the same as the solution board, the algorithm stops and returns the shortest
    root line to the solution."""

    def __init__(self, starting_board):
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.solution_found = False
        self.current_node.update_coordinates_board_state()
        self.current_board_coordinates_string = str(self.current_node.coordinates_list)
        print(self.current_board_coordinates_string)
        self.all_states_set = set()
        self.all_states_set.add(self.current_board_coordinates_string)
        self.generation = 1

    def generate_nodes(self):
        """Method that creates instances of all the posible next generation nodes,
        using the current node as a 'parent'. The nodes are added to the queue list
        attribute. The board history (of each node) is saved in the board instance
        itself."""
        lst = [-1,1]

        #1. 
        
        # Loop through the cars in the current node:
        for car in self.current_node.cars_list:
            i = self.current_node.cars_list.index(car)

            # Propose a move in both directions:
            for direction in lst:
                
                # Propose on the original board:
                car.step(direction)                                         # Car: updated coordinates bijgewerkt
                
                # Check availability in the board:
                availability = self.current_node.check_availability(car)    # Car: check updated coordinates with board cars   
                print(availability, direction)
                
                # If available, make a copy of the current board:
                if availability == True:
                    
                    #And make a copy of the updated board:
                    copy_ = copy.deepcopy(self.current_node)                # Kopie van aangepast board
                    
                    # And update board history of the copy:
                    copy_.update_board_history(car.type, direction)
                    
                    # And update coordinates list of the copy:
                    copy_.update_coordinates_board_state()                  # Update copy board car coordinates list

                    #Check whether the copy doesn't already exist:
                    # print(self.all_states_set)
                    if self.current_board_coordinates_string not in self.all_states_set:
                        #Update coordinates of the car:
                        print(f"Pre update: {car.coordinates_list}")
                        # loop over copy car
                        print("!!!!!!!!!!!!!!!!!!!!1")
                        print(copy_.cars_list[i])
                        copy_.cars_list[i].update_coordinates()                     # Car: updated coords >> coords_list
                        print(f"Post update: {car.coordinates_list}")

                        # Save current board coordinates list:
                        self.current_board_coordinates_string = str(copy_.coordinates_list) # Board: string of car coords
                        # Show copy plot:
                        copy_.array_plot(copy_.coordinates_list)
                        print(copy_.coordinates_list)
                        print(f"Length all states set: {len(self.all_states_set)}")
                        print(f"Child coords string: {self.current_board_coordinates_string}")
                        print(f'All strings: {self.all_states_set}')

                        # And add copy to queue:
                        self.queue.append(copy_)
                        print(f"Len queue: {len(self.queue)}\n {self.queue}")
                        
                        # And add copy to all states list:
                        self.all_states_set.add(self.current_board_coordinates_string)
    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

        print(f"{self.queue}")
        # Delete:
        self.queue.pop(0)
        #print(f"{self.queue}")
        # Update:
        self.current_node = self.queue[0]

        # print([str(b) for b in self.queue])

        # Update generation:
        old_generation = self.generation
        self.generation = len(self.current_node.step_history)
        # print("generation old", old_generation, "new: ", self.generation,)
        if old_generation != self.generation:
            print(f"\n Next generation: {self.generation} -----------------------------------------")
            # for board in self.queue:
            #     print(board)
            # import sys
            # sys.exit()
    
    def evaluate_node(self):
        """Method that checks whether the current board has the red car next to the exit.
        It uses the current node attribute and returns a boolean indicating whether the
        red car is on the exit coordinate, and so if the solution has been reached."""

        #Exit coordinates:
        exit = self.current_node.exit
        print(f"Exit: {exit}")

        #Red car coordinates:
        red_car_coordinate = self.current_node.cars_list[-1].coordinates_list[0]
        print(f"Red car coordinate: {red_car_coordinate}")

        #Are they equal?
        if exit == red_car_coordinate:
            self.solution_found = True
        else:
            self.solution_found = False
    
    def run(self):
        """Method that runs the algorithm. It continues untill a solution has been
        found. Untill then, each node in the queue is evaluated and root nodes are 
        created. When the solution has been found, the board history of that board
        is returned, containing all the steps that have been taken to get there."""
        
        # Continue untill a solution has been found:
        while self.solution_found == False: 
            print(f"\nNext board: {self.current_node} -----------------\n")

            # Evaluate current node:
            self.evaluate_node()
            print("evaluate")
        
            # Add baby nodes to queue:
            self.generate_nodes()
            print("generate nodes")

            # Check whether there's minimally one node in the queue:
            if len(self.queue) == 0:
                return print("No solution has been found.")

            # Select new node and update queue:
            self.update_current_node()
            print("update current node")

        return self.current_node.step_history