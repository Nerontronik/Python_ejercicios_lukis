#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

#instalar primero pip instal plyer

import time
from plyer import notification
if __name__== '__main__':
    while True:
        notification.notify(
            title="toma una clase",
            message="yo he tomado un workshop python",
            timeout=10
        )
        time.sleep(15)