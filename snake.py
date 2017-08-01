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
    
    
UP_ARROW = "Up"  #Make sure you pay attention to upper and lower
#case
LEFT_ARROW = "Left"  #Pay attention to upper and lower case
DOWN_ARROW = "Down"  #Pay attention to upper and lower case
RIGHT_ARROW = "Right"  #Pay attention to upper and lower case
TIME_STEP = 100  #Update snake position after this many
#milliseconds
SPACEBAR = "space"  # Careful, it's not supposed to be
#capitalized!
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

def up():
    global direction
    direction= UP
    move_snake()
    print("you pressed the up key")

def down():
    global direction
    direction= DOWN
    move_snake()
    print("you pressed the down key")

def left():
    global direction
    direction= LEFT
    move_snake()
    print("you pressed the left key")

def right():
    global direction
    direction= RIGHT
    move_snake()
    print("you pressed the right key")
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos= snake.pos()
    x_pos= my_pos[0]
    y_pos= my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")

#4. Write the conditions for UP and DOWN on your own
##### YOUR CODE HERE
#Stamp new element and append new stamp in list
#Remember: The snake position changed - update my_pos()
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

