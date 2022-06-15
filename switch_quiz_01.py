import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
bp,lp1,lp2,ledOn,lbtn=18,23,24,0,0
GPIO.setup(bp,GPIO.IN)
GPIO.setup(lp1,GPIO.OUT)
GPIO.setup(lp2,GPIO.OUT)
try:
    while True:
        btnInput=GPIO.input(bp)
        if btnInput and not lbtn:
            print("rising")
            ledOn=1 if not ledOn else 0
            GPIO.output(lp1,ledOn)
            GPIO.output(lp2,ledOn)
        elif not btnInput and lbtn:
            print("falling")
        else:
            pass
        lbtn=btnInput
except KeyboardInterrupt :
    pass
GPIO.cleanup()


