# from code.classes import board
from code.algorithms import BreadthFirst
from queue import PriorityQueue
from typing import Any
from dataclasses import dataclass, field
import copy 

@dataclass(order=True)
class PrioritizedItem:
    priority: int 
    item: Any = field(compare=False)

class A_star(BreadthFirst.Breadth_first):
    '''
    This class is an inheritance from Breadth First '''
    def __init__(self, end_board, starting_board):
        self.end_node = end_board
        self.current_node = starting_board
        #open_list
        self.queue = [copy.deepcopy(starting_board)]
        self.queue = PriorityQueue()
        self.queue.put(PrioritizedItem(self.current_node.cost_star(self.end_node.cars_list), self.current_node))
        
        self.solution_found = False
        #closed_list
        self.all_states_set = set()
        self.all_states_set.add(str(self.current_node.coordinates_list))
        self.generation = 1
        self.expanded_nodes = 0
        
    def generate_nodes(self):
        #1. Look at each possible move (on the parent board):
        # Loop through cars on the parent board
        for car in self.current_node.cars_list:                                 
            
            for direction in [-1, 1]:
                count = 1
                distance = direction * count
                new_coords = car.step(distance)
                # get index of car in current node
                i = self.current_node.cars_list.index(car)
                
                # self.queue.put(PrioritizedItem(self.current_node.cars_list[i].distance_calculator_star(self.end_node.cars_list[i]), self.current_node.cars_list[i]))
                # print(self.queue)
                
                while self.current_node.check_availability(car, new_coords) == True:
                    count +=1
                                                # Propose a move on the parent board

                    # new_coords = car.updated_coordinates
                    carname = car.type                    

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

                        self.queue.put(PrioritizedItem(child.cost_star(self.end_node.cars_list),child))

                        # print(child.distance(self.end_node.cars_list), child)
                        self.all_states_set.add(child_coords)

                        # child.array_plot(child.coordinates_list)                    # Show array of the board

                        self.expanded_nodes += 1
                    distance = direction * count
                    new_coords = car.step(distance)

    def update_current_node(self):
        """
        Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute.
        """
        # Update:
        self.current_node = self.queue.get().item

        #Update generation:
        # old_generation = self.generation
        # self.generation = len(self.current_node.step_history)
        
        #if old_generation != self.generation:
            #print(f"\nNext generation: {self.generation} -------------------------------\n")
    

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

    