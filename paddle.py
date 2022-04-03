from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(paddle_position)
        self.speed("fastest")

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

