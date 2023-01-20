import copy

class Breadth_first():
    """The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board). It evaluates each root node and adds
    their root nodes to the queue of nodes to be evaluated. When the evaluated node
    is the same as the solution board, the algorithm stops and returns the shortest
    root line to the solution."""

    def __init__(self, starting_board):
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
                #print(direction)
                # Propose a move:
                car.step(direction)
                # Check availability in the board:
                availability = self.current_node.check_availability(car)
                # If available, make a copy of the current board:
                if availability == True:
                    #print("--------------------------------")
                    #print(car.coordinates_list)
                    #Update coordinates of the car:
                    car.update_coordinates()
                    #print(car.coordinates_list)
                    #And make a copy of the updated board:
                    copy_ = copy.deepcopy(self.current_node)
                    # And update board history of the copy:
                    copy_.update_board_history(car.type, 1)
                    # And add copy to queue:
                    self.queue.append(copy_)
    
    def update_current_node(self):
        """Method to update the current node. It takes the first node from the queue,
        deletes it from there and moves it to the current node attribute."""

        # Update:
        self.current_node = self.queue[0]

        # Delete:
        self.queue.pop(0)
    
    def evaluate_node(self):
        """Method that checks whether the current board has the red car next to the exit.
        It uses the current node attribute and returns a boolean indicating whether the
        red car is on the exit coordinate, and so if the solution has been reached."""

        #Exit coordinates:
        exit = self.current_node.exit
        #print(exit)

        #Red car coordinates:
        red_car_coordinate = self.current_node.cars_list[-1].coordinates_list[0]
        #print(red_car_coordinate)

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
        count = 0
        # Continue untill a solution has been found:
        while self.solution_found == False:
        #for i in range(500):
            count+=1
            print(f"Round {count}")

            # Check whether there's minimally one node in the queue:
            if len(self.queue) < 1:
                return print("No solution has been found.")

            # Add baby nodes to queue:
            self.generate_nodes()

            # Select new node and update queue:
            self.update_current_node()

            # Evaluate current node:
            self.evaluate_node()

        return self.current_node.step_history