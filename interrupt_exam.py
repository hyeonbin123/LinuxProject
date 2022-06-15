import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

ls=0
lsc=0
def buttonPressed(channel):
    global ls, lsc
    ls=not ls
    lsc=1
bp=18
lp1=23
lp2=24

GPIO.setup(bp,GPIO.IN)
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)

GPIO.add_event_detect(bp,GPIO.RISING)
GPIO.add_event_callback(bp,buttonPressed)

try:
    while True:
        if lsc == 1:
            lsc=0
            GPIO.output(lp1,ls)
            GPIO.output(lp2,ls)
except KeyboardInterrupt: pass
GPIO.cleanup()
