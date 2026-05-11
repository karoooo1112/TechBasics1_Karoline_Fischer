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
color('random')
fillcolor('yellow')
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

colors = ["#483D8B", "#87CEFA", "#8470FF", "#20B2AA", "90EE90", "#9ACD32", "F08080", "#FF8247", "#FF82AB", "#E066FF", "#9F79EE", "#DA70D6", "#551A8B")

def repeat(times: int=50):
    for i in range(50):
        pencolor(random.choice(colors))
        fillcolor(random.choice(colors))
        stars()

if __name__ == "__main__":
    repeat()

    done()
