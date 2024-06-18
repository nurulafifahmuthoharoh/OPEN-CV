import RPi.GPIO as GPIO

import time



GPIO.setwarnings(False)

TRIG = int(4)

ECHO = int(17)



servoPIN = int(12)



GPIO.setmode(GPIO.BCM)



GPIO.setup(servoPIN, GPIO.OUT)





servo = GPIO.PWM(servoPIN, 50)

servo.start(7.5)



GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)

GPIO.setup(ECHO, GPIO.IN)





while True:

   GPIO.output(TRIG, False)

   time.sleep(0.000002)

   GPIO.output(TRIG, True)

   time.sleep(0.000010)

   GPIO.output(TRIG, False)



   StartTime = time.time()

   StopTime = time.time()



   while GPIO.input(ECHO) == 0:

      StartTime = time.time()

   while GPIO.input(ECHO) == 1:

      StopTime = time.time()



   TimeElapsed = StopTime - StartTime

   distance = (TimeElapsed * 34300) / 2

   distance= int (distance)

   print("jarak =", distance)



   if(distance >=2 and distance <=20):

      servo.ChangeDutyCycle(2.5)            # 0 Degrees

   elif (distance >=21 and distance <=30):

      servo.ChangeDutyCycle(5)              # 45 Degrees

   elif (distance >=31 and distance <=40):

      servo.ChangeDutyCycle(7.5)            # 90 Degrees

   else:

      servo.ChangeDutyCycle(12.5)            # 180 Degrees



   time.sleep(0.1)
