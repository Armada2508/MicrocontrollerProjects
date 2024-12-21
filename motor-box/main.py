from machine import PWM, Pin

from mcp3008 import MCP3008

FREQUENCY = 333
NEUTRAL_PW = 1500000  # PWM Pulse Width for neutral output in nano seconds
mcp = MCP3008(1, 10, 11, 12, 13)
# Input Pins/PWM
pIn14 = Pin(14, Pin.IN, Pin.PULL_DOWN)
pIn15 = Pin(15, Pin.IN, Pin.PULL_DOWN)
pIn16 = Pin(16, Pin.IN, Pin.PULL_DOWN)
pIn17 = Pin(17, Pin.IN, Pin.PULL_DOWN)
# Output Pins/PWM
pOut2 = PWM(Pin(2, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut3 = PWM(Pin(3, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut4 = PWM(Pin(4, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut5 = PWM(Pin(5, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut6 = PWM(Pin(6, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut7 = PWM(Pin(7, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut8 = PWM(Pin(8, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
pOut9 = PWM(Pin(9, Pin.OUT), freq=FREQUENCY, duty_ns=NEUTRAL_PW)
adcPower = Pin(18, Pin.OUT, value=1)

while True:
    convertedRangeChannelZero = mcp.rangeConvert(mcp.read_adc(0))
    convertedRangeChannelOne = mcp.rangeConvert(mcp.read_adc(1))
    convertedRangeChannelTwo = mcp.rangeConvert(mcp.read_adc(2))
    convertedRangeChannelThree = mcp.rangeConvert(mcp.read_adc(3))

    pOut2.duty_ns(convertedRangeChannelZero)
    pOut3.duty_ns(convertedRangeChannelZero)

    pOut4.duty_ns(convertedRangeChannelOne)
    pOut5.duty_ns(convertedRangeChannelOne)

    pOut6.duty_ns(convertedRangeChannelTwo)
    pOut7.duty_ns(convertedRangeChannelTwo)

    pOut8.duty_ns(convertedRangeChannelThree)
    pOut9.duty_ns(convertedRangeChannelThree)

    if pIn14.value():
        pOut2.duty_ns(NEUTRAL_PW)
        pOut3.duty_ns(NEUTRAL_PW)
    if pIn15.value():
        pOut4.duty_ns(NEUTRAL_PW)
        pOut5.duty_ns(NEUTRAL_PW)
    if pIn16.value():
        pOut6.duty_ns(NEUTRAL_PW)
        pOut7.duty_ns(NEUTRAL_PW)
    if pIn17.value():
        pOut8.duty_ns(NEUTRAL_PW)
        pOut9.duty_ns(NEUTRAL_PW)
