from gpiozero import DigitalInputDevice
import time
import smtplib

d0_input = DigitalInputDevice(21)

while True:
    print(d0_input.value)
    if not d0_input.value:
        print('Moisture threshold reached!!! \n')
    else:
        print('You need to water your plant \n')
    time.sleep(3)