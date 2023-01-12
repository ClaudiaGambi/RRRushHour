import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

class Cars():

    def __init__(self, x_coord, y_coord, length, orientation):
        self.x = x_coord
        self.y = y_coord
        self.length = length
        self.orientation = orientation


class Board():
    def __init__(self, column = 6, row = 6):
        self.column = column
        self.row = row
        self.fig = plt.figure(figsize = [self.column, self.row])
        self.ax = self.fig.add_subplot(111)
        self.cars_list = []


    def create_board(self):
        for x in range(self.column + 1):
            self.ax.plot([x, x], [0, self.column], 'k')
        for y in range(self.row + 1):
            self.ax.plot([0, self.row], [y, y], 'k')

        self.ax.set_position([0, 0, 1, 1])

        self.ax.set_axis_off()

        self.ax.set_xlim(-1, self.column + 1)
        self.ax.set_ylim(-1, self.row + 1)

        for car in range(len(self.cars_list)):
            print(car)
            print(car.orientation)
            if car.orientation == 'H':
                self.ax.add_patch(plt.Rectangle(car.x, car.y), 1, car.length)
                print('hi')
            else:
                self.ax.add_patch(plt.Rectangle(car.x, car.y), car.length, 1)

        plt.show()

    def create_car(self):
        df = pd.read_csv('gameboards/Rushhour6x6_1.csv')
        # print(df)
        for row, column in df.iterrows():
            col = column[2]
            # print(col)
            row = column[3]
            length = column[4]
            orientation = column[1]
            # print(orientation)
            self.cars_list.append(Cars(col, row, length, orientation))
        print(len(self.cars_list))




Board = Board()
Board.create_board()
# Board.create_car()

# cars_list = []
# df = pd.read_csv('gameboards/Rushhour6x6_1.csv')
# # print(df)
# for row, column in df.iterrows():
#     col = column[2]
#     # print(col)
#     row = column[3]
#     length = column[4]
#     orientation = column[1]
#     # print(orientation)
#     cars_list.append(Cars(col, row, length, orientation))
# # print(len(self.cars_list))
#
# for car in self.cars_list:
#     print(car)
#     print(car.orientation)
#     if car.orientation == 'H':
#         self.ax.add_patch(plt.Rectangle(car.x, car.y), 1, car.length)
#         print('hi')
#     else:
#         self.ax.add_patch(plt.Rectangle(car.x, car.y), car.length, 1)
#
# plt.show()