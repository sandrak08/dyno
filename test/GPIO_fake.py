"""
Fake functions to allow programming that is not directly on the Raspberry Pi
"""
BCM = 1

IN = 0
OUT = 1

def setwarning(flag):
    pass

def setmode(mode):
    pass

def setup(channel, mode):
    pass

def add_event_detect(channel, edge_mode, callback, bouncetime):
    pass

def cleanup():
    pass

class Pwm:
    def start(self, ratio):
        pass
    def ChangeDutyCycle(self, ratio):
        pass

def PWM(channel, freq):
    return Pwm()
    
