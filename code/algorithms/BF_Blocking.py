# ----------------------- Import packages and code ----------------------------

from code.algorithms import BF_NearExit
import copy
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

class BF_Blocking(BF_NearExit.BF_NearExit):
    """
    The Breadth First Blocking Cars inherits from Near Exit algorithm.
    On top of egular Breadth First, Blocking Cars checks how many cars there are in between
    the red car and the exist. Based on this information certain boards are 
    prioritized in the queue.
    """
    def __init__(self,starting_board):
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.queue = PriorityQueue()
        self.queue.put(PrioritizedItem(self.current_node.blocking_number_calculator(), self.current_node))
        self.solution_found = False
        self.all_states_set = set()
        self.all_states_set.add(str(self.current_node.coordinates_list))
        self.generation = 1
        self.expanded_nodes = 0
        self.evaluated_nodes = 0
     
    def generate_nodes(self):
        """
        Method that creates instances of all the posible next generation nodes,
        using the current node as a 'parent'. The nodes are added to the prioritized
        queue based on number of blocking cars.
        The board history (of each node) is saved in the board instance itself.
        """
        # Look at each possible move (on the parent board):
        for car in self.current_node.cars_list:            
            
            # Loop over the two possible directions
            for direction in [-1, 1]:

                # Make a first step
                step_count = 1

                # Check for multiple steps in a certain direction
                distance = direction * step_count

                # Safe the new coordinates of the possible new move
                new_coords = car.step(distance)  

                # If there is a spot available for the car to be moved to on the current board
                while self.current_node.check_availability(car, new_coords) == True:
                    
                    # Add 1 to count for possible next step
                    step_count +=1
                    
                    carname = car.type

                    # get index of car in current node
                    car_index = self.current_node.cars_list.index(car)

                    # If a possible move is proposed, make a copy of the parent board
                    child = copy.deepcopy(self.current_node)                        # Make a copy of the parent board

                    # Update coordinates of car in child board with index of mother board
                    child.cars_list[car_index].update_coordinates(new_coords)
                    
                    # Update coordinates list of the child board
                    child.update_coordinates_board_state()                          # Update coordinates list of the child
                
                    # Update board history of the child
                    child.update_board_history(carname, distance)                  # Update board history of the child

                    # Safe child board as string
                    child_coords = str(child.coordinates_list)

                    # Check whether child doesn't already exists in the all states set
                    if child_coords not in self.all_states_set:

                        # Based on the number of blocking cars the queue is ordered
                        # For this child, the number of blocking cars is computed
                        # Based on that value the child is put in a certain spot in the queue
                        self.queue.put(PrioritizedItem(child.blocking_cars(), child))
    
                        # Add to all state set
                        self.all_states_set.add(child_coords)

                        # Add to expanded nodes 
                        self.expanded_nodes += 1

                    # Add step to distance
                    distance = direction * step_count

                    # Update new coordinates
                    new_coords = car.step(distance)  