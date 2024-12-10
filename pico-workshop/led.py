from machine import Pin

pin = Pin("LED", Pin.OUT)

pin.toggle()