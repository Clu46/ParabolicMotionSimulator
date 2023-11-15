import turtle
from math import sin, cos, radians, sqrt

gui = turtle.Screen()
gui.screensize(2000, 2000)
gui.setup(width=1.0, height=1.0)            
gui.title("Parabolic Motion Simulator")     

obj = turtle.Turtle()                       
obj.speed(11)                               

text_velocity = turtle.Turtle()             
text_distance = turtle.Turtle()             
text_time = turtle.Turtle()                 

g = 9.81                                    

def set_env():
    ground = turtle.Turtle()                
    ground.clear()
    ground.speed(11)
    ground.hideturtle()
    ground.penup()
    
    ground.goto(-500, -200)                 
    ground.color('green')
    ground.pendown()
    ground.goto(1000, -200)                 

def set_missile(altezza):
    obj.clear()
    obj.hideturtle()
    obj.penup()

    obj.goto(-500, altezza)                  
    
    obj.color("black")
    obj.shape("circle")                     

    obj.shapesize(0.3, 0.3, 0.3)            

    obj.showturtle()
    obj.pendown()
        
def take_input():
    gui = turtle.Screen()
    
    v = gui.numinput("Initial speed", "Enter the speed at which the missile is fired (in km/h): ", 100, 10, 400)
    h = gui.numinput("Initial altitude", "Enter the altitude from which the missile is fired (in meters): ", 200, 50, 500)
    teta = gui.numinput("Launch Angle", "Enter the angle at which the missile is fired (in degrees): ", 45, 0, 90)
    
    return round((v / 3.6), 5), teta, (h-200)

def set_outputs(altezza):
    text_velocity.clear()
    text_distance.clear()
    text_time.clear()

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

    set_missile(altezza)

def aggiorna_xyv(vx, vy, delta_t):

    x = round(obj.xcor() + vx*delta_t, 5)   

    y = round((-1/2) * g * (delta_t ** 2) + vy*delta_t + obj.ycor(), 5)

    vy = round(vy - g * delta_t, 5)

    return x, y, vy

def move_missile(v0, teta, h):
    set_outputs(h)

    vx = v0*cos(teta)                        
    vy = v0*sin(teta)                       

    tempo_totale = 0
    distanza = 0

    text_time.clear()
    text_distance.clear()

    while obj.ycor() > -200:
        tempo_totale += 0.05

        x, y, vy = aggiorna_xyv(vx, vy, 0.05)
        distanza = abs(-500 - x)
        
        text_velocity.clear()
        text_velocity.write(f"Velocity: {round(sqrt(vx ** 2 + vy ** 2)*3.6, 2)} km/h", align="left", font=("Arial", 10, "normal"))

        obj.goto(x, y)


    text_distance.write(f"Travelled Distance: {round(distanza, 2)} meters", align="left", font=("Arial", 10, "normal"))

    text_time.write(f"Time in Flight: {round(tempo_totale, 2)} seconds", align="left", font=("Arial", 10, "normal"))


    gui.onclick(main())

def main():
    set_env()

    velocita, angolo, altezza = take_input()

    move_missile(velocita, radians(angolo), altezza)

if __name__ == "__main__":
    main()