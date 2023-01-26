#imports libraries
import pygame
import sys
import math
from tkinter import *
from tkinter import messagebox
import random
import pandas as pd

Tk().wm_withdraw() #to hide the main Tkinter window

# limit downwards is off because of changed settings...

class Car:

    def __init__(self, orientation, size, column, row, color, identification):

        #one square is has the length of 80
        square = 80

        #starting x-coordinate
        self.startX = (column) * square 

        #starting y-coordinate
        self.startY = (row) * square

        self.identification = identification
        self.orientation = orientation
        self.size = size
        # pygame.display.init()
        # pygame.display.set_mode()
        
        #for horizontal cars
        if self.orientation == "H": 

            #How much the x-coordinate extends by
            length = square * size

            #How much the y-coordinate extends by
            self.X = length
            self.startY = self.startY + square

            self.Y = square 
            self.color = color
            self.startLimitX = 0 #Starting x coordinate of where the car can be positioned
            self.startLimitY = self.startY #Starting y coordinate of where the car can be positioned
            self.endLimitX = 480 - length + 80 #Ending x coordinate of where the car can be positioned
            self.endLimitY = self.startY + self.Y #Ending x coordinate of where the car can be positioned
            
        else: #same as above, but for vertical, so swap x and y
            length = square * size
            self.X = square
            self.Y = length 
            self.color = color
            self.startLimitX = self.startX
            self.startLimitY = 0
            self.endLimitX = self.startX + self.X
            self.endLimitY = 480 - length + 80

        self.currentX = self.startX + 0 #current x-coordinate of car
        self.currentY = self.startY + 0 #current y-coordinate of car

        self.rectDrag = False #boolean if the car is currently being dragged or not
        # IMAGE = pygame.image.load('mcqueen.png').convert_alpha()  # or .convert_alpha()

        self.rect = pygame.Rect(self.startX, self.startY, self.X, self.Y) #make rectangle object
        # Create a rect with the size of the image.
        # self.rect = IMAGE.Rect(self.startX, self.startY, self.X, self.Y)


class game: #main class
    # board object as input
    def __init__(self, board, df):

        # get cars list
        self.cars_list = board.cars_list
        self.makeCars()
        self.turns = 0

        # drop not needed columns, get the right answers in a dataframe
        self.answers = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        # print(self.answers)
        
        pygame.init() #run pygame
        surfaceSize = 480
        surface = pygame.display.set_mode((surfaceSize, surfaceSize)) #make display window
        
        start = True #if it is beginning of program
        self.inGame = True #loop condition

        while self.inGame:
            self.ev = pygame.event.poll() #pygame events
            if self.ev.type == pygame.QUIT: #if window exited
                self.inGame = False

            # for row in self.answers:
            #     for car in self.cars_list:
            #         if car.type == row[0]:
            #             if self.ev.type == pygame.MOUSEBUTTONUP: #if the window has been released from the left-click
            #                 self.unclickObject(car)

            
            elif self.ev.type == pygame.MOUSEBUTTONDOWN: #if the window has been left-clicked
                self.clickObject()

            elif self.ev.type == pygame.MOUSEBUTTONUP: #if the window has been released from the left-click
                self.unclickObject()

            elif self.ev.type == pygame.MOUSEMOTION: #if the lect click is still being clicked
                self.objectMidAir()

            #make the surface dark grey
            surface.fill((102,102,102))

            for car in range(len(self.cars)): #for each rectangle
                surface.fill(self.cars[car].color, self.cars[car].rect) #color fill the rectangles
                pygame.draw.rect(surface, (0,0,0), self.cars[car].rect, 5) #draw rectangles, with black borders
            
            #display on window
            pygame.display.flip() 
            
            if start: #if beginning of program
                #create popup
                # messagebox.showinfo('Welcome!','Rush Hour\nGet the red car to the end.\nClick and drag to control the cars.')
                start = False

            self.gameOver()

        pygame.quit() #quit program

    def clickObject(self): #when the window is clicked
       
        for car in range(len(self.cars)): #for every object
            if self.cars[car].rect.collidepoint(self.ev.pos): #if the coordinates of the click is within a rectangle
                self.cars[car].rectDrag = True #make it be in the air
                self.mouseX, self.mouseY = self.ev.pos #get current mouse position
                self.offsetX = self.cars[car].rect.x - self.mouseX #get different between mouse and rectangle coordinates
                self.offsetY = self.cars[car].rect.y - self.mouseY
                break #stop the loop

    def objectMidAir(self): #when the rectangle is being held (in air)
        for car in range(len(self.cars)): #for each rectangle
            if self.cars[car].rectDrag: #if the rectangle is in the air
                self.mouseX, self.mouseY = self.ev.pos #get mouse position
                self.cars[car].rect.x = self.mouseX + self.offsetX #get midair rectangle coordinates
                self.cars[car].rect.y = self.mouseY + self.offsetY

    def unclickObject(self): #when the rectangle is let go
        for car in range(len(self.cars)): #for each rectangle
            if self.cars[car].rectDrag: #if the rectangle is in the air

                square = 80 #one square is 80x80
                #get the 'row and column' of where the rectangle is
                makeshiftColumn, makeshiftRow = self.cars[car].rect.x / 80, self.cars[car].rect.y / 80
                decimalColumn, decimalRow = makeshiftColumn % 1, makeshiftRow % 1

                #depending on decimal part, whether to round up or round down
                #math.ceil will get rid of decimal part and round up
                #math.floor will get rid of decimal part and round down
                if decimalColumn >= 0.5:
                    jumpX = math.ceil(makeshiftColumn) * square
                else:
                    jumpX = math.floor(makeshiftColumn) * square   
                if decimalRow >= 0.5:
                    jumpY = math.ceil(makeshiftRow) * square
                else:
                    jumpY = math.floor(makeshiftRow) * square
                #jump is the proposed coordinate following multiples of 80
                #say the midair x-coordinate is something like 146, the jumpX will be 160

                #make a temporary list without the rectangle being held for rectangle comparison
                temporaryRectangles = self.cars * 1
                temporaryRectangles.remove(self.cars[car])

                #get the coordinates in the middle of the rectangle
                middleY = (self.cars[car].startY + self.cars[car].Y + self.cars[car].startY) / 2
                middleX = (self.cars[car].startX + self.cars[car].X + self.cars[car].startX) / 2
                moveAllowed = True #boolean for allowing the move

                if self.cars[car].orientation == "H":
                    countStart = int(self.cars[car].currentX /80) #get the starting square that is needed to be checked for collisions
                    countEnd = int(jumpX / 80) #get the last square that is needed to be checked for collision
                    if countStart > countEnd: #if start is bigger then swap
                        countStart, countEnd = countEnd, countStart
                    
                else: #same but just for vertical, swap X and Y
                    countStart = int(self.cars[car].currentY /80)
                    countEnd = int(jumpY / 80)
                    if countStart > countEnd:
                        countStart, countEnd = countEnd, countStart

                #depending on size of car, where to check for collision
                #okay i kind of lied about it being the 'middle', because for size 3 car
                #it would check 1/3 and 2/3 of the rectangle
                if self.cars[car].size == 2:
                    divisor = 2

                else:
                    divisor = 3

                for y in range(len(temporaryRectangles)): #for each rectangle
                    for z in range(countStart, countEnd+1): #for each square between the move
                        if self.cars[car].orientation == "H":
                            middleX = ((z*square) + (((z+1)*square)+(((self.cars[car].size-1)*square)))) / divisor #get the new middle coordinate
                            middleX2 = (((z*square) + (((z+1)*square)+(((self.cars[car].size-1)*square)))) / divisor) * (divisor-1) #for size 3 cars
                            #this monster if statement checks whether or not the 'middle' coordinate is between the coordinates of another rectangle or not
                            if ((temporaryRectangles[y].startX <= middleX <= (temporaryRectangles[y].X + temporaryRectangles[y].startX)) or (temporaryRectangles[y].startX <= middleX2 <= (temporaryRectangles[y].X + temporaryRectangles[y].startX))) and (temporaryRectangles[y].startY <= middleY <= (temporaryRectangles[y].Y + temporaryRectangles[y].startY)):
                                moveAllowed = False
                                #if there is a collision then it cannot move
                                break
                            else:
                                moveAllowed = True
                        else: #for vertical, same as above, just swap X and Y                            
                            middleY = ((z*square) + (((z+1)*square)+(((self.cars[car].size-1)*square)))) / divisor
                            middleY2 = (((z*square) + (((z+1)*square)+(((self.cars[car].size-1)*square)))) / divisor) * (divisor-1)
                            if (temporaryRectangles[y].startX <= middleX <= (temporaryRectangles[y].X + temporaryRectangles[y].startX)) and ((temporaryRectangles[y].startY <= middleY <= (temporaryRectangles[y].Y + temporaryRectangles[y].startY)) or (temporaryRectangles[y].startY <= middleY2 <= (temporaryRectangles[y].Y + temporaryRectangles[y].startY))):
                                moveAllowed = False
                                break
                            else:
                                moveAllowed = True
                                
                    if moveAllowed == False:
                            break
                #this semi-monster if statement checks whether the new proposed coordinates of the rectangle is within the limits or not
                #and also checks for collision
                if (self.cars[car].startLimitX <= jumpX < self.cars[car].endLimitX) and (self.cars[car].startLimitY <= jumpY < self.cars[car].endLimitY) and moveAllowed:
                    #update the necessary attributes of the rectangle
                    self.cars[car].rect = pygame.Rect(jumpX, jumpY, self.cars[car].X, self.cars[car].Y)
                    self.cars[car].currentX = jumpX
                    self.cars[car].currentY = jumpY
                    self.cars[car].startX = jumpX
                    self.cars[car].startY = jumpY
                    self.cars[car].rectDrag = False
                    self.turns += 1

                else: #if it doesnt match
                    #put the rectangle back to where the user moved it from
                    self.cars[car].rect = pygame.Rect(self.cars[car].currentX, self.cars[car].currentY, self.cars[car].X, self.cars[car].Y)
                    self.cars[car].rectDrag = False
                    messagebox.showwarning('Error','You cannot make that move.') #error message popup

    #make new car objects
    def makeCars(self): 

        #list of car objects
        self.cars = [] 

        for car in self.cars_list: 
            # colors in pygame have a different range, so make new colors
            color = (random.randrange(10, 250), random.randrange(10, 250), random.randrange(10, 250))
            # if car.orientation == 'H':
            #     print(car.coordinates_list[0][1])
            #     car.coordinates_list[0][1] = 7 - (car.coordinates_list[0][1])

            if car.type == 'X':
                self.cars.append(Car(car.orientation, car.length, car.coordinates_list[0][0] - 1, car.coordinates_list[0][1] - 2, (255,0,0), car.type))
        
            else:
                self.cars.append(Car(car.orientation, car.length, car.coordinates_list[0][0] - 1, car.coordinates_list[0][1] - 2, color, car.type))

    def gameOver(self): 

        #checks if starting coordinate of red/last car is at the winning position or not
        if self.cars[-1].startX == 320: 
            messagebox.showinfo('Congratulations!','You have completed the game!\nYou did it in %d moves!' % self.turns)
            self.inGame = False #cut the loop
