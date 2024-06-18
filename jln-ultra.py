import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

TRIG = int(4)
ECHO = int(17)
in1 = 26
in2 = 19
en =  13
temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(100)

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
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
   else:

      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)


   time.sleep(0.1)
