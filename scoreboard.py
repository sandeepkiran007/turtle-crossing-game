from turtle import Turtle
FONT = ('Courier', 30, 'bold')
FONT_GAME_OVER = ('Courier', 50, 'bold')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()

    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-350, 270)
        self.write(f"Level:{self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('white')
        self.write(f"Game Over!", align='center', font=FONT_GAME_OVER)


