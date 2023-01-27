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
#imports libraries
import pygame
from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import time

#to hide the main Tkinter window
Tk().wm_withdraw() 

class Car:
    '''
    In the Car class, small details are changed so the input from our original Car object
    can be used for this car object. Fot the visuals, the car id letter needs to be an 
    attribute as well.
    '''
    def __init__(self, board_size, orientation, size, column, row, color, identification):

        #one square is has the length of 80
        square = 80

        # car identification
        self.identification = identification

        #starting x-coordinate
        self.startX = (column) * square 

        #starting y-coordinate
        self.startY = (row) * square

        self.orientation = orientation
        self.size = size

        length = square * size
        self.color = color
        
        #for horizontal cars
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
            
        # for vertical cars
        else:
            self.X = square
            self.Y = length 
            self.startY = self.startY + square

            #Starting x coordinate of where the car can be positioned
            self.startLimitX = self.startX

            #Starting y coordinate of where the car can be positioned
            self.startLimitY = 0

            #Ending x coordinate of where the car can be positioned
            self.endLimitX = self.startX + self.X
            
            #Ending y coordinate of where the car can be positioned
            self.endLimitY = board_size * 80 - length + 80

        self.currentX = self.startX #current x-coordinate of car
        self.currentY = self.startY #current y-coordinate of car

        self.rectDrag = False #boolean if the car is currently being dragged or not

        self.rect = pygame.Rect(self.startX, self.startY, self.X, self.Y) #make rectangle object

class Visual:
    '''
    The game class is changed so that it will automatically show the answer that is generated with
    one of our algorithms. This not really a game anymore, but more a visual representaion of our solution.
    
    In the solution csv contains the moves in the right order. These moves are done automatically in the 'game'
    to show how to get to the solution.
    '''
    def __init__(self, board, df, board_size):

        # get cars list from board object
        self.cars_list = board.cars_list
        self.makeCars(board_size)

        # keep track of turns
        self.turns = 0

        self.board_size = board_size

        # drop not needed columns, get the right answers in a dataframe
        self.answers = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        pygame.init() #run pygame
        surfaceSize = self.board_size * 80
        surface = pygame.display.set_mode((surfaceSize, surfaceSize)) #make display window

        self.inGame = True

        while self.inGame == True:

            #make the surface dark grey
            surface.fill((102,102,102))
            
            #display on window
            pygame.display.flip()

            for car in self.cars: 

                #color fill the rectangles
                surface.fill(car.color, car.rect) 

                #draw rectangles, with black borders
                pygame.draw.rect(surface, (0,0,0), car.rect, 5) 

                #display on window
                pygame.display.flip()
                
            #pygame events
            self.ev = pygame.event.poll() 

            #if window exited
            if self.ev.type == pygame.QUIT: 
                self.inGame = False

            # loop over the answers dataframe
            for index, row in self.answers.iterrows():

                # loop over cars
                for car in self.cars:

                    # if the car is the same as in the df, make the move
                    if car.identification == row['car']:

                        move = row['move']

                        # do this every second
                        time.sleep(1)

                        surface.fill((102,102,102), car.rect)

                        # make the move
                        new_rect = self.make_move(car, move)
        
                        #color fill the rectangles
                        surface.fill(car.color, new_rect) 
                        
                        # draw updated
                        pygame.draw.rect(surface, (0,0,0), new_rect, 5) 
                        
                        #display on window
                        pygame.display.flip() 

            self.gameOver()

        #quit program
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

        # if vertical:
        if car.orientation == 'V':

            # make move
            car.startY = car.startY + move

            # save in rectangle object
            car.rect = pygame.Rect(car.startX, car.startY, car.X, car.Y)

        # if horizontal
        else:
            # make move
            car.startX = car.startX + move

            # save in rectangle object
            car.rect = pygame.Rect(car.startX, car.startY, car.X, car.Y)

        return car.rect

    def makeCars(self, board_size): 
        '''
        This function takes the list of car objects from our own project and turns it into 
        a list suitable for this game.
        '''
        #list of car objects
        self.cars = [] 

        for car in self.cars_list: 

            # colors in pygame have a different range, so make new colors
            color = (random.randrange(10, 250), random.randrange(10, 250), random.randrange(10, 250))

            # save car objects in cars list, make sure red car(X) is red
            if car.type == 'X':
                self.cars.append(Car(board_size, car.orientation, car.length, car.coordinates_list[0][0] - 1, (board_size + 1) -car.coordinates_list[0][1] - 2, (255,0,0), car.type))
            else:
                self.cars.append(Car(board_size, car.orientation, car.length, car.coordinates_list[0][0] - 1, (board_size + 1) -car.coordinates_list[0][1] - 2, color, car.type))

    def gameOver(self): 

        #checks if starting coordinate of red/last car is at the winning position or not
        if self.cars[-1].startX == 320: 
            messagebox.showinfo('Congratulations!','You have completed the game!\nYou did it in %d moves!' % self.turns)
            self.inGame = False #cut the loop
