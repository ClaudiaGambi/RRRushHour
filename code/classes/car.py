
class Car():
    """
    This class initiates a car object. In a Car() instance information is saved (as 
    attributes) about the location, the size of car, the orientation, the name and
    the color.
    """

    def __init__(self, coordinates_list, length, orientation, type, color):
        
        self.coordinates_list = coordinates_list
        self.length = length
        self.orientation = orientation
        self.type = type
        self.color = color

    def propose_move(self, move):
        """
        Method to propose a move. As input a move needed: an integer representing the
        size and direction (-/+) of the move. The updated coordinates of the car 
        (after making the move) are returned.
        """

        # A list of coordinates representing the location of the car
        updated_coordinates = []

        # For horizontal cars, update the column coordinate
        if self.orientation == 'H':

            # Loop over all coordinates the car is on
            for coordinate in self.coordinates_list:
                
                # Update the coordinate with the size of the move
                updated_coordinate = (coordinate[0] + move, coordinate[1])

                # Save the updated coordinate
                updated_coordinates.append(updated_coordinate)
               

        # For vertical cars, update the row coordinate
        if self.orientation == 'V':

            # Loop over all coordinates the car is on
            for coordinate in self.coordinates_list:

                # Update the coordinate with the size of the move. For vertical cars
                # taking a step up on the board means subtracting the move from the
                # current coordinate (to line up with the check50 program)
                updated_coordinate = (coordinate[0], coordinate[1] - move)

                # Save the updated coordinate
                updated_coordinates.append(updated_coordinate)
        
        return updated_coordinates
        
    def update_coordinates(self, updated_coordinates):
        """
        Function updates coordinates in coordinates list to the new computed 
        updates coordinates from the step function. This function is called 
        if the availability in board is true. 
        """

        # Update coordinates in coordinates list
        self.coordinates_list = updated_coordinates

    def distance_to_endstate(self, other):
        """
        Method that takes a car (self) and a car from another board (other) and
        calculates the distance between the two cars. The distance is computed
        according to the orientation and then returned.
        """

        # Vertical cars
        if self.orientation == 'V':

            # Calculate distance with row values
            distance = abs(other.coordinates_list[0][1] - self.coordinates_list[0][1])
        
        # Horizontal cars
        else:
            # Calculate distance with column values
            distance = abs(other.coordinates_list[0][0] - self.coordinates_list[0][0])

        return distance

   
    

    
        
        

        
