from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("pong")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


s.listen()
s.onkey(r_paddle.paddle_up, "Up")
s.onkey(r_paddle.paddle_down, "Down")
s.onkey(l_paddle.paddle_up, "w")
s.onkey(l_paddle.paddle_down, "s")

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(ball.move_speed)
    ball.move()

    # DETECTING COLLISION WITH THE WALLS
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECTING COLLISIONS WITH PADDLES
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # DETECTING RIGHT PADDLE DISMISS
    if ball.xcor() > 380:
        ball.refresh()
        ball.move()
        scoreboard.l_point()
    # DETECTING LEFT PADDLE DISMISS
    if ball.xcor() < -380:
        ball.refresh()
        ball.move()
        scoreboard.r_point()




s.exitonclick()
