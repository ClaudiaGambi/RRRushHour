# ----------------------- Import packages and code ----------------------------

import copy

# -----------------------------------------------------------------------------

class Breadth_first():
    """
    The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board). It evaluates each root node and adds
    their root nodes to the queue of nodes to be evaluated. When the evaluated node
    is the same as the solution board, the algorithm stops and returns the shortest
    root line to the solution.
    """
    def __init__(self, starting_board):
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.solution_found = False
        self.all_states_set = set()
        self.all_states_set.add(str(self.current_node.coordinates_list))
        self.generation = 1
        self.expanded_nodes = 0
        self.evaluated_nodes = 0

    def generate_nodes(self):
        """
        Method that creates instances of all the posible next generation nodes,
        using the current node as a 'parent'. The nodes are added to the queue list
        attribute. The board history (of each node) is saved in the board instance
        itself.
        """

        # Loop through cars on the parent board
        for car in self.current_node.cars_list:                                 
            
            # Loop over the two possible directions
            for direction in [-1, 1]:

                # Make a first step
                step_count = 1

                # Check for multiple steps in a certain direction
                distance = direction * step_count

                # Safe the new coordinates of the possible new move
                new_coords = car.propose_move(distance)

                # If there is a spot available for the car to be moved to on the current board
                while self.current_node.check_availability(car, new_coords) == True:

                    # Add 1 to count for possible next step
                    step_count +=1

                    carname = car.type

                    # Get index of car in current node
                    car_index = self.current_node.cars_list.index(car)

                    # If a possible move is proposed, make a copy of the parent board
                    child = copy.deepcopy(self.current_node)                        

                    # Update coordinates of car in child board with index of mother board
                    child.cars_list[car_index].update_coordinates(new_coords)
                    
                    # Update coordinates list of the child board
                    child.update_coordinates_board_state()                          
                
                    # Update board history of the child
                    child.update_board_history(carname, distance)                  

                    # Safe child board as string
                    child_coords = str(child.coordinates_list)

                    # Check whether child doesn't already exists in the all states set
                    if child_coords not in self.all_states_set:

                        #If not, add to queue and to all state set:
                        self.queue.append(child)
                        self.all_states_set.add(child_coords)

                        # Add to expanded nodes 
                        self.expanded_nodes += 1

                    # Add step to distance 
                    distance = direction * step_count

                    # Update new coordinates
                    new_coords = car.propose_move(distance)
                    
    def update_current_node(self):
        """
        Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute.
        """
        # Delete parent node
        self.queue.pop(0)

        # Save number of evaluated nodes
        self.evaluated_nodes += 1

        # Update what node to take as next parent node
        self.current_node = self.queue[0]
    
    def evaluate_node(self):
        """
        Method that checks whether the current board has the red car next to the exit.
        It uses the current node attribute and returns a boolean indicating whether the
        red car is on the exit coordinate, and so if the solution has been reached.
        """
        # Exit coordinates:
        exit = self.current_node.exit

        # Red car coordinates:
        red_car_coordinate = self.current_node.cars_list[-1].coordinates_list[0]
        
        # Check if the coordinates are the same
        if exit == red_car_coordinate:
            self.solution_found = True
        else:
            self.solution_found = False
    
    def run(self):
        """
        Method that runs the algorithm. It continues untill a solution has been
        found. Untill then, each node in the queue is evaluated and root nodes are 
        created. When the solution has been found, the board history of that board
        is returned, containing all the steps that have been taken to get there.
        """        
        # Continue untill a solution has been found
        while self.solution_found == False: 
        
            # Add child nodes to queue
            self.generate_nodes()

            # Check whether there's at least one node in the queue
            if len(self.queue) == 0:
                return print("No solution has been found.")

            # Select new node and update queue
            self.update_current_node()

            # Evaluate current node
            self.evaluate_node()

        # Resturn the steps that need to be taken to get to the bes answer
        return self.current_node.step_history