import turtle
from time import sleep, perf_counter
from math import sin, cos, radians, sqrt

g = 9.81

gui = turtle.Screen()
gui.title("Parabolic Motion Simulator")

def set_env():
    ground = turtle.Turtle()
    ground.hideturtle()
    ground.penup()
    
    ground.goto(-500, -200)
    ground.color('green')
    ground.pendown()
    ground.setpos(500, -200)

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
    gui = turtle.Screen()

    v = gui.numinput("Velocità iniziale", "Inserire la velocità con cui il proiettile viene sparato: ", 10, 1, 100)
    # h = gui.numinput("Altezza iniziale", "Inserire l'altezza da cui proiettile viene sparato: ", 10, 1, 100)
    teta = gui.numinput("Angolo di lancio", "Inserire l'angolo con cui il proiettile viene sparato: ", 45, 0, 360)
    
    return v, teta

obj = turtle.Turtle()
text_velocity = turtle.Turtle()
text_distance = turtle.Turtle()
text_time = turtle.Turtle()

def aggiorna_xyv(vx, vy, delta_t):
    x = obj.xcor() + vx*delta_t

    y = (-1/2) * g * (delta_t ** 2) + vy*delta_t + obj.ycor()

    vy = vy - g * delta_t

    return x, y, vy


def move_proiettile(v0, teta):
    text_velocity.hideturtle()
    text_velocity.penup()
    text_velocity.goto(-500, 200)  

    text_distance.hideturtle()
    text_distance.penup()
    text_distance.goto(-500, 250)

    text_time.hideturtle()
    text_time.penup()
    text_time.goto(-500, 300)

    set_proiettile()

    vx = v0*cos(teta)
    vy = v0*sin(teta)

    tempo_totale = 0

    while obj.ycor() >= -200:
        tempo_totale += 0.1
        x, y, vy = aggiorna_xyv(vx, vy, 0.1)
        
        text_velocity.clear()
        text_velocity.write(f"Velocity: {round(sqrt(vx ** 2 + vy ** 2), 3)} m/s", align="left", font=("Arial", 10, "normal"))

        text_distance.clear()
        text_distance.write(f"Distanza percorsa: {round(abs(-500 - x), 3)} meters", align="left", font=("Arial", 10, "normal"))
        
        text_distance.clear()
        text_distance.write(f"Distanza percorsa: {round(abs(-500 - x), 3)} meters", align="left", font=("Arial", 10, "normal"))
        
        text_time.clear()
        text_time.write(f"Tempo in volo: {tempo_totale} secondi", align="left", font=("Arial", 10, "normal"))
        obj.goto(x, y)

if __name__ == "__main__":
    set_env()

    velocita, angolo = take_input()

    
    move_proiettile(velocita, radians(angolo))
    gui.mainloop()