#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/


#hola, es un cuadro para ver la velocidad el internet

#primero isntalar pip install pyspeedtest
from tkinter import *
from tkinter import messagebox
import pyspeedtest

def one():
    speed=pyspeedtest.SpeedTest("www.google.com")#paguina para conectar
    a1=(str(speed.download())+"[bps]")#variable de la velocidad
    a2=(str(speed.download()/10000)+"[Mbps]")#variable de la velocidad
    messagebox.showinfo("Tu velocidad de descarga es ",a1)#nombre de la ventana

root=Tk()
root.title("check de velocidad de internet")#nombre de la ventana
root.config(bg="pink")#color de fondo
root.geometry("520x200")#tamaño del cuadro

label1=Label(root,text="Check Velocidad Internet",font=("Arial",30,"bold"),bg="lightblue").pack()
button1=Button(root,text="START",font=("Arial",20,"bold"),bg="yellow",height=1,width=10,command=one).pack()
root.mainloop()