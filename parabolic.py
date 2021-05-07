from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y): 
    """
Responde a que los clicks sea hacia donde apunta la bola roja

"""
    if not inside(ball): # Regula la velocidad de la bola
        ball.x = -199  # Estaba en -199
        ball.y = -199  # Estaba en -199
        speed.x = (x + 200) / 10 # Antes dividía entre 25 
        speed.y = (y + 200) / 10 # Antes dividía entre 25  

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2.5 # estaba en 0.5

    if inside(ball):
        speed.y -= 1 # estaba en 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()