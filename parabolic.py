# Código modificado
# David Damián Galán
# Angélica Sofía Ramírez Porras

from random import randrange  # Importa la función randrange
from turtle import *  # Importa las fuciones de turtle
from freegames import vector  # Importa vector

ball = vector(-200, -200)  # Posición inicial de la bola roja
speed = vector(0, 0)  # Velocidad inicial
targets = []  # Al inicio no hay targets


def tap(x, y):
    """
    Responde a que los clicks sea hacia donde apunta la bola roja
    x = Posición en eje x
    y = Posición en eje y
    """
    if not inside(ball):  # La bola está fuera de la pantalla
        # Hace aparecer la bola y regula su velocidad
        ball.x = -199
        ball.y = -199
        # Aumenta la velocidad
        speed.x = (x + 200) / 10  # Antes dividía entre 25
        speed.y = (y + 200) / 10  # Antes dividía entre 25


def inside(xy):
    """
    Determina si la posición se encuentra dentro de la ventana
    xy = Posición o coordenada a evaluar
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """
    Dibujar la bola y los targets
    """
    clear()  # Elimina el contenido de la pantalla

    for target in targets:  # Loop de los targets
        goto(target.x, target.y)  # Se mueve a la posición de target
        dot(20, 'blue')  # Crea un punto en la posición de target

    if inside(ball):  # La pelota se encuentra dentro de la ventana
        goto(ball.x, ball.y)  # Se mueve a la posición de la pelota
        dot(6, 'red')  # Crea un punto en la posición de la pelota

    update()  # Reflejar los cambios realizados


def move():
    """
    Realiza el movimiento de la pelota y de los targets
    """
    if randrange(40) == 0:  # Crea un target de manera aleatoria
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)  # Agrega el target a la lista de targets

    for target in targets:  # Loop de movimiento en x de targets
        target.x -= 2.5  # Estaba en 0.5

    if inside(ball):  # Movimiento de la pelota
        # Cambia velocidad en y
        speed.y -= 1  # Estaba en 0.35
        # Realiza el movimiento de la pelota con el parámetro speed
        ball.move(speed)

    # Crea una copia de targets
    dupe = targets.copy()
    # Elimina todos los targets
    targets.clear()

    for target in dupe:  # Loop de targets
        # Verifica que la pelota esté a mayor distancia de 13 al target
        if abs(target - ball) > 13:
            # Agrega el target
            targets.append(target)

    # Dibuja los obstáculos y la pelota
    draw()

    for i in range(len(targets)):  # Itera sobre la lista de targets
        # Verifica si el target se ha salido de la ventana
        if not inside(targets[i]):
            y = targets[i].y  # En caso afirmativo, copia la coordenada y
            # Finalmente reubica el target en la posicion más a la derecha
            targets[i] = vector(200, y)
            # El juego nunca termina al no existir return

    ontimer(move, 50)  # Llama a la función de movimiento cada 50 milisegundos


setup(420, 420, 370, 0)  # Configura dimensiones de la ventana
hideturtle()  # Esconde el ícono de turtle
up()  # Levanta la pluma para no dibujar mientras se mueve
tracer(False)  # Oculta la animación de dibujo
onscreenclick(tap)  # Sincroniza eventos de clicks con el juego
move()  # Inicia el juego

done()  # Termina el juego
