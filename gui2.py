"""
The GUI
"""
from guizero import App, Text, TextBox, PushButton, Picture
import matplotlib.pyplot as plt
from dynamometer import dynamometer
from tacho_reader import HallEffectReader, calculate_speed
from dynograph import LineGraph

import sys
sys.path.insert(0,'test')
from controller_gui import MotorControllerPi, ControllerGUI

class dynoGUI:
    def __init__(self, dyno):
        self.mydyno = dyno
        self.mycontroller = None
        self.xspeed = [] #speed of x for graph
        
        self.app = App(title="Dyno Testing", width=610, height=500,
            layout="grid", bg="#fdbbff")
        
        welcome_msg = Text(self.app, text="Welcome to the Dyno GUI",
           size=30, color="blue", grid=[1,0], width="fill")

        dinopicture = Picture(self.app, image="dinosaur1.gif", grid=[0,0])
        dinopicture = Picture(self.app, image="dinosaur1.gif", grid=[2,0])
        
        
    # This function updates the diameter
    def updateD(self, input_diameter):
        dynodiameter = input_diameter.value
        mydyno.updateWheel(dynodiameter)
        
    # This function updates the horsepower
    def updateH(self, input_horsepower):
        dynohorsepower = input_horsepower.value
        mydyno.updateHorse(dynohorsepower)
        
    def updateR(self, input_reading):
        mydyno.updateReading(input_reading.value)

    def update_speed(self, display_speed):
        display_speed.value = self.mydyno.speed
        
        #self.xspeed.append(display_speed.value)
        display_speed.after(1000, self.update_speed, args=[display_speed]);

    # This function displays the values of known variables    
    def displayValues(self):
        one = Text(self.app, text="diammeter: " + str(mydyno.wheelDiameter),
            grid=[1,7], align="left")
            
        two = Text(self.app, text="horsepower: " + str(mydyno.horsepower),
            grid=[1,8], align="left")
            
        three = Text(self.app, text="rpm: " + str(mydyno.rpm), grid=[1,9],
            align="left")
            
        four = Text(self.app, text="speed: " + str(mydyno.speed), grid=[1,10],
            align="left")
        
        # calculates the twerk
        # mydyno.calculate()
        # five = Text(self.app, text="torque: " + str(mydyno.torque), grid=[1,11],
        #    align="left")

    def display_controller(self):
        c = MotorControllerPi()
        self.mycontroller = ControllerGUI(c, self.app)
        self.mycontroller.display()
        
    def updateE(self, input_diameter, input_horsepower, input_reading):
        dynodiameter = input_diameter.value
        mydyno.updateWheel(dynodiameter)
        
        dynohorsepower = input_horsepower.value
        mydyno.updateHorse(dynohorsepower)
        
        mydyno.updateReading(input_reading.value)


    def setup_gui(self):
        """
        Diameter
        """
        d_description = Text(self.app, text="Diameter (mm): ", grid=[0,1],
            align="left")
        input_diameter = TextBox(self.app, grid=[1,1], width=10)
        
        """
        Horsepower
        """
        
        h_description = Text(self.app, text="Horsepower (hp): ", grid=[0,2],
            align="left")
        input_horsepower = TextBox(self.app, grid=[1,2], width=10)
        
        
        """
        Tachometer
        """
        r_description = Text(self.app, text="Reading Amounts: ", grid=[0,3],
            align="left")
        input_readings = TextBox(self.app, grid=[1,3], width=10)
        
        update_everything = PushButton(self.app, command=self.updateE ,
            text="Update Values", grid=[0,4])
        
        update_everything.update_command(command=self.updateE, args =[input_diameter,input_horsepower,input_readings])
        


        show_info = PushButton(self.app,command=self.displayValues,
            text= "Calculate Results", grid=[1,6])

                ### starts and stops tacho
        start_tacho = PushButton(self.app, command=self.mydyno.run_tacho,
            text ="Start Readings", grid=[1,10])
        
        """
        grapphing stuff
        """
        show_graph = PushButton(self.app, command=self.mydyno.graphSpeed,
            text = "Display Graph", grid= [1,11])
        
        #display_speed = Text(self.app, grid=[1,15], text=self.mydyno.speed)
        #display_speed.after(100, self.update_speed, [display_speed])
        
        
        """
        Controller GUI
        """
        show_controllergui = PushButton(self.app, command=self.display_controller,
            text = "Display Motor Controller", grid= [2,3])
        
        
        self.app.display()

if __name__ == "__main__":
    """
    Initiates the dyno
    """
    mydyno = dynamometer(0, 0)
    guiInstance = dynoGUI(mydyno)
    theapp = guiInstance.setup_gui()

