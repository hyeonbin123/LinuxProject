import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
bp,lp,ledOn1,ledOn2,lbtn1,lbtn2=[16,18],[20,21,23,24],0,0,0,0
for i in bp: GPIO.setup(i,GPIO.IN)
for i in lp: GPIO.setup(i,GPIO.OUT)
bI=[0,0]
try:
    while True:
        bI=[GPIO.input(i) for i in bp]
        if bI[0] :
            while GPIO.input(bp[0]): pass
            ledOn1 = not ledOn1
            for i in range(2):GPIO.output(lp[i],ledOn1)
        if bI[1] :
            while GPIO.input(bp[1]): pass
            ledOn2 = not ledOn2 
            for i in range(2):GPIO.output(lp[i+2],ledOn2)
except KeyboardInterrupt :
    pass
GPIO.cleanup()


