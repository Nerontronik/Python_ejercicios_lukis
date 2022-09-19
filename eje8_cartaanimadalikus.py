#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

import turtle
from pygame import mixer

t=turtle.Turtle()

mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()

t.pensize(5)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Ashok chakra
t.color('#050F88')
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0,-80)
t.circle(80,360)

#verde
t.begin_fill()
t.color("red")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()
#amarillo
t.color("yellow")
move(-350,80)
t.begin_fill()
t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()