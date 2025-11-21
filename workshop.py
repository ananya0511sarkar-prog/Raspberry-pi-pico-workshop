#print("Hello world")
#SCode Example:
#out put code or blink codeS
from machine import Pin
import time

led = Pin(16 , Pin.OUT)

while True:
    led.value(1)  # Turn the LED ON
    time.sleep(2) 
    led.value(0)  # Turn the LED OFF
    time.sleep(2)
