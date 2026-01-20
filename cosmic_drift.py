import turtle
import math
import random
import winsound

# Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("ASSETS/Space 3.gif")
wn.title("Cosmic Drift")
# wn.tracer(2)


# Boundary
mypen = turtle.Turtle()
mypen.color("white")
mypen.up()
mypen.goto(-300, -300)
mypen.pendown()
mypen.pensize(3)

for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("black")
player.shape("turtle")
player.penup()
player.speed(0)
speed = 1

# Score
score = 0

# Create goals
maxGoals = 7
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].shape("circle")
    goals[count].color("red")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

# Def function
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def  increasespeed():
    global speed
    speed +=1

def decreasespeed():
    global speed
    speed -=0.5
       
def isCollision(t1, t2):
     d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2)) + (math.pow(t1.ycor() - t2.ycor(),2))
     if d < 20:
         return True
     else:
         return False

# Controls
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)


    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        winsound.PlaySound("ASSETS/Boundary.wav", winsound.SND_ASYNC)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        winsound.PlaySound("ASSETS/Boundary.wav", winsound.SND_ASYNC)

# Move goals
    for count in range(maxGoals):
        goals[count].forward(3)
    
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
           

# Collision Check
        if isCollision(player, goals[count] ):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            winsound.PlaySound("ASSETS/Score.wav", winsound.SND_ASYNC)
            score +=1
            # Score
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score : %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))