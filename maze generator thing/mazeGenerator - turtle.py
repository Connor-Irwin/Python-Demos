from random import randint
import turtle

moveProbability = 5

turtle.speed("fastest")

while True:
    turn = randint(0, 2 + moveProbability)

    if turn == 0:
        turtle.left(90)

    elif turn == 1:
        turtle.right(90)

    elif turn == 2:
        turtle.right(180)

    # tries to keep the turtle facing the center and near the center
    for i in range(int(turtle.distance(0, 0))):
        if turtle.towards(0, 0) != 0:
            turn = randint(0, 1 + moveProbability)

    if turn > 1:
        turtle.forward(10)
