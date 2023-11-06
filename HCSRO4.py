#sudo chown root:$USER /dev/gpiomem
#sudo chmod g+rw /dev/gpiomem

#tests sensors without moving pi 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
TRIG = 23 #pin 16 
ECHO = 24 #pin 18 
print ("Distance Measurement in Progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN) 
GPIO.output(TRIG, False) 
print ("Waiting for Sensors to Settle")
time.sleep(2) 
GPIO.output(TRIG, True) 
time.sleep(0.00001)
GPIO.output(TRIG, False) 
while GPIO.input(ECHO) == 0: 
	pulse_start = time.time()
while GPIO.input (ECHO) == 1: 
	pulse_end = time.time() 
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2) 
print ("Distance for sensor 1:", distance, "cm")

#second sensor 
TRIG = 25 #pin 22 
ECHO = 12 #pin 32 
#print ("Distance Measurement in Progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN) 
GPIO.output(TRIG, False) 
#print ("Waiting for Sensors to Settle") 
time.sleep(2) 
GPIO.output(TRIG, True) 
time.sleep(0.00001)
GPIO.output(TRIG, False) 
while GPIO.input(ECHO) == 0: 
	pulse_start = time.time()
while GPIO.input (ECHO) == 1: 
	pulse_end = time.time() 
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2) 
print ("Distance for sensor 2:", distance, "cm")





