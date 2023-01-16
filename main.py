import board
from car import Car
import random

filename = 'gameboards/Rushhour6x6_1.csv'

if __name__ == '__main__':

    #Create starting board:
    Board = board.Board()
    Board.read_board_size(filename)
    # Board.board_in_array()
    dictionary = Board.df_to_dict(filename)
    cars_dictionary = dictionary[0]
    step_dictionary = dictionary[1]


    #Plot situation:
    # Board.add_cars()  

    #While not not solved:
    while cars_dictionary['X'][0] != (5, 3):

        # move count
        move_count = 0

        # choose randomly from car dictionary
        random_car = random.choice(list(cars_dictionary.keys()))

        # choose direction randomly
        random_direction = random.choice([1, -1])
        
        # propose a random step:
        new_coordinates = Board.step(random_car, cars_dictionary, random_direction)

        #Check availablity:
        availability = Board.check_availability(new_coordinates, dictionary)

        #If available, save the step in (updated) dictionary:
        if availability == True:
            dictionary[random_car][0] = new_coordinates

            move_count += 1

            # update step dictionary to keep track of the game
            step_dictionary[random_car].append((move_count, random_direction))

        #Plot current situation:
        Board.plot_situation(self.dictionary_coordinates)  



