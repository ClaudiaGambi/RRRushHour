import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import main
import board

class Plot_board():
    def __init__(self, filename='gameboards/Rushhour6x6_1.csv'):

        # read_board_size() missing 1 required positional argument: 'file_name'
        # wat was dit ookalweer?
        # self.board_size = board.Board.read_board_size(filename)
        # tijdelijke oplossing
        self.board_size = 6
        self.fig = plt.figure(figsize = [self.board_size, self.board_size])
        self.ax = self.fig.add_subplot(111)

    def create_board(self):
        '''
        Create an empty grid to plot the cars in.
        '''
        # axis = list(range(0,self.board.size))

        # plt.new()
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

        plt.show()

    def add_cars_in_plot(self, dictionary):
        """
        Method that reads coordination information of the cars dictionary. 
        Creates a plot representing the board based on that information.
        """

        # for every car in the dictionary
        for car in dictionary.keys():

            # check the orientation
            if dictionary[car][2] == 'H':
                self.ax.add_patch(mpatches.Rectangle(dictionary[car][0][0], dictionary[car][1], 1, facecolor = dictionary[car][3] ))

            # plot patch with different orientation
            else:
                self.ax.add_patch(mpatches.Rectangle(dictionary[car][0][0], 1, dictionary[car][1], facecolor = dictionary[car][3] ))

        #Mirror board:
        plt.gca().invert_yaxis()
        plt.show()
