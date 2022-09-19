#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

#instalar primero pip install wikipedia

import tkinter
from tkinter import *
import wikipedia as wk

window=Tk()
window.title("mi miniwiky")
window.config(bg="black")
f1_heading=Frame(window)
f2_frame=Frame(window)
f3_result=Frame(window)

Label(f1_heading,text="MINIKIKI",font=("Time",30,"bold"),bg="lightgreen").pack(side=TOP)
Label(f2_frame,text="busce aqui ",font=("Arial",20,"bold"),bg="yellow").pack(side=LEFT)
Label(f3_result,text="Lo que encontramos",font=("Arial",25,"bold"),bg="lightpink").pack(side=LEFT)

entry_box=Entry(f2_frame,width=40,font=("Arial",20,"bold"))
entry_box.pack(side=LEFT, fill=BOTH, expand=5)
entry_box.focus_set()

query=''
text=Text(window,font=("Arial",27,"bold"),bg="lightgreen",pady=100, padx=55)

def text_Search():
    global query
    query=entry_box.get()
    try:
        txt_summary=wk.summary(query)
        text.insert('1.0',txt_summary)
    except:
        text.insert('1.0','nada de nada')
    

button1=Button(f2_frame,text="buscando",command=text_Search,font=("Arial",15,"bold"),bg="red",fg="white")
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP, pady=20, padx=50)
text.pack()

window.mainloop()