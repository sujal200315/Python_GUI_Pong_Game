
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard, Centerline


screen = Screen()

#screen.bgcolor("black")
screen.bgpic("ping-pong-table.gif")
screen.setup(900,600)
screen.title("Pong.Game")
screen.tracer(0)

centerline = Centerline()
r_paddle = Paddle((420,0))
l_paddle = Paddle((-420,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.ycor() < 390:
        ball.bounce_x()

    # Detect R paddle misses the ball
    if ball.xcor() > 420:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses the ball
    if ball.xcor() < -420:
        ball.reset_position()
        score.r_point()


screen.exitonclick()