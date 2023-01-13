class Car():
 '''
    This class transforms the values for each car into a class object.
    These values include coordinates, size , type and orientation of the car.
    '''

    def __init__(self, x_coord, y_coord, length, orientation, type):
        self.x = x_coord - 1
        self.y = y_coord - 1
        self.length = length
        self.orientation = orientation
        self.type = type

    def move(self, car_object, direction):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1)
        '''
        if car_object.orientation == 'H':
            self.x += direction

        if car_object.orientation == 'V':
            self.y += direction
