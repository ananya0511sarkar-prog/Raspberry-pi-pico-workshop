import time
from servo import Servo
my_servo = Servo(pin_id=0)#pin id 0
while True:
    my_servo.write(30)#angle
    time.sleep(0.2)
    my_servo.write(60)
    time.sleep(0.2)
    my_servo.write(90)
