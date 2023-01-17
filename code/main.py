import board
import random
import pandas as pd

filename = 'gameboards/Rushhour6x6_1.csv'

if __name__ == '__main__':

    #Create starting board:
    Board = board.Board()
    Board.read_board_size(filename)
    # Board.board_in_array()
    Board.df_to_dict(filename)

    cars_dictionary = Board.cars_dict
    step_dictionary = Board.step_dict

    #Plot situation:
    # Board.add_cars()  

    #Dataframe to keep track of steps:
    steps_df = pd.DataFrame(columns=["car_name", "move"])

    #While not not solved:
    #while cars_dictionary['X'][0] != (5, 3):
    for i in range(20):
        # move count
        move_count = 0

        # choose randomly from car dictionary
        random_car = random.choice(list(cars_dictionary.keys()))

        # choose direction randomly
        random_direction = random.choice([1, -1])
        
        # propose a random step:
        new_coordinates = Board.step(random_car, cars_dictionary, random_direction)

        #Check availablity:
        availability = Board.check_availability(new_coordinates, cars_dictionary)

        #If available, save the step in (updated) dictionary:
        if availability == True:
            cars_dictionary[random_car][0] = new_coordinates

            move_count += 1
            # update step df to keep track of the game
            steps_df.loc[move_count] = [random_car + random_direction]

            d = {"car_name": random_car, "move": random_direction}
            serie = pd.Series(data=d, index = ["car_name", "move"])
            df = serie.to_frame()

            steps_df = steps_df.concat([serie])
        print(random_car)
        print(random_direction)
            

    print(steps_df)

        #Plot current situation:
        #Board.plot_situation(self.dictionary_coordinates)  



