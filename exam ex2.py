# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:17:45 2023

@author: twixt
"""

class Bug:
    #initialize the bug with postion and direction to the right(True)
    def __init__(self, initialPosition):
        self.initialPosition = initialPosition
        self.direction = True


    #checks the self.direction for true or false and switches it to the opposite
    def turn(self):
        if self.direction == True:
            self.direction = False
            print("\nThe bug is currently moving to the left")

        elif self.direction == False:
            self.direction = True
            print("\nThe bug is currently moving to the right")

    
    #checks direction and move it 1+ or 1-
    def move(self):
        if self.direction == True:
            self.initialPosition += 1
            self.getPosition()
        else:
            self.initialPosition -= 1
            self.getPosition()
            
    def changeStepper(self, newValue):
        self.stepper = newValue

    def getPosition(self):
        print("\nPosition:", self.initialPosition)
    
    def main():
        #checks if initialPosition is a whole number
        x = True
        while x == True:
            initialPosition = input("What would you want the initial postion to be? ")
            if initialPosition.isnumeric() == True:
                initialPosition = int(initialPosition)
                break
            else:
                print("You did not write a whole number")

        bugsy = Bug(initialPosition)
        bugsy.getPosition()
        #menu which moves, turns and quits the prgram
        keepPlaying = True
        while keepPlaying == True:
            
            action = input("1: Move\n2: Switch direction\n3: Stop\n:")
            
            if action == "1":
                bugsy.move()
            elif action == "2":
                bugsy.turn()
            elif action == "3":
                keepPlaying = False
                print("\nStopped")
            else:
                print("\nYou have to write 1 or 2 or 3")

                

Bug.main()