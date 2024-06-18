import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

TRIG = int(4)
ECHO = int(17)

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
   distance = int (distance)
   print("jarak =", distance)

   if(distance >=2 and distance <=20):
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
