
def up():
    global direction
    direction= UP
    print("you pressed the up key")

def down():
    global direction
    direction= DOWN
    print("you pressed the down key")

def left():
    global direction
    direction= LEFT
    print("you pressed the left key")

def right():
    global direction
    direction= RIGHT
    print("you pressed the right key")

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    food_position=(food_x, food_y)
    food_pos.append(food_position)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
        
        

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
        

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    if snake.pos() in food_pos:
         food_ind= food_pos.index(snake.pos())
         food.clearstamp(food_stamps[food_ind])
         food_pos.pop(food_ind)
         food_stamps.pop(food_ind)
         print("you have eaten the food")
         make_food()

    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    

    new_pos= snake.pos()
    new_x_pos= new_pos[0]
    new_y_pos= new_pos[1]
 
    
    if new_x_pos >= RIGHT_EDGE:
        print ("you hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print ("you hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print (" you hit the down edge! Game over!")
        quit()
    global food_stamps, food_pos
    if pos_list[-1] in pos_list[0:-1]:
        print( "you ate yourself" )
        quit()
     

    
    turtle.ontimer(move_snake,TIME_STEP)




####################################

import turtle
import random

turtle.bgcolor("pink")
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X+50,SIZE_Y+50)
turtle.pencolor("red")
edge= turtle.clone()
edge.shape('turtle')
edge.penup()
edge.goto(-400,250)
edge.pendown()
edge.goto(400,250)
edge.goto(400,-250)
edge.goto(-400,-250)
edge.goto(-400, 250)

turtle.penup()
edge.hideturtle()

SQUARE_SIZE= 20
START_LENGTH= 1

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
UP_EDGE= 250
DOWN_EDGE= -250
RIGHT_EDGE= 400
LEFT_EDGE= -400

    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

move_snake()

turtle.register_shape ("apple.gif")
food= turtle.clone()
food.shape("apple.gif")
food_pos= [ (100,100), (-100,100), (-100,-100), (100,-100) ]
food_stamps=[]

for this_food_pos in food_pos:
    x_pos= this_food_pos[0]
    y_pos= this_food_pos[1]
    food.goto(x_pos, y_pos)
    new_stamps =food.stamp()
    food_stamps.append(new_stamps)

food.hideturtle()


    
    
    

 

