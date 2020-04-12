#Pong

import turtle

screen = turtle.Screen()
screen.title("Flashback Pong")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
score_b = 0

# Paddle B (The paddle we are changing to the bottom of screen)
paddle_b = turtle.Turtle()
paddle_b.speed(0) #paddle speed 
paddle_b.shape("square")
paddle_b.color("red") #changed paddle B to red
paddle_b.shapesize(stretch_wid=1,stretch_len=5)
paddle_b.penup()
paddle_b.goto(0, -200) #location of paddle B

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black") #changed ball color to black
ball.penup()
ball.goto(0, 200)
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(score_b), align="center", font=("Courier", 24, "normal")) #code for title and scoreboard

def paddle_b_left():
    x = paddle_b.xcor()
    x += -30
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 30
    paddle_b.setx(x)


# Keyboard binding
screen.listen()
screen.onkeypress(paddle_b_left, "Left")
screen.onkeypress(paddle_b_right, "Right")

# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
            
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dx *= -1
    
    #new code for ball to bounce off side walls
    elif ball.xcor() > 400:
        ball.setx(400)
        ball.dx *= -1

    elif ball.xcor() < -400:
        ball.setx(-400)
        ball.dx *= -1

    #Paddle and ball collisions 
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 50 and ball.xcor() > paddle_b.xcor() - 50:
        ball.sety(-190)
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Score: {}".format(score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.ycor() < -205: #endgame
        pen.clear()
        pen.write("GAME OVER! Restart Terminal! Final Score: {}".format(score_b), align="center", font=("Courier", 24, "normal"))
