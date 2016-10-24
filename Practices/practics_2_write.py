import serial, sys, time
import io

username = 'cisco'
password = 'cisco'
help_command = 'help'
exit_command = 'exit'

serial_rs232 = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate= '115200',
)




while serial_rs232.isOpen():
    try:
        print(1)
        serial_rs232.write(exit_command.encode())
        break

    except KeyboardInterrupt:
        print ("You press ctrl+c")
        serial_rs232.close()
        sys.exit()


print ("done")
serial_rs232.close()
sys.exit()
