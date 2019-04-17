try:
    import RPi.GPIO as GPIO

except RuntimeError:
    import GPIO_fake as GPIO

except ModuleNotFoundError:
    import GPIO_fake as GPIO

import time

class PWMReader:
    def __init__(self, channel_rising, channel_falling, frequency):
        """Initialize PWM general purpose input pin via edge detection
        interrupt on the raspberry pi.
        
        Args:
            channel_rising (int): the bcm pin number the pwm rising edge
                reading is onnected to on the pi.

            channel_falling (int): the bcm pin number the pwm rising edge
                reading is onnected to on the pi.

            frequency (float): the frequency of the pulses in hertz.
        """

        # specify broadcom chip-specific pin numbering system
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # initialize general purpose input pin
        GPIO.setup(channel_rising, GPIO.IN)
        GPIO.setup(channel_falling, GPIO.IN)

        #intialize interrupt for pwm edge detection
        GPIO.add_event_detect(
            channel_rising,
            GPIO.RISING,
            callback = self.rising
        )

        GPIO.add_event_detect(
            channel_falling,
            GPIO.FALLING,
            callback = self.falling
        )

        self.PERIOD = 1 / frequency
        
        # the value of the pulse width
        self.pwm_value = 0
        
        # current time
        self.current = 0
        
        # channel (pin) that this reader is grabbing data from
        self.channel_rising = channel_rising
        self.channel_falling = channel_falling


    def rising(self, channel):
        if channel == self.channel_rising:
            self.current = time.time()

    def falling(self, channel):
        if channel == self.channel_falling:
            self.pwm_value = time.time() - self.current

    def clean_up(self):
        GPIO.cleanup()

    def get_duty_cycle(self):
        #print("period: {:.8f}".format(self.PERIOD))
        return self.pwm_value / self.PERIOD

if __name__ == "__main__":
    reader = PWMReader(23, 24, 1000)
    
    try:
        while True:
            duty_cycle = reader.get_duty_cycle()
            print("duty cycle: {:.3f}".format(duty_cycle))
            
    
    # loop until keyboard interrupt (CRTL+C)
    except KeyboardInterrupt:
        reader.clean_up()
