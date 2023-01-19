import board

class Breadth_first(board.Board):
    """The breadth first algorithm generates root nodes (possible next board
    situations) for the starting node (board)."""

    def __init__(self, starting_board, solution_board):
        self.current_node = starting_board
        self.solution_board = solution_board
        self.queue = [starting_board]
        self.solution_found = False

    def generate_nodes(self):
        self.current_board()
        return self.list_of_next_generation_boards ([board, board, board])
    
    def add_nodes_to_queue(self):
        self.queue.append(self.list_of_next_generation_boards)
    
    def select_first_node_from_queue(self):
        update self.current_node (taking first node from self.queue)
    
    def evaluate_first_node_from_queue(self):
        self.current_node == solution_board
        return self.solution_found = True/False
    
    def trace_solution_path(self):
        return df
    
    def run(self):
        
        # Continue untill a solution has been found:
        while self.solution_found == False:

            # Check whether there's minimally one node in the queue:
            if len(self.queue) < 1:
                return print("No solution has been found.")

            # Voeg de wortel van de graaf toe aan de queue:
            self.generate_nodes()
            self.add_nodes_to_queue()

            # If there's a node in the queue, evaluate it:
            self.evaluate_first_node_from_queue()

            # Als dit een oplossing is: stop het zoeken en geef de oplossing:
            if self.solution_found == True:
                return self.generate_solution_path
            
            # Als dit geen oplossing is: voeg alle kinderen van deze knoop toe aan het einde van de FIFO queue:
            else:
                self.generate_nodes()
                self.add_nodes_to_queue()

        return df