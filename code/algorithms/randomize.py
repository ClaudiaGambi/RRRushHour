import random
from classes import board
from classes.car import step as st

class Random():
    '''
    Implementation of random algorithm 
    '''
    def __init__(self, filename):
        self.board = board.Board(filename)
        
    def run(self):
        for car in self.board.cars_list:
             #While not not solved:
            while car.type == 'X' and car.coordinates_list[0] != (5, 4):

   
   #for i in range(60):
                 # move count
                move_count = 0

                # choose randomly from car dictionary
                random_car = random.choice(self.board.cars_list)

                # choose direction randomly
                random_direction = random.choice([1, -1])
                
                # propose a random step:
                random_car.st(random_direction)

                #Check availablity:
                availability = Board.check_availability(random_car, new_coordinates, cars_dictionary)

                #If available, save the step in (updated) dictionary:
                if availability == True:
                    print(f"Old coordinates: {cars_dictionary[random_car][0]}")
                    print(f"New coordinates: {new_coordinates}")
                    cars_dictionary[random_car][0] = new_coordinates
                    move_count += 1
                    # print(cars_dictionary)

                    #Plot current situation:
                    plot2 = plots.Plot_board()
                    plot2.create_board()
                    #plot2.add_cars_in_plot(cars_dictionary)
                    plot2.plot_dotted_cars(cars_dictionary)
                
                # Keep track of the game steps:
                lst.append([random_car, random_direction])

                    
            steps_df = pd.DataFrame(lst, columns = ["car", "move"])
            print(steps_df.head())

                


