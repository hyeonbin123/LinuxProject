import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
bp=18
lp1=23
lp2=24
GPIO.setup(bp,GPIO.IN)
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)
try:
    while True:
        btnInput = GPIO.input(bp)
        GPIO.output(lp1,btnInput)
        GPIO.output(lp2,btnInput)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
