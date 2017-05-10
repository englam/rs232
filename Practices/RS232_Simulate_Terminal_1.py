from threading import Thread
import serial, sys, time

serial_rs232 = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate= '115200',
)


boot_complete=""

class CountdownTask:
    def __init__(self):
        self._running = True
        self.startup =""


    def terminate(self):
        self._running = False

    def readline(self,n):
        while serial_rs232.isOpen():
            data_string = serial_rs232.readline().decode()
            print(data_string)
            global boot_complete

            if "Powered down" in data_string:
                self.startup = "startup"
                boot_complete = "startup"


    def writeline(self, n):
        #initial_write = self.readline
        while serial_rs232.isOpen():
            #msg = ('help \n\r')
            msg = input()
            msg = msg + '\r'
            serial_rs232.write(msg.encode())

    def close_terminal(self):
        serial_rs232.close()


try:
    c1 = CountdownTask()
    rs232_read = Thread(target=c1.readline, args=(3,))
    rs232_write = Thread(target=c1.writeline, args=(3,))
    rs232_read.start()
    rs232_write.start()


except:
    c1.terminate()
    serial_rs232.close()
    #c1.join()
    sys.exit()