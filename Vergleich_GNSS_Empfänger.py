import pynmea2
import serial
import io
import time

ser = serial.Serial(port='COM4', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


while 1:
    try:
        line = sio.readline()
        if line[3:6] == "VTG":
            msg = pynmea2.parse(line)
            print (msg)
        if line[3:6] == "GGA":
            msg = pynmea2.parse(line)
            print (msg)
        if line[3:6] == "GSA":
            msg = pynmea2.parse(line)
            print (msg)
        if line[3:6] == "GSV":
            msg = pynmea2.parse(line)
            print (msg)
    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue
