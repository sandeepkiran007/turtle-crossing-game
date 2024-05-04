from turtle import Turtle
import random
COLORS = ['green', 'yellow', 'violet', 'red', 'orange', 'purple']
START_MOVE = 5
MOVE_INCREMENT = 10
class Cars:
    def __init__(self):
        self.cars = []
        self.car_speed = START_MOVE

    def generate_random_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            car = Turtle()
            car.shape('square')
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(390, random.randint(-200, 200))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT


