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
ETX = 0x03 # End of Text
COT = 0x04 # End of Transmission

CMD = {
"write_TEXT":"A",
"read_TEXT":"B",
"write_SPECIAL":"C",
"read_SPECIAL":"D",
"write_STRING":"E",
"read_STRING":"F",
"write_DOTS":"G",
"read_DOTS":"H"
}


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

def setup_frame(data,cmd):
    DATA_b = bytearray(data,'ascii')
    CMD_b = bytearray(CMD[cmd],'ascii')

    DATA_LEN = len([NULL,SOH,*CMD_b,UTC,ADDR,*DATA_b,ETX,COT])
    tx_buffer = struct.pack(DATA_LEN*'b',NULL,SOH,*CMD_b,UTC,ADDR,*DATA_b,ETX,COT)
    import ipdb; ipdb.set_trace()

    return(tx_buffer)

def main():
    serial_init()
    print("\n\n\n\n\n\n\n")
    data_s = "DEADBEEF"
    cmd_s = "write_STRING"
    print("NULL,SOH,   "+cmd_s+",   UTC, ADDR,   "+data_s+",   ETX,COT")
    print(setup_frame(data_s,cmd_s))
    return

if __name__ == '__main__':
    main()
