#!/usr/bin/python
import serial,time,struct
import codecs

SERIAL_PORT = '/dev/buspirate'
TIMEOUT = 1

ser = serial.Serial()

NULL = 0x00 # Null Byte
SOH = 0x01 #  Start of Header
UTC = 0x5A # Unit Type Code
ADDR = 0x00 #  Address of the Device
STX = 0x02 # Start of Text
CMD = 0x00 # Command Code
COT = 0x04 # End of Transmission

def serial_init():
    ser.port = SERIAL_PORT #serial port
    ser.baudrate = 9600 #baudrate
    ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    ser.parity = serial.PARITY_NONE #set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    ser.timeout = None #non-block read
    ser.xonxoff = False     #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

def setup_frame(data):
    DATA = bytearray(data,'utf-8')
    DATA_LEN = len([NULL,SOH,UTC,ADDR,*DATA,COT])
    tx_buffer = struct.pack(DATA_LEN*'h',NULL,SOH,UTC,ADDR,*DATA,COT)
    return(tx_buffer)

def main():
    serial_init()
    print(setup_frame("DEADBEEF"))
    return

if __name__ == '__main__':
    main()
