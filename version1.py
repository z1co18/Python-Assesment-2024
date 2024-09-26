from gpiozero import DigitalInputDevice

d0_input = DigitalInputDevice(21)

while True:
    print(d0_input.value)
    if (not d0_input.value):
        print('moisture threshold reached!!! \n')
    else:
        print('You need to water your plant \n')
        
              