#brightness change
from machine import Pin, PWM
import time

pwm_led = PWM(Pin(16))
pwm_led.freq(1000)

while True:
    for duty in range(0, 65535, 5000):  # Increase brightness
        pwm_led.duty_u16(duty)
        time.sleep(0.05)

    for duty in range(65535, 0, -5000):  # Decrease brightness
        pwm_led.duty_u16(duty)
        time.sleep(0.05)
