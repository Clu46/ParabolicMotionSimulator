import turtle as obj
from time import sleep, perf_counter
from math import sin, cos, radians

g = 9.81

def set_env():
    terrain = obj

    
    terrain.title("Parabolic Motion Simulator")
    terrain.hideturtle()
    terrain.penup()
    
    terrain.goto(-500, -200)
    terrain.color('green')
    terrain.pendown()
    terrain.setpos(500, -200)

def set_proiettile():
    obj.hideturtle()
    obj.penup()

    obj.goto(-500, 0)
    
    obj.color("black")
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
    set_proiettile()

    vx = v0*cos(teta)
    vy = v0*sin(teta)


    while obj.ycor() >= -200:
        x, y, vy = aggiorna_xyv(vx, vy, teta, 0.01)
        
        obj.write("Home = ", True, align="center")
        
        obj.goto(x, y)

if __name__ == "__main__":
    set_env()

    velocita, angolo = take_input()

    
    move_proiettile(velocita, radians(angolo))
    obj.mainloop()