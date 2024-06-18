import RPi.GPIO as GPIO #in order to use the RPI GPIO pins
import pigpio
import time
GPIO.setmode(GPIO.BCM) #in order to use the GPIO pins as GPIO18 according to the raspberry pinout
trig=4
echo=17
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.output(trig,True)
time.sleep(0.0001) #given time is in seconds GPIO.output(trig, False)
while
   GPIO.input(echo)==False
   start= time.time()
while
   GPIO.input(echo)==True
   end= time.time()
   sig_time=end-start distance=sig_time/0.000058
   print('Distance: {} centimeters'.format(distance)) #display distance in cm if needed in inches divide sig_time by 0.000148
   GPIO.cleanup() #clean all GPIO pins
