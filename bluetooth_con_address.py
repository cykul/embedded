import bluetooth
import time
import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


os.system('hciconfig hci0 up')
os.system('hciconfig hci0 piscan')
check=0
target_name = "Redmi"
target_address =  'C4:0B:CB:D6:A2:70'


nearby_devices = bluetooth.discover_devices()
print nearby_devices
if any(target_address in string for string in nearby_devices):
			print 'address found'
                   	GPIO.output(11, 1)
                        print "on"
                        time.sleep(2)
                        GPIO.output(11, 0)
                        print "off"

			check=1


if (check==1) :
        print "found target bluetooth device with address ", target_address
        
else:
        print "could not find target bluetooth device nearby"
        

time.sleep(1)


