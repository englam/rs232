from datetime import datetime
import serial, sys
import io


serial_rs232 = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate= '115200',
)




while serial_rs232.isOpen():
    try:
        data_string = serial_rs232.read(size=50)
        data_string = serial_rs232.readline().decode()
        print (data_string, end='\n')
    except KeyboardInterrupt:
        print ("You press ctrl+c")
        serial_rs232.close()
        sys.exit()

