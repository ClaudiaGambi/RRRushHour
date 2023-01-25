import copy
import numpy as np
from code.classes import plots
from code.algorithms import BreadthFirst
from operator import attrgetter

class BF_NearExit(BreadthFirst.Breadth_first):

    """
    A Breadth First algorithm that sorts the queue of board states according to the distance
    of the red car to the exit. 
    """

    def sort_queue(self):

        #self.queue.sort(key=lambda x: x.distance_to_exit, reverse = False)
        self.queue.sort(key=attrgetter("distance_to_exit"))

    def generate_nodes(self):

        #1. Look at each possible move (on the parent board):
        for car in self.current_node.cars_list:                                 # Loop through cars on the parent board
            
            for direction in [-1, 1]:                                           # Propose a move in both directions

                new_coords = car.step(direction)                                # Propose a move on the parent board

                # new_coords = car.updated_coordinates
                carname = car.type

                # get index of car in current node
                i = self.current_node.cars_list.index(car)

                availability = self.current_node.check_availability(car, new_coords)# Check availability on the parent board

        #2. If a possible move is proposed, make a copy of the parent board:

                if availability == True:

                    child = copy.deepcopy(self.current_node)                        # Make a copy of the parent board

        #3. Adjust child board with the proposed move:
        # update coordinates of car in child board with index of mother board
                    # print(f'before: {child.cars_list[i].coordinates_list}')
                    child.cars_list[i].update_coordinates(new_coords)
                    # print(f'after:{child.cars_list[i].coordinates_list}')
                    
                    child.update_coordinates_board_state()                          # Update coordinates list of the child
                
                    child.update_board_history(carname, direction)                  # Update board history of the child

                    child_coords = str(child.coordinates_list)

        #4. Check whether child doesn't already exists in the all states set:

                    if child_coords not in self.all_states_set:

        #5. If not, make distance to exit variable:

                        child.distance_calculator()

        #6. And add to queue and to all state set:

                        self.queue.append(child)

                        self.all_states_set.add(child_coords)

                        self.expanded_nodes += 1

                        #child.array_plot(child.coordinates_list)                    # Show array of the board
        
        #7. Organize queue:

                        self.sort_queue()

