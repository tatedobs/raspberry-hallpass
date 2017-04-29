import RPi.GPIO as GPIO
import time

GPIO_green = 6
GPIO_red = 5

def green_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_green, GPIO.OUT)
    GPIO.setup(GPIO_red, GPIO.OUT)
    GPIO.output(GPIO_green,GPIO.HIGH)
    print "green LED on"
    GPIO.output(GPIO_red, GPIO.LOW)
    print "red LED off"

def red_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_green, GPIO.OUT)
    GPIO.setup(GPIO_red, GPIO.OUT)
    GPIO.output(GPIO_red,GPIO.HIGH)
    print "red LED on"
    GPIO.output(GPIO_green, GPIO.LOW)
    print "green LED off"

def flashy_flash():
    for x in range(5):
        green_on()
        time.sleep(0.05)
        red_on()
        time.sleep(0.05)
