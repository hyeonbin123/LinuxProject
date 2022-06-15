import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
lp1=23
lp2=24
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)
try:
    while True:
        for i in range(11):
            for j in range(11):
                GPIO.output(lp1,True)
                GPIO.output(lp2,True)
                time.sleep(i*0.001)
                GPIO.output(lp1,False)
                GPIO.output(lp2,False)
                time.sleep((10-i)*0.001)
        for z in range(10,-1,-1):
            for j in range(11):
                GPIO.output(lp1,True)
                GPIO.output(lp2,True)
                time.sleep(z*0.001)
                GPIO.output(lp1,False)
                GPIO.output(lp2,False)
                time.sleep((10-z)*0.001)
except KeyboardInterrupt :
    pass
GPIO.cleanup()
