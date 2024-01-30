#CSC235 Week 3 Assignment 3-1 AI Collaboration ChatGPT  Nicholas M James0927 ;-)

# Import of module random
import random
# Import of module os
import os
# Import of module time
import time

class FrogGame:
    # define of the console 
    def __init__(self,width=20, height=5):
        self.width
        self.height

    def __frog__(posistion, width=2, height=2):
        posistion
    
    def __fly__(position2, width, height):
        position2 = random.randint(0,width -1) and (0,height -1)
    def __obstacle__(position3, width, height):
        position3 = random.randint(0,width -1) and (0,height -1)
        # define of the what and how displayed in the console
    def display_game(self):
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen
        # for statement of the what in the vertical range of the console
        for y in range(self.height):
                # for statement of the what in the horizontal range of the console
            for x in range(self.width):
                    # if statement of the frog's position
                if [x, y] == self.frog.position:
                    # print statement of the frog's position
                        print("F", end=" ")
                    # elif statement of the fly's position
                elif [x, y] == self.fly.position:
                        # print statement of the fly's position
                    print("*", end=" ")
                    # elif statement of the obstacle's position
                elif [x, y] == self.obstacle.position:
                        # print statement of the obstacle's position
                    print("X", end=" ")
                    # else statement of the console
                else:
                        # print statement of the displayed in the console
                    print(".", end=" ")
        # print statment of the console
                print()
            # def frog movement in the console
    def move_frog(self, direction):
            # if statement of frog's movement up
        if direction == "UP" and self.frog.position[1] > 0:
            self.frog.position[1] -= 1
        # elif statement of frog's movement down
        elif direction == "DOWN" and self.frog.position[1] < self.height - 1:
            self.frog.position[1] += 1
        # elif statement of frog's movement left
        elif direction == "LEFT" and self.frog.position[0] > 0:
            self.frog.position[0] -= 1
        # elif statement of frog's movement right
        elif direction == "RIGHT" and self.frog.position[0] < self.width - 1:
            self.frog.position[0] += 1

    def play_game(self):
        # print welcome 
        print("Welcome to the Frog Catching Game!")
        # while loop for display of console
        while True:
            # variable game display 
            self.display_game()
            # input statement for action direction of movement 
            action = input("Enter a direction (UP/DOWN/LEFT/RIGHT) or (Q) to quit): ")
            # if statment for action quit
            if action == "Q":
                # print statement thanking user for playing
                print("Quitting the game. Thanks for playing!")
                # break out of loop
        # var for action of frog's movement 
            self.move_frog(action)
        # if statement for frog's position and fly's position
            if self.frog.position == self.fly.position:
                # print statement Congratulating user for cathing a fly
                print("Congratulations! You caught a fly!")
                # variable for fly's position displayed in console
                self.fly.position = [random.randint(0, self.width - 1)]; self.obstacle.position = [random.randint(0, self.height - 1)]
                # if statement for frog's position and obstacle's position
            elif self.frog.position == self.obstacle.position:
                # print statement when Obstacle is Hit
                print("Oops! You hit an obstacle. Game over!")
                # break out of loop
            break
#time.sleep(0.5)  # Pause for a moment before updating the display
# if statment for class import frog game play
if __name__ == "__main__":
    game = FrogGame()
    game.play_game()