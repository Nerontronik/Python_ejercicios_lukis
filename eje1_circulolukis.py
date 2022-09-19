#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

import turtle
turtle.bgcolor("lightpink")
turtle.pensize(1.5)
turtle.speed(0.5)
color=["red","blue","green","orange"]
for a in range (99):
    for i in color :
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()
