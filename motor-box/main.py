from machine import Pin
from utime import sleep
from machine import Pin, PWM

FQ = 333
PW = 1500000
#Input Pins/PWM
pIn10 = (Pin(10, Pin.IN, Pin.PULL_DOWN))
pIn11 = (Pin(11, Pin.IN, Pin.PULL_DOWN))
pIn12 = (Pin(12, Pin.IN, Pin.PULL_DOWN))
pIn13 = (Pin(13, Pin.IN, Pin.PULL_DOWN))
#Output Pins/PWM
pOut2 = PWM(Pin(2, Pin.OUT), FQ, duty_ns = PW)
pOut3 = PWM(Pin(3, Pin.OUT), FQ, duty_ns = PW)
pOut4 = PWM(Pin(4, Pin.OUT), FQ, duty_ns = PW)
pOut5 = PWM(Pin(5, Pin.OUT), FQ, duty_ns = PW)
pOut6 = PWM(Pin(6, Pin.OUT), FQ, duty_ns = PW)
pOut7 = PWM(Pin(7, Pin.OUT), FQ, duty_ns = PW)
pOut8 = PWM(Pin(8, Pin.OUT), FQ, duty_ns = PW)
pOut9 = PWM(Pin(9, Pin.OUT), FQ, duty_ns = PW)
# pwm5 = PWM(pOut0, freq=333)

pOut2.duty_ns(2000000) # 1 ms
print(pOut2.freq())
print("LED starts flashing...")
while True:
    pOut2.duty_ns(PW)
    pOut3.duty_ns(PW)
    pOut4.duty_ns(PW)
    pOut5.duty_ns(PW)
    pOut6.duty_ns(PW)
    pOut7.duty_ns(PW)
    pOut8.duty_ns(PW)
    pOut9.duty_ns(PW)
    if pIn10.value():
        pOut2.duty_ns(PW)
        pOut3.duty_ns(PW)
    if pIn11.value():
        pOut4.duty_ns(PW)
        pOut5.duty_ns(PW)
    if pIn12.value():
        pOut6.duty_ns(PW)
        pOut7.duty_ns(PW)
    if pIn13.value():
        pOut8.duty_ns(PW)
        pOut9.duty_ns(PW)