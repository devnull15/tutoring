#!/usr/bin/env python

import socket
from random import randint


## Network Set-Up ##
DST_IP = '192.168.101.222'
DST_PORT = 2605
BUFFER_SIZE = 0x0090
SRC_IP = "192.168.98.128"
SRC_PORT = 31337

## Print Request Packet ##
def genREQ():
    MessageType = "REQ"
    msTimeStamp = "" # milisecond time stamp value from timer running on client; max length 10
    RequestID = str(randint(0,99999999999999999999))
    StudentName = "BudzitowskiD"
    StudentID = "99-9999"
    ResponseDelay = "10"
    ClientIPAddress = SRC_IP
    ClientServicePort = str(SRC_PORT)
    ClientSocketNumber = "00000" # ???
    ForeignHostIPAddress = DST_IP
    ForeignHostServicePort = str(DST_PORT)
    StudentData = "                    " # Currently all spaces; max length = 20
    ScenarioNo = "1"
    MESSAGE = MessageType + "|" + msTimeStamp + "|" + RequestID + "|" + StudentName + "|" + StudentID + "|" + ResponseDelay + "|" + ClientIPAddress + "|" + ClientServicePort + "|" + ClientSocketNumber + "|" + ForeignHostIPAddress + "|" + ForeignHostServicePort + "|" + StudentData + "|" + ScenarioNo + "|"
    TCPHeader = '\x00' + chr(len(MESSAGE)) # compute length of message (first byte will always be 00
    MESSAGE = TCPHeader + MESSAGE
    return MESSAGE

def main():
    packet = genREQ()
    s = socket.create_connection((DST_IP, DST_PORT), 1, (SRC_IP, SRC_PORT))
    s.send(packet)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "received data:", data

if __name__ == "__main__":
    main()
