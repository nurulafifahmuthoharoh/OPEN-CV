import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

TRIG1 = int(4)
ECHO1 = int(17)

TRIG2 = int(27)
ECHO2 = int(22)

TRIG3 = int(24)
ECHO3 = int(25) 

ina1 = 26
ina2 = 19
ena =  13
inb1 = 21
inb2 = 20
enb =  16
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(ina1,GPIO.OUT)
GPIO.setup(ina2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(ina1,GPIO.LOW)
GPIO.output(ina2,GPIO.LOW)
p=GPIO.PWM(ena,1000)
p.start(100)

GPIO.setmode(GPIO.BCM)
GPIO.setup(inb1,GPIO.OUT)
GPIO.setup(inb2,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(inb1,GPIO.LOW)
GPIO.output(inb2,GPIO.LOW)
p=GPIO.PWM(enb,1000)
p.start(100)


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(TRIG3, GPIO.OUT)
GPIO.setup(ECHO3, GPIO.IN)



while True:
   GPIO.output(TRIG1, False)
   time.sleep(0.000002)
   GPIO.output(TRIG1, True)
   time.sleep(0.000010)
   GPIO.output(TRIG1, False)

   StartTime = time.time()
   StopTime = time.time()

   while GPIO.input(ECHO1) == 0:
      StartTime = time.time()
   while GPIO.input(ECHO1) == 1:
      StopTime = time.time()

   TimeElapsed = StopTime - StartTime
   distance1 = (TimeElapsed * 34300) / 2
   distance1 = int (distance1)
   print("jarak1 =", distance1)

   GPIO.output(TRIG2, False)
   time.sleep(0.000002)
   GPIO.output(TRIG2, True)
   time.sleep(0.000010)
   GPIO.output(TRIG2, False)

   StartTime = time.time()
   StopTime = time.time()

   while GPIO.input(ECHO2) == 0:
      StartTime = time.time()
   while GPIO.input(ECHO2) == 1:
      StopTime = time.time()

   TimeElapsed = StopTime - StartTime
   distance2 = (TimeElapsed * 34300) / 2
   distance2= int (distance2)
   print("jarak2 =", distance2)

   GPIO.output(TRIG3, False)
   time.sleep(0.000002)
   GPIO.output(TRIG3, True)
   time.sleep(0.000010)
   GPIO.output(TRIG3, False)

   StartTime = time.time()
   StopTime = time.time()

   while GPIO.input(ECHO3) == 0:
      StartTime = time.time()
   while GPIO.input(ECHO3) == 1:
      StopTime = time.time()

   TimeElapsed = StopTime - StartTime
   distance3 = (TimeElapsed * 34300) / 2
   distance3= int (distance3)
   print("jarak3 =", distance3)


   if(distance1 >=2 and distance1 <=20 or distance2 <= 20 or distance3 <= 20):
      GPIO.output(ina1,GPIO.LOW)
      GPIO.output(ina2,GPIO.LOW)
      GPIO.output(inb1,GPIO.LOW)
      GPIO.output(inb2,GPIO.LOW)
   else:

      GPIO.output(ina1,GPIO.HIGH)
      GPIO.output(ina2,GPIO.LOW)
      GPIO.output(inb1,GPIO.LOW)
      GPIO.output(inb2,GPIO.HIGH)

   time.sleep(0.1)

