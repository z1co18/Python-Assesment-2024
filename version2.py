import RPI.GPIO as GPIO
import time

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPI.IN)

def callback(channel):
        if GPIO.input(channel):
            print("no water detected")
        else:
            print("water detected")
            
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=30) # let us know when pin is high or low
GPIO.add_event_callback(channel, callback) # assigns fucntions to GPIO PIN, Run fucntions change....?

#infinte loop
while true:
        time.sleep(1)