import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE= 20
START_LENGTH= 5

pos_list= []
stamp_list= []
food_pos= []
food_stamps= []

snake= turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos= snake.pos()[0]
    y_pos= snake.pos()[1]
    x_pos= x_pos + SQUARE_SIZE

    my_pos= (x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_ID= snake.stamp()
    stamp_list.append(stamp_ID)
    
    
UP_ARROW = "Up" ​ #Make sure you pay attention to upper and lower
#case
LEFT_ARROW = "Left" ​ #Pay attention to upper and lower case
DOWN_ARROW = "Down" ​ #Pay attention to upper and lower case
RIGHT_ARROW = "Right" ​ #Pay attention to upper and lower case
TIME_STEP = 100 ​ #Update snake position after this many
#milliseconds
SPACEBAR = "space" ​ # Careful, it's not supposed to be
capitalized!
UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN=1
LEFT=2
RIGHT=3
direction=up

def up():
    global direction
    direction= UP
    
