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

    def step(self, car, dictionary, direction):
        '''
        Function to make a car move. The input is the car object and the direction
        in which it should move (1 or -1)
        '''
        print(dictionary[car])
        print(car)

        # ????????????
        orientation = dictionary[car][2]
        
        coordinates = dictionary[car][0]
        if orientation == 'H':
            coordinates[0] += direction

        if orientation == 'V':
            coordinates[1] += direction

        return coordinates
