import bluetooth,subprocess
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
passkey="1111"
port=24
nearby_devices = bluetooth.discover_devices()

print nearby_devices

subprocess.call("kill -9 pidof bluetooth-agent",shell=True)

status=subprocess.call("bluetooth agent"+passkey+"&",shell=True)
       

#time.sleep(1)


try:
	s=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	s.connect((target_address,port))
except bluetooth.btcommon.BluetoothError as err:
	pass
