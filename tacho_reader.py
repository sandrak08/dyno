import RPi.GPIO as GPIO
import time
import math

class HallEffectReader:
    def __init__(self, channel):
    """Initialize hall effect sensor's general purpose input pin and
    edge detection interrupt on the raspberry pi.
    
    Args:
        channel (int): the bcm pin number the hall effect sensor is
            connected to on the pi.
    """
        # specify broadcom chip-specific pin numbering system
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # initialize general purpose input pin
        GPIO.setup(hall_pin, GPIO.IN, GPIO.PUD_UP)
        
        # initialize interrupt for hall effect sensor's edge detection 
        GPIO.add_event_detect(
            channel, 
            GPIO.FALLING,
            callback = self.elapsed_callback,
            bouncetime = 10) # minimum time between callbacks (msecs) 
        
        self.current = 0 # current time
        self.elapse = 0  # time for one complete revolution of the magnet (sec)
        self.pulse = 0   # total number of complete revolution by the magnet 
        
    def elapsed_callback(self):
        """The callback function that will count the pulses of the
            tachometer.
        """
        self.pulse += 1
        self.elapse = time.time() - self.current
        self.current = time.time()
    
    def clean_up(self):
        GPIO.cleanup()

    def get_elapse(self):
        return self.elapse
    
    def get_pulse(self):
        return self.pulse
    
    
def calculate_speed(radius, elapse_time):
    """ Determine how fast the magnet is rotating in miles per hour.
    
    Args:
        radius (float): the distance from the center of the circular
            object to the perimeter of that object where the magnet
            is located in millimeter (mm)
            
    Returns:
        The speed in miles per hour (float)
    """
    # to avoid error in frequency calculation
    if elapse_time == 0:
        return;
    
    # calculate frequency (rps) and scale (rph)
    frequency = 1 / elapse_time
    frequency = frequency * 3600 
    
    # calculate circumference (mm) and scale (mile)
    circumference = 2 * math.pi * radius
    circumference = circumference * 6.2137e-7
    
    # speed calculation (mph)
    return circumference * frequency
    

if __name__ == "__main__":                
    # initialize hall effect sensor reader
    reader = HallEffectReader(12)
    
    try:
        while True:
            # calculate speed
            elaspe = reader.get_elapse()
            speed = calculate_speed(15, elapse)
            
            # display content every second
            print("Speed (mph): {:.3f}".format(speed))
            time.sleep(1)
            
    # loop until keyboard interrupt (CTRL+C)      
    except KeyboardInterrupt:
        reader.clean_up()
        
