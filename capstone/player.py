from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def go_down(self):
        if self.ycor() > -280:
            self.backward(10)
    
    def go_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - 10, self.ycor())
    
    def go_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + 10, self.ycor())

    def go_to_start(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        return self.ycor() > 285
