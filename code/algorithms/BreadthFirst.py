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
        self.current_board_coordinates_string = str(starting_board.coordinates_list)
        self.all_states_set = set()
        self.generation = 0

    def generate_nodes(self):
        """Method that creates instances of all the posible next generation nodes,
        using the current node as a 'parent'. The nodes are added to the queue list
        attribute. The board history (of each node) is saved in the board instance
        itself."""

        # Loop through the cars in the current node:
        for car in self.current_node.cars_list:
            # Propose a move in both directions:
            for direction in [-1,1]:
                #print(direction)
                # Propose a move:
                car.step(direction)
                # Check availability in the board:
                availability = self.current_node.check_availability(car)
                # print(availability, direction)
                # If available, make a copy of the current board:
                if availability == True:

                    #Update coordinates of the car:
                    car.update_coordinates()

                    #And make a copy of the updated board:
                    copy_ = copy.deepcopy(self.current_node)

                    # And update board history of the copy:
                    copy_.update_board_history(car.type, direction)

                    # test easy array plot
                    # copy_.array_plot(copy_.coordinates_list)

                    # And update coordinates list of the copy:
                    copy_.update_coordinates_board_state()

                    # test easy array plot
                    copy_.array_plot(copy_.coordinates_list)

                    # Update current board coordinates list:
                    self.current_board_coordinates_string = str(copy_.coordinates_list)

                    # print(len(self.all_states_set))
                    #Check whether the copy doesn't already exist:
                    # print(self.all_states_set)
                    if self.current_board_coordinates_string not in self.all_states_set:
                        
                        # And add copy to queue:
                        self.queue.append(copy_)

                        # print(f"Len queue: {len(self.queue)}")
                        # And add copy to all states list:
                        self.all_states_set.add(self.current_board_coordinates_string)

                    #!!!!!!!!!!!!!!!!!! --> 
                    car.update_coordinates()
                
                car.step(-direction)
                

    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""
        # Delete:
        self.queue.pop(0)

        # print(f'LEN QUEUE {len(self.queue)}')
        # for i in range(len(self.queue)):
            # print(f'QUEUE NUMBER {i} {self.queue[i]}')

        # Update:
        self.current_node = self.queue[0]

        # print([str(b) for b in self.queue])

        # Update generation:
        old_generation = self.generation
        self.generation = len(self.current_node.step_history)
        # print("generation old", old_generation, "new: ", self.generation,)
        if old_generation != self.generation:
            print(f"Next generation: {self.generation}")
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

        #Red car coordinates:
        red_car_coordinate = self.current_node.cars_list[-1].coordinates_list[0]
        #print(red_car_coordinate)

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
        count = 0
        # Continue untill a solution has been found:
        while self.solution_found == False: 
        # for i in range(5):
            count+=1
            #print(f"Round {count}")


            # Add baby nodes to queue:
            self.generate_nodes()
            # print(len(self.queue))
            # Check whether there's minimally one node in the queue:
            if len(self.queue) <= 1:
                
                return print("No solution has been found.")

            # Select new node and update queue:
            self.update_current_node()

            # Evaluate current node:
            self.evaluate_node()

        return self.current_node.step_history