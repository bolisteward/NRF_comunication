import RPi.GPIO as GPIO
import time
import spidev
from lib_nrf24 import NRF24

#Begin the radio using GPIO08 as CE and GPIO25 as CSN pins.
GPIO.setmode(GPIO.BCM)

pipes = [[0xFF, 0xFF, 0xF1, 0xF1, 0xF2],[0xFF, 0xFF, 0xF2, 0xF2, 0xF3]]

"""Set payload size as 32 bit, channel address as 76, data rate of 1 mbps and power levels as minimum."""
radio.begin(0,25)
radio.setPayloadSize(32)  
radio.setChannel(0x76) 
radio.setDataRate(NRF24.BR_1MBPS)    
radio.setPALevel(NRF24.PA_MIN)

radio.openWritingPipe(pipes[0])     
radio.printDetails()

sendMessage = list("Hi..Arduino UNO")  
while len(sendMessage) < 32:    
    sendMessage.append(0)

while True:
    start = time.time()      
    radio.write(sendMessage)   
    print("Sent the message: {}".format(sendMessage))  
    radio.startListening() 

while not radio.available(0):
    time.sleep(1/100)
    if time.time() - start > 2:
        print("time out") # print error message if radio disconnected or not functioning anymore
        break

radio.stopListening()     # close radio
time.sleep(3)  # give delay of 3 seconds
