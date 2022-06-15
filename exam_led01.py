import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led1 = 23
led2 = 24
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.output(led1,True)
GPIO.output(led2,True)
time.sleep(5.0)
GPIO.output(led1,False)
GPIO.output(led2,False)
GPIO.cleanup()
