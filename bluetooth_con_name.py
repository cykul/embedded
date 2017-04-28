import time 
import bluetooth 
import os 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

target_name="Redmi"
target_address=None
nearby_devices=bluetooth.discover_devices()
print nearby_devices
for bdaddr in nearby_devices:
	
	if target_name == bluetooth.lookup_name(bdaddr):


			target_address= bdaddr
			GPIO.output(11, 1)
	                print "on"
                        time.sleep(2)
                        GPIO.output(11, 0)
                        print "off"			
			break



if target_address is not None:
	print 'found target bluetooth device with address  ',target_address

else:
	print 'could not find target bluetooth device nearby '





'''os.system('hciconfig hci0 up')
#os.system('exechciconfig hci0 sspmode 0')
os.system('hciconfig hci0 piscan')'''
#sudo bluetooth-agent 1234

'''output = shell_exec('gpio mode '.$_GET['pin'].' out');
time.sleep(20)
hciconfig hci0 up
exechciconfig hci0 sspmode 1
hciconfig hci0 piscan
sudo bluetooth-agent 1234'''

#output = shell_exec('gpio write '.$_GET['pin'].' '.$_GET['status']);

'''import serial
from protocol import *
from MotorControllerP import *

def startBluetoothServer():
        bluetoothSerial = serial.Serial("/dev/rfcomm1",baudrate=9600)
        print("Bluetooth connected")
        try:
                while 1:
                        data = bluetoothSerial.readLine()
                        if not data: break
                        data = data.decode()
                        print("Data received: "+data)
                        if data[:3] == Client.INIT_HEY:
                                print("Initiallizing connection")
                                bluetoothSerial.write((Server.INIT_OK+"\n").enc$
                                print("Connection initiallized")
                        elif data[:3] == Client.KTHXBYE:
                               bluetoothSerial.write(Server.CLOSE.encode())
                                exitAndClean()
                        elif data[:3] == Client.CUSTOM_MOVE:
                                data = str(data)
                                formattedData = data.split(",")
                                direction = formattedData[1]
                                left = formattedData[2]
                                right = formattedData[3]
                                response = customSpeed(direction,left,right)
                                print(direction+","+left+","+right)
                                bluetoothSerial.write((str(response)+"\n").enco$
                        else:
                                print("Command not understood: "+data)
                bluetoothSerial.write(Server.CLOSE.encode())
        except KeyboardInterrupt:
                print("Rage Quit")
        except:
                print("Error happened:",sys.exc_info())
        finally:'''
