''''
To create a automatically playing visual representation of our solutions, 
I copied the parts of the python game I needed and changed the game class 
to a visual class to represent the results.

First run any of the algorithms. For example:
python main.py -algo BreadthFirst data/output.csv gameboards/Rushhour6x6_1.csv

This will put the output steps into a csv. Then with this output file you can
run the visual that will show the results:

python main.py -algo visual data/output.csv gameboards/Rushhour6x6_1.csv
'''
# ----------------------- Import packages and code ----------------------------
import pygame
from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import time
# -----------------------------------------------------------------------------

# To hide the main Tkinter window
Tk().wm_withdraw() 

class Car:
    '''
    In the Car class, small details are changed so the input from our original Car object
    can be used for this car object. Fot the visuals, the car id letter needs to be an 
    attribute as well.
    '''
    def __init__(self, board_size, orientation, size, column, row, color, identification):

        # One square is has the length of 80
        square = 80

        # Car identification
        self.identification = identification

        # Starting x-coordinate
        self.startX = (column) * square 

        # Starting y-coordinate
        self.startY = (row) * square

        self.orientation = orientation
        self.size = size

        length = square * size
        self.color = color
        
        # For horizontal cars
        if self.orientation == "H": 
            
            self.X = length
            self.Y = square 
            self.startY = self.startY + square

            #Starting x coordinate of where the car can be positioned
            self.startLimitX = 0 

            #Starting y coordinate of where the car can be positioned
            self.startLimitY = self.startY 

            #Ending x coordinate of where the car can be positioned
            self.endLimitX = board_size * 80 - length + 80 

            #Ending y coordinate of where the car can be positioned
            self.endLimitY = self.startY + self.Y
            
        # For vertical cars
        else:
            self.X = square
            self.Y = length 
            self.startY = self.startY + square

            # Starting x coordinate of where the car can be positioned
            self.startLimitX = self.startX

            # Starting y coordinate of where the car can be positioned
            self.startLimitY = 0

            # Ending x coordinate of where the car can be positioned
            self.endLimitX = self.startX + self.X
            
            # Ending y coordinate of where the car can be positioned
            self.endLimitY = board_size * 80 - length + 80

        # Current x-coordinate of car
        self.currentX = self.startX 

        # Current y-coordinate of car
        self.currentY = self.startY 

        # Boolean if the car is currently being dragged or not
        self.rectDrag = False 

        # Make rectangle object
        self.rect = pygame.Rect(self.startX, self.startY, self.X, self.Y) 

class Visual:
    '''
    The game class is changed so that it will automatically show the answer that is generated with
    one of our algorithms. This not really a game anymore, but more a visual representaion of our solution.
    
    In the solution csv contains the moves in the right order. These moves are done automatically in the 'game'
    to show how to get to the solution.
    '''
    def __init__(self, board, df):

        # Get cars list from board object
        self.cars_list = board.cars_list
        self.board_size = board.board_size
        self.makeCars()

        # Keep track of turns
        self.turns = 0

        # Drop not needed columns, get the right answers in a dataframe
        self.answers = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        # Run pygame
        pygame.init()

        surfaceSize = self.board_size * 80

        # Make display window
        surface = pygame.display.set_mode((surfaceSize, surfaceSize)) 

        self.inGame = True

        while self.inGame == True:

            # Make the surface dark grey
            surface.fill((102,102,102))
            
            # Display on window
            pygame.display.flip()

            # For every car
            for car in self.cars: 

                # Color fill the rectangles
                surface.fill(car.color, car.rect) 

                # Draw rectangles, with black borders
                pygame.draw.rect(surface, (0,0,0), car.rect, 5) 

                # Display on window
                pygame.display.flip()
                
            # Pygame events
            self.ev = pygame.event.poll() 

            # If window exited
            if self.ev.type == pygame.QUIT: 
                self.inGame = False

            # Loop over the answers dataframe
            for index, row in self.answers.iterrows():

                # Loop over cars
                for car in self.cars:

                    # If the car is the same as in the df, make the move
                    if car.identification == row['car']:

                        move = row['move']

                        # Do this every second
                        time.sleep(1)

                        surface.fill((102,102,102), car.rect)

                        # Make the move
                        new_rect = self.make_move(car, move)
        
                        # Color fill the rectangles
                        surface.fill(car.color, new_rect) 
                        
                        # Draw updated
                        pygame.draw.rect(surface, (0,0,0), new_rect, 5) 
                        
                        # Display on window
                        pygame.display.flip() 

            self.gameOver()

        # Quit program
        pygame.quit() 

    def make_move(self, car, move):
        '''
        (new function)
        This function takes a specific car object and a move and returns an updated rectangle object with the 
        new location. 
        '''
        # *80 to match the square sizes
        move = move * 80
        self.turns += 1

        # If vertical
        if car.orientation == 'V':

            # Make move
            car.startY = car.startY + move

            # Save in rectangle object
            car.rect = pygame.Rect(car.startX, car.startY, car.X, car.Y)

        # If horizontal
        else:
            # Make move
            car.startX = car.startX + move

            # Save in rectangle object
            car.rect = pygame.Rect(car.startX, car.startY, car.X, car.Y)

        return car.rect

    def makeCars(self): 
        '''
        This function takes the list of car objects from our own project and turns it into 
        a list suitable for this game.
        '''
        # List of car objects
        self.cars = [] 

        for car in self.cars_list: 

            # Colors in pygame have a different range, so make new colors
            color = (random.randrange(10, 250), random.randrange(10, 250), random.randrange(10, 250))

            # Save car objects in cars list, make sure red car(X) is red
            if car.type == 'X':
                self.cars.append(Car(self.board_size, car.orientation, car.length, car.coordinates_list[0][0] - 1, (self.board_size + 1) -car.coordinates_list[0][1] - 2, (255,0,0), car.type))
            else:
                self.cars.append(Car(self.board_size, car.orientation, car.length, car.coordinates_list[0][0] - 1, (self.board_size + 1) -car.coordinates_list[0][1] - 2, color, car.type))

    def gameOver(self): 

        # Checks if starting coordinate of red/last car is at the winning position or not
        if self.cars[-1].startX == (self.board_size - 2) * 80: 
            messagebox.showinfo('Congratulations!','You have completed the game!\nYou did it in %d moves!' % self.turns)
            self.inGame = False #cut the loop
