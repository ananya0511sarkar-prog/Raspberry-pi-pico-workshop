from machine import Pin
import time

fan = Pin(0, Pin.OUT, value=0)

ON_TIME_S = 5
OFF_TIME_S = 5

while True:
    fan.value(1)   # Fan ON
    time.sleep(ON_TIME_S)
    fan.value(0)   # Fan OFF
    time.sleep(OFF_TIME_S)