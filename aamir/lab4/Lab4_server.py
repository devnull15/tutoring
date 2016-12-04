#!/usr/bin/env python

import socket
import time
import datetime
import random
from thread import start_new_thread

## Network Parameters ## 
TCP_IP = '127.0.0.1'
TCP_PORT = 2605
BUFFER_SIZE = 0x0090
##

def genRES(parsedREQ):
    ## TO DO
    '''MessageType = "REQ"
    msTimeStamp =  str(int(round(time.time() * 1000))) # milisecond time stamp value from timer running on client; max length 10
    msTimeStamp = msTimeStamp[:-3]
    print msTimeStamp;
    RequestID = str(reqid)
    StudentName = "KhanA"
    StudentID = "91-81551"
    ResponseDelay = str(responsDelay)
    ClientIPAddress = SRC_IP
    ClientServicePort = str(SRC_PORT)
    ClientSocketNumber = "1" # ???
    ForeignHostIPAddress = DST_IP
    ForeignHostServicePort = str(DST_PORT)
    StudentData = "Hello dear I am Aami"
    
    ScenarioNo = "2"
    MESSAGE = MessageType + "|" + msTimeStamp + "|" + RequestID + "|" + StudentName + "|" + StudentID + "|" + ResponseDelay + "|" + ClientIPAddress + "|" + ClientServicePort + "|" + ClientSocketNumber + "|" + ForeignHostIPAddress + "|" + ForeignHostServicePort + "|" + StudentData + "|" + ScenarioNo + "|"
    TCPHeader =  struct.pack ('>H',(len(MESSAGE))) # compute length of message (first byte will always be 00
    MESSAGE = TCPHeader + MESSAGE
    print "sent data:", MESSAGE '''
    MESSAGE = ''
    return MESSAGE

def parseREQ(REQ):
    ## TO DO
    parsed = []
    return parsed
    
def trailerRecord():
    Mydate = time.strftime("%m%d%y")
    MyTime = time.strftime("%H%M%S")
    ## TO DO


def GenShutDown():
    MessageType = "FIN" 
    MESSAGE = MessageType 
    TCPHeader =  struct.pack ('>H',(len(MESSAGE))) # compute length of message (first byte will always be 00
    MESSAGE = TCPHeader + MESSAGE
    print "sent data:", MESSAGE
    return MESSAGE

## thread for each individual client that connects to the server
def client_thread(conn, addr):
    fn = 'Lab4.Scenario1.KhanA.server.'
    fn += addr
    fn += '.txt'
    f = open(fn, 'w') # log file per client
    while 1:
        REQ = conn.recv(BUFFER_SIZE) # get REQ
        if not REQ: break
        print "received:", REQ
        f.write(REQ + '\n')
        #parsedREQ = parseREQ(REQ) # parse request for things the server needs for response
        #RES = genRES(parsedREQ) # generate a response for the client using the parsed request
        RES = REQ
        f.write(RES + '\n')
        print "sent:", RES
        conn.send(RES)  # echo
    #f.write(trailerRecord()) # TODO: append trailer info to log file
    f.close()
    conn.close()

    
def main():

    ## Set up Server ##
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    ##
    
    ## Listener loop to establish connection with a client  ##
    while True:
        conn, addr = s.accept()
        print("Client connected: " + addr[0] + ":" + str(addr[1]))

        start_new_thread(client_thread, (conn,addr[0])) # starts new thread when client arrives
    ##

    s.close()
    f.close()




if __name__ == "__main__":
    main()
