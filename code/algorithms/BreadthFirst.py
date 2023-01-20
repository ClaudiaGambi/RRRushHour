<<<<<<< HEAD
from classes import board
=======
from code.classes import board
>>>>>>> fd328ffb107b79bcacf049261a5c56e020251408
import copy

class Breadth_first(board.Board):
    """The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board). It evaluates each root node and adds
    their root nodes to the queue of nodes to be evaluated. When the evaluated node
    is the same as the solution board, the algorithm stops and returns the shortest
    root line to the solution."""

<<<<<<< HEAD
    def _init_(self, starting_board):
=======
    def init(self, starting_board):
>>>>>>> fd328ffb107b79bcacf049261a5c56e020251408
        self.current_node = starting_board
        self.queue = [copy.deepcopy(starting_board)]
        self.solution_found = False

    def generate_nodes(self):
        """Method that creates instances of all the posible next generation nodes,
        using the current node as a 'parent'. The nodes are added to the queue list
        attribute. The board history (of each node) is saved in the board instance
        itself."""

        # Loop through the cars in the current node:
        for car in self.current_node.cars_list:
            # Propose a move in both directions:
            for direction in [-1,1]:
                # Make a copy of the current board:
                copy_ = copy.deepcopy(self.current_node)
                # Propose a move:
                car.step(direction)
                # Check availability in the board:
                copy_.check_availability(car)
                # If available, update board history:
                copy_.update_board_history(car, 1)
                # And add copy to queue:
                self.queue.append(copy_)
    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

        # Update:
        self.current_node = self.queue[0]

        # Delete:
        self.queue -= self.current_node
    
    def evaluate_node(self):
        """Method that checks whether the current board has the red car next to the exit.
        It uses the current node attribute and returns a boolean indicating whether the
        red car is on the exit coordinate, and so if the solution has been reached."""

        #
        exit_coordinate = (5, 4)

        return self.solution_found == True/False
    
    def run(self):
        """Method that runs the algorithm. It continues untill a solution has been
        found. Untill then, each node in the queue is evaluated and root nodes are 
        created. When the solution has been found, the board history of that board
        is returned, containing all the steps that have been taken to get there."""
        
        # Continue untill a solution has been found:
        while self.solution_found == False:

            # Check whether there's minimally one node in the queue:
            if len(self.queue) < 1:
                return print("No solution has been found.")

            # Add baby nodes to queue:
            self.generate_nodes()

            # Select new node and update queue:
            self.update_current_node()

            # Evaluate current node:
            self.evaluate_node()

        return self.current_node.board_history