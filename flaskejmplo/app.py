from flask import Flask,render_template
import RPi.GPIO as gpio
from time import sleep

foto1 = 4
foto2 = 3
foto3 = 6
foto4 = 7

gpio.setmode(gpio.BCM)
gpio.setup(foto1,gpio.IN)
gpio.setup(foto2,gpio.IN)
gpio.setup(foto3,gpio.IN)
gpio.setup(foto4,gpio.IN)
contador_goles = 0

def sensor(llamada):
	global contador_goles
	contador_goles = contador_goles + 1 #este el contador
	print(contador_goles)
	
if foto1 == True:
	gpio.add_event_detect(foto1,gpio.RISING, callback=sensor, bouncetime=100)
if foto2 == True:
	gpio.add_event_detect(foto2,gpio.RISING, callback=sensor, bouncetime=100)


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
		
