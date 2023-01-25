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
    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

       
        # Delete:
        self.queue.pop(0)

        # Sort:
        # print("before")
        # for i in self.queue:
        #     i.array_plot(i.coordinates_list)

        self.sort_queue()

        # print("after")
        # for i in self.queue:
        #     i.array_plot(i.coordinates_list)

        # Update:
        self.current_node = self.queue[0]

        # Update generation:
        old_generation = self.generation
        self.generation = len(self.current_node.step_history)
        
        if old_generation != self.generation:
            print(f"\nNext generation: {self.generation} -------------------------------\n")
