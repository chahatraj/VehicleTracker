import serial 
import time 
def gsm(msg):
port= serial.Serial("/dev/ttyAMA0",9600,timeout=3.0) 
print "Sending message ..."   
number=raw_input("Enter mobile number: ")  
port.write('AT+CMGS=”'+number+'”\r\n')  
time.sleep(2)  
port.flushInput()  
port.flushOutput()  
port.write(msg)  
time.sleep(2)  
port.write('\x1A\r\n')  
print port.read(50)  
port.flushInput()  
port.flushOutput() 
port.close()
print ‘done’
