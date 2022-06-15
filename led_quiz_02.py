import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
lp1=23 # led_pin1  BCM_GPIO 23
lp2=24
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)
p1=GPIO.PWM(lp1,1000.0)
p1.start(0.0)
p2=GPIO.PWM(lp2,1000.0)
p2.start(0.0)
try:
    while True:
        for i in range(101):
            p1.ChangeDutyCycle(i)
            p2.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(100,-1,-1):
            p1.ChangeDutyCycle(i)
            p2.ChangeDutyCycle(i)
            time.sleep(0.01)
except KeyboardInterrupt :
    pass
p1.stop()
p2.stop()
GPIO.cleanup()
