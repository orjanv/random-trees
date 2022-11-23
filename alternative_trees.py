from turtle import *
from random import *
from time import sleep
import sys
import os

# Run this program as python3 alternative_trees.py FILENAME FOLDER
# For example: python3 alternative_trees.py 1 trees
# This will draw a tree and save it as 1.ps in a folder named trees
# Use the run.sh shell script to run this python script multiple times
# and convert each file to .png and a bigger collage in the end.


# Sirkler
def circle_leaves(size):
    color("Green")
    pendown()
    begin_fill()
    circle(size)
    end_fill()
    penup()

# Leavs som skyer
def bubble_leaves(size):
    color(LEAVES_COLOR)
    setheading(0)
    pendown()
    begin_fill()
    circle(size,180)
    setheading(90)
    circle(size*1.33,180)
    setheading(180)
    circle(size,180)
    setheading(270)
    circle(size*1.33,180)
    end_fill()
    penup()


# to halvbue leavs
def leaves(size):
    pendown()
    color(LEAVES_COLOR)
    begin_fill()
    circle(size,70)
    left(110)
    circle(size,70)
    end_fill()
    penup()

def drawBranch(num_branches, pen_size, branch_length, start_posx, start_posy, d):
    d += 1
    for i in range(num_branches):
        penup()
        setpos(start_posx,start_posy)
        pensize(pen_size)
        setheading(randrange(0, 180, 30))
        pendown()
        color(BRANCH_COLOR)
        branch_arc = randrange(20,30)
        
        # tegne grenene, tilfeldig rette eller buet
        if randrange(0,10) > 5:
            forward(branch_length)
        else:
            if randrange(0,10) > 5:
                circle(-branch_length,branch_arc)
            else:
                circle(branch_length,branch_arc)
        
        # Ved slutten av en gren ytterst
        if 1 < d < 3:
            branch_length = randrange(150,300,10)

        if 3 < d < 4:
            branch_length = randrange(100,200,10)

        if 4 < d < 6:
            branch_length = randrange(50,100,10)

        if d > 4:
            #print("reached end", d)
            #bubbles(7)
            leaves(20)
        else:
            branchx, branchy = pos()
            print(branch_length,d, num_branches)
            drawBranch(num_branches, pen_size/PHI, branch_length/PHI, branchx, branchy, d)

    
# Some setup
bgcolor("#d1cbba")
BRANCHES = 6
DEPTH = 0
PHI = 1.618034
BRANCH_COLOR_LIST = ["#29221b", "#5e5224", "#a15c21", "#c6cacd"]
BRANCH_COLOR = choice(BRANCH_COLOR_LIST)
LEAVES_COLOR_LIST = ["#5c776c", "#e5cff3", "white", "#988b71", "#5291a0"]
LEAVES_COLOR = choice(LEAVES_COLOR_LIST) 
setup(1600, 1600)
speed(0)
tracer(0, 0)
hideturtle()

try:
    save_path = sys.argv[2] + '/'
    filename = sys.argv[1] + ".ps"
    completeName = os.path.join(save_path, filename)
except:
    completeName = "test.ps"

# Draw the log
penup()
setpos(0, -500)
color(BRANCH_COLOR)
pensize(40)
setheading(90)
pendown()
forward(300)
# start branching
topx, topy = pos()
drawBranch(BRANCHES, 30, 250, topx, topy, DEPTH)

# save and quit
update()
getcanvas().postscript(file=completeName)
#exitonclick()
bye()

