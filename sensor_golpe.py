import RPi.GPIO as GPIO			#importamos las funciones de la led
import time 					#importamos la funcion time
  
GPIO.setmode(GPIO.BCM)

sensor = 17
led = 27
GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
  
  
#Function executed on signal detection
def golpe_red(null):				#esta funcion sera la que detecte el golpe en la red (2da manera de discriminacion de gol), null porque no le pasamos ningun parametro
        GPIO.output(led,1)		#enciende el led
        print ("Paso por aqui")	#texto de comprobacion
        time.sleep(1)			#se queda encendido 1 segundo 
        GPIO.output(led,0)		#se vuelve a apagar

#Cuando se detecte el cambio de vibracion (falling), se activa la funcion.
GPIO.add_event_detect(sensor, GPIO.FALLING, callback=golpe_red, bouncetime=100) #sensor activa el mismo, falling detecta el cambio en la frecuencia, callback es el llamado a la funcion, bouncetime es la "sensibilidad"
  
# ciclo del programa (lo mantriene siempre leyendo)
try:				
	while True:
		time.sleep(1)	#le da una pausa cada vez que llama a la funcion golpe_red

  
# Detiene el programa a traves de la consola
except KeyboardInterrupt:
        GPIO.cleanup()
