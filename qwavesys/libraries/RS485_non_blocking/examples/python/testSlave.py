# Add parent directory to path so the example can run without the library being installed
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import serial
import rs485

# Open non-blocking port
port = serial.Serial("COM11", baudrate=9600, timeout=0, rtscts=False)
rs485 = rs485.SerialWrapper(port)

while True:
    if rs485.update():
        packet = rs485.getPacket()
        print(len(packet), " bytes received\n".encode())
        print(packet)
