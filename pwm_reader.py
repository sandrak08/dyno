try:
    import RPi.GPIO as GPIO

except RuntimeError:
    import GPIO_fake as GPIO

except ModuleNotFoundError:
    import GPIO_fake as GPIO

import time

class PWMReader:
    def __init__(self, channel, frequency):
        """Initialize PWM general purpose input pin via edge detection
        interrupt on the raspberry pi.
        
        Args:
            channel (int): the bcm pin number the pwm reading is connected to
                on the pi.
            
            frequency (float): the frequency of the pulses in hertz.
        """

        # specify broadcom chip-specific pin numbering system
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # initialize general purpose input pin
        GPIO.setup(channel, GPIO.IN)

        #intialize interrupt for pwm edge detection
        GPIO.add_event_detect(
            channel,
            GPIO.RISING,
            callback = self.rising,
        )

        GPIO.add_event_detect(
            channel,
            GPIO.FALLING,
            callback = self.falling,
        )
        
        self.PERIOD = 1 / frequency
        
        # the value of the pulse width
        self.pwm_value = 0
        
        # current time
        self.current = 0

    def rising(self):
        """The callback function that will clock the rising edge.
        """
        self.current = time.time()

    def falling(self):
        """The callback function that will clock the falling edge and calculate
        the value of the pulse width.
        """
        self.pwm_value = time.time() - self.current

    def clean_up(self):
        GPIO.cleanup()

    def get_duty_cycle(self):
        return self.pwm_value / self.PERIOD

if __name__ == "__main__":
    reader = PWMReader(24, 30000)
    
    try:
        while True:
            duty_cycle = reader.get_pwm()
            print("duty cycle: {:.3f}".format(duty_cycle))
    
    # loop until keyboard interrupt (CRTL+C)
    except KeyboardInterrupt:
        reader.clean_up()
