#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

#instalar por comandos pip install python_barcode
#clic derecho sobre text correr bar code maker
import barcode
from barcode.writer import ImageWriter
text="Python programing code"
text1=str(text)
code=barcode.get_barcode_class("code128")
image=code(text,writer=ImageWriter())
save_img=image.save('my final barcode')