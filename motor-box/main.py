from machine import PWM, Pin
from mcp3008 import MCP3008
from utime import sleep

FQ = 333
PW = 1500000
mcp = MCP3008(1, 14, 15, 16, 17)
convertedRangeChanelZero = mcp.rangeConvert(mcp.read_adc(0))
convertedRangeChanelOne = mcp.rangeConvert(mcp.read_adc(1))
convertedRangeChanelTwo = mcp.rangeConvert(mcp.read_adc(2))
convertedRangeChanelThree = mcp.rangeConvert(mcp.read_adc(3))
# self, bus: int, clock_pin: int, mosi_pin: int, miso_pin: int, chip_select_pin: int
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
#adc Pins?

# pwm5 = PWM(pOut0, freq=333)
# as
pOut2.duty_ns(2000000) # 1 ms
print(pOut2.freq())
print("LED starts flashing...")
while True:
    pOut2.duty_ns(convertedRangeChanelZero)
    pOut3.duty_ns(convertedRangeChanelZero)

    pOut4.duty_ns(convertedRangeChanelOne)
    pOut5.duty_ns(convertedRangeChanelOne)

    pOut6.duty_ns(convertedRangeChanelTwo)
    pOut7.duty_ns(convertedRangeChanelTwo)

    pOut8.duty_ns(convertedRangeChanelThree)
    pOut9.duty_ns(convertedRangeChanelThree)

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
