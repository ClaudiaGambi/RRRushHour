# ----------------------- Import packages and code ----------------------------
import copy
from code.algorithms import BreadthFirst
from queue import PriorityQueue
from typing import Any
from dataclasses import dataclass, field
import copy 
# -----------------------------------------------------------------------------

@dataclass(order=True)
class PrioritizedItem:
    """
    Initialize priority queue.
    """
    priority: int 
    item: Any = field(compare=False)

class BF_NearExit(BreadthFirst.Breadth_first):
    """
    The Breadth First Near Exit inherits from the Breadth first algorithm.
    On top of regular Breadth First, Near Exit checks the distance between
    the red car and the exist. Based on this information certain boards are 
    prioritized in the queue.
    """
    def __init__(self,starting_board):
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.queue = PriorityQueue()
        self.queue.put(PrioritizedItem(self.current_node.distance_calculator(), self.current_node))
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
        attribute according to the distance of the red car to the exit. 
        The board history (of each node) is saved in the board instance itself.
        """
        # Look at each possible move (on the parent board):
        for car in self.current_node.cars_list:                                
            
            # Loop over the two possible directions
            for direction in [-1, 1]:

                # Make a first step
                count = 1

                # Check for multiple steps in a certain direction
                distance = direction * count

                # Safe the new coordinates of the possible new move
                new_coords = car.step(distance)  

                # If there is a spot available for the car to be moved to on the current board
                while self.current_node.check_availability(car, new_coords) == True:
                    
                    # Add 1 to count for possible next step
                    count +=1
                   
                    carname = car.type

                    # get index of car in current node
                    car_index = self.current_node.cars_list.index(car)

                    # If a possible move is proposed, make a copy of the parent board
                    child = copy.deepcopy(self.current_node)

                    # update coordinates of car in child board with index of mother board
                    child.cars_list[car_index].update_coordinates(new_coords)
                    
                    # Update coordinates list of the child board
                    child.update_coordinates_board_state()              
                
                    # Safe child board as string
                    child.update_board_history(carname, distance)            

                    # Check whether child doesn't already exists in the all states set:
                    child_coords = str(child.coordinates_list)

                    # Check whether child doesn't already exists in the all states set:
                    if child_coords not in self.all_states_set:

                        # Based on the total distance to end state, the queue is ordered
                        # For this child, the total distance is computed
                        # Based on that value the child is put in a certain spot in the queue
                        self.queue.put(PrioritizedItem(child.distance_calculator(), child))

                        # Add to all state set
                        self.all_states_set.add(child_coords)

                        # Add to expanded nodes
                        self.expanded_nodes += 1

                    # Add step to distance
                    distance = direction * count

                    # Update new coordinates
                    new_coords = car.step(distance)

    def update_current_node(self):
        """
        Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute.
        """
        # Save number of evaluated nodes
        self.evaluated_nodes += 1

        # Update current node
        self.current_node = self.queue.get().item

    def run(self):
        """
        Method that runs the algorithm. It continues untill a solution has been
        found. Untill then, each node in the queue is evaluated and root nodes are 
        created. When the solution has been found, the board history of that board
        is returned, containing all the steps that have been taken to get there.
        """
        # Continue untill a solution has been found:
        while self.solution_found == False: 
        
            # Add baby nodes to queue:
            self.generate_nodes()

            # Check whether there's minimally one node in the queue:
            if self.queue.qsize() == 0:
                return print("No solution has been found.")

            # Select new node and update queue:
            self.update_current_node()

            # Evaluate current node:
            self.evaluate_node()

        return self.current_node.step_history
