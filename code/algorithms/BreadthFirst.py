import copy
import numpy as np

class Breadth_first():
    """The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board). It evaluates each root node and adds
    their root nodes to the queue of nodes to be evaluated. When the evaluated node
    is the same as the solution board, the algorithm stops and returns the shortest
    root line to the solution."""

    def __init__(self, starting_board):
        self.current_node = starting_board

        # KLEINERE REPRESENTATIE VERZINNEN: NIET CARS INSTANCES IN BOARD INSTANCE OPSLAAN
        self.queue = [copy.deepcopy(starting_board)]
        self.solution_found = False
        #closed_list
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

        #1. Look at each possible move (on the parent board):
        for car in self.current_node.cars_list:                                 # Loop through cars on the parent board
            
            
            for direction in [-1, 1]:
                count = 0
                distance = direction * count
                new_coords = car.step(distance)

                while self.current_node.check_availability(car, new_coords) == True:
                    count +=1
                   

                    # print(count)
                    
                    # print(new_coords)  
                                                # Propose a move on the parent board

                    # new_coords = car.updated_coordinates
                    carname = car.type
                    # print(carname)

                    # get index of car in current node
                    i = self.current_node.cars_list.index(car)

                    # print(availability)
                    # Check availability on the parent board

            #2. If a possible move is proposed, make a copy of the parent board:
                    child = copy.deepcopy(self.current_node)                        # Make a copy of the parent board

        #3. Adjust child board with the proposed move:
        # update coordinates of car in child board with index of mother board
                    # print(f'before: {child.cars_list[i].coordinates_list}')
                    child.cars_list[i].update_coordinates(new_coords)
                    # print(f'after:{child.cars_list[i].coordinates_list}')
                    
                    child.update_coordinates_board_state()                          # Update coordinates list of the child
                
                    child.update_board_history(carname, distance)                  # Update board history of the child

                    child_coords = str(child.coordinates_list)

                    

        #4. Check whether child doesn't already exists in the all states set:

                    if child_coords not in self.all_states_set:

        #5. If not, add to queue and to all state set:

                        self.queue.append(child)

                        self.all_states_set.add(child_coords)

                        # child.array_plot(child.coordinates_list)                    # Show array of the board

                        self.expanded_nodes += 1

                    distance = direction * count
                    new_coords = car.step(distance)
                    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

       
        # Delete:
        self.queue.pop(0)

        #Save number of evaluated nodes:
        self.evaluated_nodes += 1

        # Update:
        self.current_node = self.queue[0]

        # Update generation:
        # old_generation = self.generation
        # self.generation = len(self.current_node.step_history)
        
        # if old_generation != self.generation:
        #     print(f"\nNext generation: {self.generation} -------------------------------\n")
    
    def evaluate_node(self):
        """Method that checks whether the current board has the red car next to the exit.
        It uses the current node attribute and returns a boolean indicating whether the
        red car is on the exit coordinate, and so if the solution has been reached."""

        #Exit coordinates:
        exit = self.current_node.exit
        # print(exit)

        #Red car coordinates:
        red_car_coordinate = self.current_node.cars_list[-1].coordinates_list[0]
        # print(red_car_coordinate)
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
        
        # self.current_node.array_plot(self.current_node.coordinates_list)
        

        # Continue untill a solution has been found:
        while self.solution_found == False: 
        
            # Add baby nodes to queue:
            self.generate_nodes()

            # Check whether there's minimally one node in the queue:
            if len(self.queue) == 0:
                return print("No solution has been found.")

            # Select new node and update queue:
            self.update_current_node()

            # Evaluate current node:
            self.evaluate_node()

        return self.current_node.step_history