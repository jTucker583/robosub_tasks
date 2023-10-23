import sys
import serial
import os

def main(args):
    # ensure three total args python GPSdatatester.py [PORT] [BAUDRATE]
    if len(args) != 3:
        print("Usage: python GPSdatatester.py [PORT] [BAUDRATE]")
        quit()

    # check if the port is open and connected
    if os.path.exists(argv[1]):
        print("Port " + argv[1] + " is connected.")
    else:
        print("Port " + argv[1] + " does not exist or is not connected to the system!")
        quit()
    
    gps = ser.Serial(argv[1],argv[2],timeout=1)
    gps.flushInput() # clears the serial port so there is no data overlaping
    gps_bytes = gps.readline()
    while gps_bytes:
        line = gps_bytes.readline()
        if line.find('GPGGA'):
            print(line)

main(sys.argv)