import copy
# import numpy as np
# from code.classes import plots
from code.algorithms import BreadthFirst
# from operator import attrgetter
from queue import PriorityQueue
from typing import Any
from dataclasses import dataclass, field
import copy 

@dataclass(order=True)
class PrioritizedItem:
    priority: int 
    item: Any = field(compare=False)


class BF_NearExit(BreadthFirst.Breadth_first):

    """
    A Breadth First algorithm that sorts the queue of board states according to the distance
    of the red car to the exit. 
    """
    def __init__(self,starting_board):
        self.current_node = starting_board
        #open_list
        self.queue = [copy.deepcopy(starting_board)]
        self.queue = PriorityQueue()
        self.queue.put(PrioritizedItem(self.current_node.distance_calculator(), self.current_node))
        
        self.solution_found = False
        #closed_list
        self.all_states_set = set()
        self.all_states_set.add(str(self.current_node.coordinates_list))
        self.generation = 1
        self.expanded_nodes = 0
    

    # def sort_queue(self):

    #     #self.queue.sort(key=lambda x: x.distance_to_exit, reverse = False)
    #     self.queue.sort(key=attrgetter("distance_to_exit"))
    
   
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
                availability = True
                while availability == True:
                    count +=1
                    distance = direction * count
                    new_coords = car.step(distance)  
                    # print(new_coords)  
                                                # Propose a move on the parent board

                    # new_coords = car.updated_coordinates
                    carname = car.type

                    # get index of car in current node
                    i = self.current_node.cars_list.index(car)

                    availability = self.current_node.check_availability(car, new_coords) 
                    # print(availability)
                    # Check availability on the parent board

            #2. If a possible move is proposed, make a copy of the parent board:
                    if availability == True:
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

                            # child.distance_calculator()

                            self.queue.put(child.distance_calculator(), child)

                            self.all_states_set.add(child_coords)

                            # child.array_plot(child.coordinates_list)                    # Show array of the board

                            self.expanded_nodes += 1

    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

       
        # Delete:
        # self.queue.pop(0)

        # Save number of evaluated nodes:
        self.evaluated_nodes += 1

        # Sort:
        # self.sort_queue()

        # Update:
        self.current_node = self.queue.get().item

        # Update generation:
        old_generation = self.generation
        self.generation = len(self.current_node.step_history)
        
        if old_generation != self.generation:
            print(f"\nNext generation: {self.generation} -------------------------------\n")
        
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
            if self.queue.qsize() == 0:
                return print("No solution has been found.")

            # Select new node and update queue:
            self.update_current_node()

                # Evaluate current node:
            self.evaluate_node()

        return self.current_node.step_history
