import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
lp1=23
lp2=24
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)
p1=GPIO.PWM(lp1,1.0)
p1.start(50.0)
p2=GPIO.PWM(lp2,1.0)
p2.start(50.0)
try:
    while True:
        pass
except KeyboardInterrupt:
    pass
p1.stop()
p2.stop()
GPIO.cleanup()
