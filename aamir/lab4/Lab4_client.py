#!/usr/bin/env python

import socket
import time
import datetime
#from random import randint
import asyncore
import struct 
import random

DST_IP = '127.0.0.1'
DST_PORT = 2605
BUFFER_SIZE = 0x0090
#SRC_IP = socket.gethostbyname(socket.gethostname()) 
SRC_IP = '192.168.50.128'
SRC_PORT = random.randint(2000,5000)

## Network Set-Up ##
class Client(asyncore.dispatcher):

    def __init__(self, host,port,SRC_IP,SRC_PORT):
        asyncore.dispatcher.__init__(self)
        self.socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((SRC_IP,SRC_PORT))
        self.connect( (host, port) )
        self.buffer= '      '

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        return self.recv(0x0090)

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self,packet):
        #self.send(packet)
        sent = self.send(packet)
        print sent
        self.buffer = self.buffer[sent:]

    def genREQ(self,reqid,responsDelay):
        MessageType = "REQ"
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
        print "sent data:", MESSAGE
        return MESSAGE

    
    def trailerRecord():
        Mydate = time.strftime("%m%d%y")
        MyTime = time.strftime("%H%M%S")
    #RcvShutdownStatus = 


    def GenShutDown():
        MessageType = "FIN" 
        MESSAGE = MessageType 
        TCPHeader =  struct.pack ('>H',(len(MESSAGE))) # compute length of message (first byte will always be 00
        MESSAGE = TCPHeader + MESSAGE
        print "sent data:", MESSAGE
        return MESSAGE
    


'''
DST_IP = '192.168.101.222'
DST_PORT = 2605
BUFFER_SIZE = 0x0090
#SRC_IP = socket.gethostbyname(socket.gethostname()) 
SRC_IP = '10.1.20.16'
SRC_PORT = random.randint(2000,5000)

## Print Request Packet ## '''

     

def main():

    client = Client(DST_IP,DST_PORT,SRC_IP,SRC_PORT)
    f = open('Lab4.Scenario1.KhanA.client.-txt', 'w')
     
    packet = client.genREQ(1,0)
    client.handle_write(packet)
    data = client.handle_read()
    ResponseType = ''
    if('Good Req' in data.decode('ascii')):
        ResponseType = '1'
    elif ('Bad Req' in data.decode('ascii')):
        ResponseType = '4'
    elif ('OIT-Delay' in data.decode('ascii')):  
        ResponseType = '2'  


   
    data = data+ ResponseType +'|'

    print data 
           

    asyncore.loop()


    '''Packet = GenShutDown()
    s.send(Packet)
    data = s.recv(BUFFER_SIZE)'''

    for i in range (0,100):
         packet = client.genREQ(i,0)
         client.handle_write(packet)
         #time.sleep(3)
         data = client.handle_read()
         if('Good Req' in data.decode('ascii')):
            ResponseType = '1'
         elif ('Bad Req' in data.decode('ascii')):
            ResponseType = '4'
         elif ('OIT-Delay' in data.decode('ascii')):  
            ResponseType = '2'    
         data = data+ ResponseType +'|'
         print "received data:" , data.decode('ascii')
         f.write(packet + '\n')
         f.write(data + '\n')
         asyncore.loop()
         

    client.handle_close()
    #s.shutdown(socket.SHUT_WR)

    f.close()




if __name__ == "__main__":
    main()
