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
        serial_rs232.write(help_command.encode())
        break

    except KeyboardInterrupt:
        print ("You press ctrl+c")
        serial_rs232.close()
        sys.exit()


print ("done")
serial_rs232.close()
sys.exit()
