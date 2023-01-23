import numpy as np
import matplotlib.pyplot as plt


class Plot_board():
    def __init__(self, board_size):

        self.board_size = board_size
        self.fig = plt.figure(figsize = [self.board_size, self.board_size])
        self.ax = self.fig.add_subplot(111)

    def create_board(self):
        '''
        Create an empty grid to plot the cars in.
        '''
        
        #Create basic grid:
        for x in range(self.board_size + 1):
            self.ax.plot([x, x], [0, self.board_size], 'k')
        for y in range(self.board_size + 1):
            self.ax.plot([0, self.board_size], [y, y], 'k')

        #Make sure the board is squared:
        self.ax.set_position([0, 0, 1, 1])

        #No numbers visible:
        self.ax.set_axis_off()
        self.ax.set_xlim(-1, self.board_size + 1)
        self.ax.set_ylim(-1, self.board_size + 1)

    def plot_dotted_cars(self, cars_list):
        plt.ion()
        
        #Loop through cars list:
        for car in cars_list:
            #Select the color:
            color = car.color
           
            #Loop through every coordinate of the car:
            for coordinate in car.coordinates_list:
                column = coordinate[0]
                row = coordinate[1]
                self.ax.plot(column - 0.5,row - 0.5, marker = "s", color = color, markersize = 50)
        
        
        #!!! create plot that does not close figure  !!!
       
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(5)
        
    

