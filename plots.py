import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import main
import board

class Plot_board():
    def __init__(self, filename='gameboards/Rushhour6x6_1.csv'):

        # read_board_size() missing 1 required positional argument: 'file_name'
        # self.board_size = board.Board.read_board_size(filename)
        self.board_size = 6
        self.fig = plt.figure(figsize = [self.board_size, self.board_size])
        self.ax = self.fig.add_subplot(111)

    def create_board(self, ):

        for x in range(self.board_size + 1):
            self.ax.plot([x, x], [0, self.board_size], 'k')
        for y in range(self.board_size + 1):
            self.ax.plot([0, self.board_size], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.board_size + 1)
        self.ax.set_ylim(-1, self.board_size + 1)

    def add_cars_in_plot(self):

        # for every car
        for car in main.cars_dictionary.keys():

            if main.cars_dictionary[car][2] == 'H':
                
                self.ax.add_patch(mpatches.Rectangle(main.cars_dictionary[car][0][0], main.cars_dictionary[car][1], 1, facecolor = (random.random(), random.random(), random.random())))
                
                if car == 'X':
                    self.ax.add_patch(mpatches.Rectangle(main.cars_dictionary[car][0][0], main.cars_dictionary[car][1], 1, facecolor = 'r' ))

            else:
                self.ax.add_patch(mpatches.Rectangle(main.cars_dictionary[car][0][0], 1, main.cars_dictionary[car][1], facecolor = (random.random(), random.random(), random.random())))

        plt.gca().invert_yaxis()
        plt.show()

board_plot = Plot_board()
plotting = board_plot.create_board()
c = board_plot.add_cars_in_plot()