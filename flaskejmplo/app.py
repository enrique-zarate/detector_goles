from flask import Flask,render_template
import RPi.GPIO as gpio
from time import sleep

app=Flask(__name__)


foto1 = True
foto2 = False
foto3 = True
foto4 = True

'''
gpio.setmode(gpio.BCM)
gpio.setup(foto1,gpio.IN)
gpio.setup(foto2,gpio.IN)
gpio.setup(foto3,gpio.IN)
gpio.setup(foto4,gpio.IN)'''
contador_goles = 0

def sensor ():
	contador_goles = contador_goles + 1 #este el contador
	index()
	
	
@app.route('/')
def index():
	
	return render_template('index.html',dat = contador_goles)
	


if __name__=='__main__':
	app.run()
	while True:
		#if gpio.input(foto1) == False or gpio.input(foto2) == False or gpio.input(foto3) == False or gpio.input(foto4) == False:
		if foto1 == False or foto2 == False or foto3 == False or foto4 == False:
			print("Gol")
			sensor()
			sleep(2)
