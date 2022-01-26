from random import randint
from PIL import Image
from math import sqrt

class Turtle:
    def __init__(self):
        self.location = (0, 0)
        self.direction = 0

    def fixDirection(self):
        while self.direction >= 360:
            self.direction -= 360

        while self.direction < 0:
            self.direction += 360

    # currently only supports directions that are a multiple of 90 or 0
    def forward(self, distance):
        if self.direction == 0:
            self.location = (self.location[0], self.location[1] + distance)
        elif self.direction == 90:
            self.location = (self.location[0] + distance, self.location[1])
        elif self.direction == 180:
            self.location = (self.location[0], self.location[1] - distance)
        elif self.direction == 270:
            self.location = (self.location[0] - distance, self.location[1])

    def left(self, degrees):
        self.direction -= degrees
        self.fixDirection()

    def right(self, degrees):
        self.direction += degrees
        self.fixDirection()

    def distance(self, locX, locY):
        return sqrt(pow(locX - self.location[0], 2) + pow(locY - self.location[1], 2))

moveProbability = input("Move probability (blank = default = 10): ")
if moveProbability == "":
    moveProbability = 10

repetitions = input("Repetitions (blank = default = 1000000): ")
if repetitions == "":
    repetitions = 1000000

moveProbability = int(moveProbability)
repetitions = int(repetitions)

turtle = Turtle()

locations = {(0, 0)}

print("Generating (this may take a while)...")

for i in range(repetitions):
    turn = randint(0, 2 + moveProbability)

    if turn == 0:
        turtle.left(90)

    elif turn == 1:
        turtle.right(90)

    elif turn == 2:
        turtle.right(180)

    '''
    # tries to keep the turtle facing the center and near the center
    for e in range(int(turtle.distance(0, 0))):
        if turtle.direction != 0:
            turn = randint(0, 2 + moveProbability)
    '''

    if turn > 2:
        oldX = turtle.location[0]
        oldY = turtle.location[1]
        
        turtle.forward(2)

        newX = turtle.location[0]
        newY = turtle.location[1]

        locations.add(turtle.location)

        if oldX > newX:
            locations.add((newX + 1, newY))
        if oldX < newX:
            locations.add((newX - 1, newY))
        if oldY > newY:
            locations.add((newX, newY + 1))
        if oldY < newY:
            locations.add((newX, newY - 1))

smallestX = 0
smallestY = 0
largestX = 0
largestY = 0

for item in locations:
    if item[0] < smallestX:
        smallestX = item[0]
    elif item[0] > largestX:
        largestX = item[0]
    if item[1] < smallestY:
        smallestY = item[1]
    elif item[1] > largestY:
        largestY = item[1]

newLocations = {(0, 0)}

for i in range(len(locations)):
    item = locations.pop()
    
    newLocations.add((item[0] + abs(smallestX), item[1] + abs(smallestY)))

img = Image.new(mode="RGB", size=(largestX + abs(smallestX) + 1, largestY + abs(smallestY) + 1), color="black")
pixels = img.load()

for location in newLocations:
    pixels[location] = (255, 255, 255)

# adds start dot to maze
pixels[abs(smallestX), abs(smallestY)] = (255, 0, 0)

# adds end dot to maze
#pixels[newLocations[len(newLocations) - 1]] = (0, 0, 255)

img.save("mp=" + str(moveProbability) + " r=" + str(repetitions) + ".jpg", optimize=True, quality=100)
img.show()
