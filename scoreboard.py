from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100,220)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)


    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

class Centerline(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(35, 0.2)
        self.penup()


