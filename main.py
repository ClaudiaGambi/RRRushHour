import board
import cars
import random


if __name__ == '__main__':
    Board = board.Board()
    Board.create_board()
    Board.add_cars()
    car = random.choice(Board.cars_list)
    cars.move(car, 1)
