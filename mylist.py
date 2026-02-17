from machine import Pin
import time

led1 = Pin(15, Pin.OUT )
led2 = Pin(18, Pin.OUT )
led3 = Pin(21,Pin.OUT )
led4 = Pin(26, Pin.OUT )

Arshialist = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

for j in Arshialist:
        led1.value(j[0])
        led2.value(j[1])
        led3.value(j[2])
        led4.value(j[3])
        time.sleep(1)#Create any list
