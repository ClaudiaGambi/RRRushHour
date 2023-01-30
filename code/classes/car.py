
class Car():
    '''
    This class initiates a car object. In this object attributes with the coordinates,
    length of car, orientation, identification, and color are created.

    In this class, the function step is created too. This function lets a car take a step.
    '''
    def __init__(self, coordinates_list, length, orientation, type, color):
        self.coordinates_list = coordinates_list
        self.length = length
        self.orientation = orientation

        # identification of car
        self.type = type
        self.color = color

        

    def step(self, direction ):
        '''
        Function to make a car move. The input is the car object, the direction and the amount of steps
        in which it should move. The function returns new coordinates.
        '''
        updated_coordinates = []

        # if the car moves horizontally, add the direction to the current x coordinate
        if self.orientation == 'H':

            # loop over all coordinates the car is on
            for coordinate in self.coordinates_list:

                updated_x = coordinate[0] + direction
                updated_coordinate = (updated_x, coordinate[1])

                # update the coordinate list
                updated_coordinates.append(updated_coordinate)
               

        # if the car moves vertically, add the direction to the current y coordinate
        if self.orientation == 'V':

            # loop over all coordinates the car is on
            for coordinate in self.coordinates_list:
                updated_y = coordinate[1] - direction
                updated_coordinate = (coordinate[0], updated_y)

                # update the coordinate list
                updated_coordinates.append(updated_coordinate)
        
        return updated_coordinates
        
        
    def update_coordinates(self, updated_coordinates):
        """
        Function updates coordinates in coordinates list to the new computed 
        updates coordinates from the step function. This function is called 
        if the availability in board is true. 
        """

        # update coordinates in coordinates list
        self.coordinates_list = updated_coordinates

    def distance_calculator_star (self, other):
        """
        Function that takes a car (self) and a car from another board (other) and calculates the distance between the two cars.
        The distance is computed according to the orientation and then returned.
        """

        #get orientation of car 
        if self.orientation == 'V':

            # calculate distance with y values 
            distance = abs(other.coordinates_list[0][1] - self.coordinates_list[0][1])
        else:

            # calculate distance with x values 
            distance = abs(other.coordinates_list[0][0] - self.coordinates_list[0][0])

        return distance

   
    

    
        
        

        
