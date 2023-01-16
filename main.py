import board
import car
import random

if __name__ == '__main__':

    #Create starting board:
    Board = board.Board()
    Board.read_board_size()
    Board.board_in_array()

    #Plot situation:
    Board.add_cars()  

    #While not not solved:

        #Propose a random step:
        # choose randomly from car dictionary
        random_car_step = random.choice(Board.cars_dictionary)

        # choose direction randomly
        random_direction_step = random.choice([1, -1])

        # to check order of step, keep track of total number of steps in game
        number_step = 0

        # create step
        step = (random_car_step, number_step += 1, random_direction_step)

        new_coordinates = car.step(car, 1)

        #Check availablity:
        Board.check_availability(new_coordinates, self.dictionary_coordinates_all)

        #If available, save the step:
        if available = + :
            Board.add_step_to_dictionary(step)

        #And update locations dictionary:
        Board.update_location(new_coordinates)

        #Plot current situation:
        Board.plot_situation(self.dictionary_coordinates)  

    return dictionary_with_steps             
    
   
