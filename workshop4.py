from machine import Pin, PWM

pwm_pin = PWM(Pin(16))
pwm_pin.freq(1000)

while True:
    PWM_value = int(0.2 * 65535) #0.2 /0.5 dibo 
    pwm_pin.duty_u16(PWM_value)
