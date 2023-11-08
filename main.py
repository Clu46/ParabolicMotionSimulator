import turtle as obj
from time import sleep, perf_counter
from math import sin, cos, radians

"""

Data la velocità iniziale in metri al secondo, simulare la traiettoria di un proiettile sparato con la velocità iniziale presa in input

delta_t = 0.01 secondi

#
#       x = x0 + v0 * cos(a) * delta_t
#       y = -1/2 * g * (delta_t ^ 2) + v0 * sin(a) + y0
#


"""

obj.title("Simulazione sparo proiettile")

g = 9.81

def set_env():
    terrain = obj

    terrain.title("Simulazione proiettile")
    terrain.hideturtle()
    terrain.penup()
    
    terrain.goto(-500, -200)
    terrain.color('green')
    terrain.pendown()
    terrain.setpos(500, -200)

def set_proiettile(y):
    obj.hideturtle()
    obj.penup()

    obj.goto(-500, 0)
    
    obj.color('black')
    obj.shape("circle")

    obj.shapesize(0.3, 0.3, 0.3)
    
    obj.showturtle()
    obj.pendown()

def take_input():
    v = obj.numinput("Velocità iniziale", "Inserire la velocità con cui il proiettile viene sparato: ", 10, 1, 100)
    # h = obj.numinput("Altezza iniziale", "Inserire l'altezza da cui proiettile viene sparato: ", 10, 1, 100)
    teta = obj.numinput("Angolo di lancio", "Inserire l'angolo con cui il proiettile viene sparato: ", 45, 0, 360)
    
    return v, teta



def aggiorna_xyv(vx, vy, teta, delta_t):



    x = obj.xcor() + vx*delta_t

    y = (-1/2) * g * (delta_t ** 2) + vy*delta_t + obj.ycor()

    vy = vy - g * delta_t

    return x, y, vy


def move_proiettile(v0, teta):
    vx = v0*cos(teta)
    vy = v0*sin(teta)


    while obj.ycor() >= 0:
        x, y, vy = aggiorna_xyv(vx, vy, teta, 0.01)

        obj.goto(x, y)

if __name__ == "__main__":
    set_env()

    velocita, angolo = take_input()

    
    move_proiettile(velocita, radians(angolo))
    obj.done()