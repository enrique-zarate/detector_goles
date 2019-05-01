from flask import Flask,render_template
import RPi.GPIO as gpio
from time import sleep
import time
tiempo_anterior = 0

foto1 = 27
foto2 = 17
foto3 = 6
foto4 = 7

gpio.setmode(gpio.BCM)
gpio.setup(foto1,gpio.IN)
gpio.setup(foto2,gpio.IN)
gpio.setup(foto3,gpio.IN)
gpio.setup(foto4,gpio.IN)
contador_goles = 0


def sensor(llamada):
	global tiempo_anterior
	tiempo_ahora = time.time()
	diferencia_tiempos = tiempo_ahora - tiempo_anterior
	if(diferencia_tiempos>3):
		global contador_goles
		contador_goles = contador_goles + 1 #este el contador
		tiempo_anterior = tiempo_ahora
		print("GOOOOOOL ",contador_goles)
	else:
		print("Debes esperar: ", 3-diferencia_tiempos)
	

# Si alguno de los sensores es FALSE, contar. Obviar el resto
	#gpio.add_event_detect(foto1,gpio.RISING, callback=sensor, bouncetime=100)


gpio.add_event_detect(foto1,gpio.FALLING, callback=sensor, bouncetime=100)
#if foto1 == False
gpio.add_event_detect(foto2,gpio.FALLING, callback=sensor, bouncetime=100)
gpio.add_event_detect(foto3,gpio.FALLING, callback=sensor, bouncetime=100)
gpio.add_event_detect(foto4,gpio.FALLING, callback=sensor, bouncetime=100)
			
			
			

			

app=Flask(__name__)




@app.route('/')
def index():
	
	return render_template('index.html',dat = contador_goles)




if __name__=='__main__':
	"""
	while True:
		if gpio.input(foto1) == True or gpio.input(foto2) == False or gpio.input(foto3) == False or gpio.input(foto4) == False:
		#if foto1 == True or foto2 == False or foto3 == False or foto4 == False:
			print("Gol")
			sensor()
			sleep(2)
	"""

	
		
	app.run()
		
