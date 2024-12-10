from classes import Motor, Potentiometer

talon = None

try:

    pin = 0
    freq = 100 
    talon = Motor(pin, freq)
    # speed = 0.55
    # talon.setSpeed(speed)
    potPowerPin = 27
    potInputPin = 26
    pot = Potentiometer(potPowerPin, potInputPin)
    while True:
        speed = pot.getVal()
        talon.setSpeed(speed)
        
except KeyboardInterrupt:
    if talon is not None: 
        talon.stop()
