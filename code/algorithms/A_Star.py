# ----------------------- Import packages and code ----------------------------
from code.algorithms import BF_NearExit
from queue import PriorityQueue
from typing import Any
from dataclasses import dataclass, field
import copy 

# -----------------------------------------------------------------------------

@dataclass(order=True)
class PrioritizedItem:
    """
    Initialize priority queue
    """
    priority: int 
    item: Any = field(compare=False)

class A_star(BF_NearExit.BF_NearExit):
    '''
    This class is an inheritance from BF_NearExit and takes a starting board and endboard as inpt.
    Astar works with a priorityqueue, the queue is prioritized based on the total distances between 
    beginstates en endstates of cars. The amount of cars blocking the red car also is added 
    to the value for the priorityqueue. 
    '''
    def __init__(self, end_board, starting_board):
        self.end_node = end_board
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.queue = PriorityQueue()
        self.queue.put(PrioritizedItem(self.current_node.cost_star(self.end_node.cars_list), self.current_node))
        self.solution_found = False
        self.all_states_set = set()
        self.all_states_set.add(str(self.current_node.coordinates_list))
        self.generation = 1
        self.expanded_nodes = 0
        self.evaluated_nodes = 0
        
    def generate_nodes(self):
        #1. Look at each possible move (on the parent board):
        # Loop through cars on the parent board
        for car in self.current_node.cars_list:                                 
            
            for direction in [-1, 1]:

                # Keep count 
                count = 1

                # Compute value of move 
                distance = direction * count

                # Generate new coordinates with move 
                new_coords = car.step(distance)

                # Get index of car in current node
                i = self.current_node.cars_list.index(car)
                
                # Loop while availability is true
                while self.current_node.check_availability(car, new_coords) == True:
                    count +=1
                                                
                    # Get name type of car for updates of board
                    carname = car.type                    

                     # If a possible move is proposed, make a copy of the parent board
                     # Make a copy of the parent board
                    child = copy.deepcopy(self.current_node)     

                    # Adjust child board with the proposed move
                    # update coordinates of car in child board with index of parent board
                    child.cars_list[i].update_coordinates(new_coords)
                   
                   # Update coordinates list of the child 
                    child.update_coordinates_board_state()          

                    # Update board history of the child
                    child.update_board_history(carname, distance)   

                    # Create string of board coordinates               
                    child_coords = str(child.coordinates_list)
                    
                    # Check whether child doesn't already exists in the all states set
                    if child_coords not in self.all_states_set:

                        # If not, add to queue and to all state set
                        self.queue.put(PrioritizedItem(child.cost_star(self.end_node.cars_list),child))

                        # Add child coords to set
                        self.all_states_set.add(child_coords)

                        # count expanded nodes              
                        self.expanded_nodes += 1

                    # update move value with new count
                    distance = direction * count

                    # propose new coordinates 
                    new_coords = car.step(distance)

    