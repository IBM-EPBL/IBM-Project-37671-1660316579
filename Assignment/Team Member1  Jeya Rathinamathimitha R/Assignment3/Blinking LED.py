import RPI.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, ini

while True:
    GPIO.output(7, GPIO.HIG
    print("LED on")
    sleep(1)
    GPIO.output(7, GPIO.LOW
    print("LED off")
    sleep(1)
                
