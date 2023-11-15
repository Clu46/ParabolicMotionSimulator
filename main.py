import turtle
from math import sin, cos, radians, sqrt

# Parabolic Motion Simulator
# 1 pixel = 1 metro
# Nessun attrito considerato

gui = turtle.Screen()
gui.setup(width=1.0, height=1.0)            # Inizializzo la GUI a full-screen
gui.title("Parabolic Motion Simulator")     # Inizializzo il titolo della GUI

obj = turtle.Turtle()                       # obj è l'oggetto che rappresenta il proiettile nella GUI
obj.speed(11)                               # Imposto la velocità di scrittura più veloce al proiettile        

text_velocity = turtle.Turtle()             # Inizializzo la turtle che si occupa di scrivere la velocità a schermo
text_distance = turtle.Turtle()             # Inizializzo la turtle che si occupa di scrivere la distanza percorsa a schermo
text_time = turtle.Turtle()                 # Inizializzo la turtle che si occupa di scrivere il tempo percorso in volo a schermo

g = 9.81                                    # Accelerazione di gravità (m / s^2)

def set_env():
    ground = turtle.Turtle()                # Inizializzo la turtle che si occupa di scrivere il terreno
    ground.speed(11)
    ground.hideturtle()
    ground.penup()
    
    ground.goto(-500, -200)                 # Coordinate del terreno
    ground.color('green')
    ground.pendown()
    ground.goto(500, -200)                  # Il terreno è lungo 1000px = 1000 metri

def set_proiettile():
    obj.hideturtle()
    obj.penup()

    obj.goto(-500, 0)                       # Coordinate da cui viene sparato il proiettile
    
    obj.color("black")
    obj.shape("circle")                     # Forma del proiettile

    obj.shapesize(0.3, 0.3, 0.3)            # Dimensioni del proiettile

    obj.showturtle()
    obj.pendown()
        
def take_input():
    gui = turtle.Screen()
    
    # Inizializzazione degli input

    v = gui.numinput("Velocità iniziale", "Inserire la velocità con cui il proiettile viene sparato: ", 50, 1, 100)
    # h = gui.numinput("Altezza iniziale", "Inserire l'altezza da cui proiettile viene sparato: ", 10, 1, 100)
    teta = gui.numinput("Angolo di lancio", "Inserire l'angolo in gradi con cui il proiettile viene sparato: ", 45, 0, 90)
    
    return v, teta

def set_outputs():
    text_velocity.speed(11)
    text_distance.speed(11)
    text_time.speed(11)

    text_velocity.hideturtle()
    text_velocity.penup()
    text_velocity.goto(-700, 300)  

    text_distance.hideturtle()
    text_distance.penup()
    text_distance.goto(-700, 275)

    text_time.hideturtle()
    text_time.penup()
    text_time.goto(-700, 250)

    set_proiettile()

def aggiorna_xyv(vx, vy, delta_t):

    # Calcolo le nuove coordinate in base alle equazioni del moto parabolico

    x = round(obj.xcor() + vx*delta_t, 5)   

    y = round((-1/2) * g * (delta_t ** 2) + vy*delta_t + obj.ycor(), 5)

    vy = round(vy - g * delta_t, 5)

    return x, y, vy

def move_proiettile(v0, teta):
    set_outputs()

    vx = v0*cos(teta)                       # Velocità orizzontale 
    vy = v0*sin(teta)                       # Velocità verticale

    tempo_totale = 0
    distanza = 0

    text_time.clear()
    text_distance.clear()

    while obj.ycor() > -200:
        tempo_totale += 0.05

        x, y, vy = aggiorna_xyv(vx, vy, 0.05)
        distanza = abs(-500 - x)
        
        # Aggiorno la velocità ogni 0.05 secondi percorsi (nella simulazione)
        
        text_velocity.clear()
        text_velocity.write(f"Velocità: {round(sqrt(vx ** 2 + vy ** 2)*3.6, 2)} km/h", align="left", font=("Arial", 10, "normal"))

        obj.goto(x, y)


    text_distance.write(f"Distanza percorsa: {round(distanza, 2)} metri", align="left", font=("Arial", 10, "normal"))

    text_time.write(f"Tempo in volo: {round(tempo_totale, 2)} secondi", align="left", font=("Arial", 10, "normal"))
            
if __name__ == "__main__":
    set_env()

    velocita, angolo = take_input()

    move_proiettile(velocita, radians(angolo))
    gui.mainloop()