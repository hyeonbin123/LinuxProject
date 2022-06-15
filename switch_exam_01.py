import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
bp=18
GPIO.setup(bp,GPIO.IN)
try:
    while True:
        btnInput = GPIO.input(bp)
        print(btnInput)
except KeyboardInterrupt :
    pass
GPIO.cleanup()
