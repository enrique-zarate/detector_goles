import RPi.GPIO as gpio
from time import sleep

foto1 = 4
foto2 = #falta definir
foto3 = #falta definir
foto4 = #falta definir

gpio.setmode(gpio.BCM)
gpio.setup(foto,gpio.IN)

while True:
    if gpio.input(foto1) == False or gpio.input(foto2) == False or
    gpio.input(foto3) == False or gpio.input(foto4) == False:
        print("Gol")
        contador_goles = contador_goles + 1 #este el contador
        sleep(2)


        
'''


    gpio.output(led3,True)
    sleep(1)
    gpio.output(led1,False)
    sleep(1)
    gpio.output(led2,False)
    sleep(1)
    gpio.output(led3,False)
    sleep(1)

gpio.setmode(gpio.BCM)

sensor = 17
led = 27
gpio.setup(sensor, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(led, gpio.OUT)

def active(null):
        GPIO.output(led, True)
        print("Funciona")
    
gpio.add_event_detect(sensor, gpio.FALLING, callback=active, bouncetime=50) 

while True:
    
    

#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
###
### KY-053 Analog Digital Converter - Raspberry Pi Python Code Example
###
#############################################################################################################
 
 
# This code is using the ADS1115 and the I2C Python Library for Raspberry Pi
# This was published on the following link under the BSD license
# [https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code]
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
 
# import needed modules
import math, signal, sys, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
print("prueba") 
# initialise variables
delayTime = 0.5 # in Sekunden
 
# assigning the ADS1x15 ADC
 
ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit
 
# choosing the amplifing gain
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V
 
# choosing the sampling rate
# sps = 8    # 8 Samples per second
# sps = 16   # 16 Samples per second
# sps = 32   # 32 Samples per second
sps = 64   # 64 Samples per second
# sps = 128  # 128 Samples per second
# sps = 250  # 250 Samples per second
# sps = 475  # 475 Samples per second
# sps = 860  # 860 Samples per second
 
# assigning the ADC-Channel (1-4)
adc_channel_0 = 0    # Channel 0
adc_channel_1 = 1    # Channel 1
adc_channel_2 = 2    # Channel 2
adc_channel_3 = 3    # Channel 3
 
# initialise ADC (ADS1115)
adc = ADS1x15(ic=ADS1115)
 
# Input pin for the digital signal will be picked here
Digital_PIN = 24
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
  
#############################################################################################################
  
# ########
# main program loop
# ########
# The program reads the current value of the input pin
# and shows it at the terminal
  
try:
        while True:
            print "reading..."
            #Current values will be recorded
            analog = adc.readADCSingleEnded(adc_channel_0, gain, sps)
  
            # Output at the terminal
            if GPIO.input(Digital_PIN) == False:
                print "Analog voltage value:", analog,"mV, ","extreme value: not reached"
            else:
                print "Analog voltage value:", analog, "mV, ", "extreme value: reached"
            print "---------------------------------------"
  
            sleep(delayTime)
except Exception,e: print(str(e)) 
  
  
except KeyboardInterrupt:
        GPIO.cleanup()
