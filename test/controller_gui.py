from guizero import App, Slider, Text, PushButton, Window

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    import GPIO_fake as GPIO
except ModuleNotFoundError:
    import GPIO_fake as GPIO

class ControllerGUI:
    def __init__(self, controller, main_window=None):
        self.controller = controller
        
        self.max_rpm = 3500
        self.rpm = 0
        self.direction = 1
        if not main_window:
            self.setup_gui()
        else:
            self.setup_sub_window(main_window)
    
    
    def setup_gui(self):
        self.app = App(title='Motor Velocity Control')
        self.rpm_text = Text(self.app, text=str(self.rpm))
        self.dir_text = Text(self.app,
            text='Clockwise' if self.direction == 1 else 'Counter Clockwise')
            
        self.slider = Slider(self.app, start=0, end=self.max_rpm, width=200,
            command=self.update_rpm)
        
        self.forward_button = PushButton(self.app, command=self.set_direction,
            args=[1], text='Forward', width=50)
            
        self.backward_button = PushButton(self.app, command=self.set_direction,
            args=[-1], text='Backward', width=50)
    
    def setup_sub_window(self, main_window):
        self.app = Window(main_window, title='Motor Velocity Control')
        self.rpm_text = Text(self.app, text=str(self.rpm))
        self.dir_text = Text(self.app,
            text='Clockwise' if self.direction == 1 else 'Counter Clockwise')
            
        self.slider = Slider(self.app, start=0, end=self.max_rpm, width=200,
            command=self.update_rpm)
        
        self.forward_button = PushButton(self.app, command=self.set_direction,
            args=[1], text='Forward', width=50)
            
        self.backward_button = PushButton(self.app, command=self.set_direction,
            args=[-1], text='Backward', width=50)       
        
    
    
    def set_direction(self, direction):
        """Set the direction where +1 = clockwise and -1 = counter-clockwise.
        
        Args:
            direction: the
            
        Returns:
            True if successful, false otherwise
        """
        if direction not in [-1, 1]:
            return False
        
        else:
            self.direction = direction
            
            if direction == 1:
                self.dir_text.value = 'Clockwise'
            else:
                self.dir_text.value = 'Counter Clockwise'
            
            return True


    def update_rpm(self, value):
        """Update the rpm.
        
        Args:
            text: the Text object to update
            value: the str value to update to
            
        Returns:
            None
        """
        self.rpm_text.value = value
        self.rpm = self.direction * int(value)
        self.controller.set_duty_cycle(self.rpm, self.max_rpm)   
    
    def display(self):
        self.app.display()


class MotorControllerPi:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # output on pin GPIO19
        GPIO.setup(19, GPIO.OUT)
        
        # GPIO19 as PWM with 30 kilohertz frequency
        self.pwm = GPIO.PWM(19, 2500)
        
        # 50% duty cycle is 0 rpm
        self.pwm.start(50)


    def set_duty_cycle(self, velocity, max_speed):
        ratio = (velocity / max_speed) * 50 + 50
        print("ratio: {:f}".format(ratio))
        self.pwm.ChangeDutyCycle(ratio)
    
    
    def cleanup(self):
        GPIO.cleanup()
    
if __name__ == '__main__':
    c = MotorControllerPi()
    gui = ControllerGUI(c)
    gui.display()
    c.cleanup()



