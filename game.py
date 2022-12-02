from tkinter import *
import random

GAME_WIDTH=1000
GAME_HEIGHT=700
SPEED =400
SPACE_SIZE =25
BODY_PARTS =4
SNAKE_COLOR ="yellow"
FOOD_COLOR ="red"


class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)


class Food:
    def __init__(self):
        x= random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y= random.randint(0, (GAME_HEIGHT/ SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates =[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")


def next_turn():
    pass


def change_direction():
    pass


def check_collisions():
    pass


def game_over():
    pass


window = Tk()

score = 0
direction ="down"


label = Label(window, text="Score :{}".format(score), font=("consolas", 30))
label.pack()

canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH, background="black")
canvas.pack()

food = Food()
snake = Snake()

window.mainloop()
