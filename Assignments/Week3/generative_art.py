import random 
from turtle import * 

width = 400 
height = 600

#screen = turtle.screen()
#screen.setup(width=width, height=height)
#is useless


tracer(0, 0)
hideturtle()
speed(0)
pensize(2)

def random_spot():
    half_w = width // 2 
    half_h = height // 2 

    x = random.randint (-half_w, half_w)
    y = random.randint (-half_h, half_h)
    return x, y 

def stars():

    penup()
    start_x, start_y = random_spot()
    goto(start_x, start_y)
    pendown()

    begin_fill()
    while True:
        forward(200)
        left(170)
        if distance(start_x, start_y) < 1:
            break 
    end_fill()

    update()

colors = ["#483d8b", "#87cefa", "#8470ff", "#20b2aa", "#90ee90", "#9acd32", "#f08080", "#ff8247", "#ff82ab", "#e066ff", "#9f79ee", "#da70d6", "#551a8b"]

def repeat(times: int=50):
    for i in range(times):
        pencolor(random.choice(colors))
        fillcolor(random.choice(colors))
        stars()

if __name__ == "__main__":
    repeat()

    done()
