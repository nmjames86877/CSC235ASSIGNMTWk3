#CSC235 Week 3 Assignment 3-1 AI Collaboration ChatGPT  Nicholas M James0927 ;-)

# Import of module random
import random
# Import of module os
import os

class FrogGame:
    def __init__(self, width=20, height=5): # def of console
        self.width = width # def of width
        self.height = height # def of height
        self.frog = {"position": [0, 0]} # def of frog position
        self.fly = {"position": [random.randint(0, width - 1), random.randint(0, height - 1)]} # def of fly position
        self.obstacle = {"position": [random.randint(0, width - 1), random.randint(0, height - 1)]} # def of obstacle

    def display_game(self): # def of gameplay
        os.system("cls" if os.name == "nt" else "clear") # def of console
        for y in range(self.height): # for statement for vertical or console height
            for x in range(self.width): # for statement for horizontal or console width
                if [x, y] == self.frog["position"]: # if statment of frog position in console
                    print("F", end=" ") # print statment for frog posistion
                elif [x, y] == self.fly["position"]: # elif statment for fly position
                    print("*", end=" ") # print statment for fly position
                elif [x, y] == self.obstacle["position"]: # elif statment for obstacle position
                    print("X", end=" ")# print statment for obstacle
                else: # else statement for gameplay
                    print(".", end=" ") # print statment for ending gameplay
            print() # print statment for console

    def move_frog(self, direction): # def of frog gameplay movement
        if direction == ("UP") and self.frog["position"][1] > 0: # if statement for frog movement up using UpperCase "UP"
            self.frog["position"][1] -= 1 # value of if statement for movement of frog up using UpperCase "UP"
        elif direction == ("u") and self.frog["position"][1] > 0: ### attempted to add another elif statement option for frog movement using lowercase "u"
            self.frog["position"][1] -= 1 # value of if statement for movement of frog up using lowercase "u"
        elif direction == ("DOWN") and self.frog["position"][1] < self.height - 1: # elif statment for frog movement down using UpperCase "DOWN"
            self.frog["position"][1] += 1 # value of elif statment for movement of frog down using UpperCase "DOWN"
        elif direction == ("d") and self.frog["position"][1] < self.height -1: ### attempted to add another elif statement option for frog movement using lowercase "d"
            self.frog["position"][1] += 1 # value of elif statment for movement of frog down using lowercase "d"
        elif direction == ("LEFT") and self.frog["position"][0] > 0: # elif statment for frog movement using UpperCase "LEFT"
            self.frog["position"][0] -= 1 # value of elif statment for movement of frog left using UpperCase "LEFT"
        elif direction == ("l") and self.frog["position"][0] > 0: ### attempted to add another elif statement option for frog movement using lowercase "l"
            self.frog["position"][0] -= 1 # value of elif statment for movement of frog left using lowercase "l"
        elif direction == ("RIGHT") and self.frog["position"][0] < self.width - 1: # elif statement for frog movement right using UpperCase "RIGHT"
            self.frog["position"][0] += 1 # value of elif statement for movement of frog right using UpperCase "RIGHT"
        elif direction == ("r") and self.frog["position"][0] < self.width - 1: ### attempted to add another elif option for frog movement using lowercase "r"
            self.frog["position"][0] += 1 # value of elif statement for movement of frog right using lowercase "r"

    def play_game(self):# def of play game
            self.display_game() # value for displaygame in console
            action = input("Enter a direction (UP or u /DOWN or d /LEFT or l /RIGHT or r) or (Q) to quit: ") # input value of users selection for frog movement up, down, left, right or quit gameplay
            if action == "Q": # if statement for action 
                print("Quitting the game. Thanks for playing!") # print statement to user printing game
                exit() # exit program

            self.move_frog(action) # value frog movement in display console

            if self.frog["position"] == self.fly["position"]: # if statement of frog's position catching fly's position in display console
                print("Congratulations! You caught a fly!") # print statement congratulating user for catching fly
                self.fly["position"] = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)] # value of fly's position in display console
                self.obstacle["position"] = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)] # value of obstacle's position in display console
            elif self.frog["position"] == self.obstacle["position"]: # elif statement of frog's position running into obstacle in display console
                print("Oops! You hit an obstacle. Game over!") # print statement to user for hitting obstacle
                exit() # exit program

if __name__ == "__main__": # if statement of init frog gameplay
    game = FrogGame() # value FrogGame
    game.play_game() # value play FrogGame