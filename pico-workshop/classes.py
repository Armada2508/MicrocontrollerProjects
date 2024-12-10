from machine import ADC, PWM, Pin


class Potentiometer:
    
    def __init__(self, powerPin, inputPin) -> None:
        potPower = Pin(powerPin, mode = Pin.OUT)
        self.potInput = ADC(Pin(inputPin, mode = Pin.IN))
        potPower.high()

    def getVal(self):
        return self.potInput.read_u16() / 65535
        

class Motor:
    
    def __init__(self, pin, freq):
        self.pwm = PWM(Pin(pin, mode = Pin.OUT))
        self.pwm.freq(freq) # Hz
        
    def setSpeed(self, speed):
        self.pwm.duty_ns(int((speed+1) * 1e6))
    
    def stop(self):
        self.pwm.deinit()