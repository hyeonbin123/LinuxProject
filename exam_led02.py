import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led1 = 23
led2 = 24
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.output(led1,False)
GPIO.output(led2,False)
try:
    while True:
        GPIO.output(led1,True)
        GPIO.output(led2,True)
        time.sleep(0.001)
        GPIO.output(led1,False)
        GPIO.output(led2,False)
        time.sleep(0.009)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
