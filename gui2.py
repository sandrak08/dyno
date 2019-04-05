"""
The GUI
"""

from guizero import App, Text, TextBox, PushButton, Picture
from dynamometer import dynamometer
from tacho_reader import HallEffectReader, calculate_speed


class dynoGUI:
    def __init__(self, dyno):
        self.mydyno = dyno
        
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
        
    def update_speed(self, display_speed):
        print("djlsf")
        display_speed.value = self.mydyno.speed
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



    def setup_gui(self):
        """
        Diameter
        """
        d_description = Text(self.app, text="Diameter (mm): ", grid=[1,1],
            align="left")
            
        input_diameter = TextBox(self.app, grid=[1,1], width=10)
        update_diameter = PushButton(self.app, command=self.updateD ,
            text="Update Diameter", grid=[1,2])
            
        update_diameter.update_command(command=self.updateD,
            args=[input_diameter])
        
        """
        Horsepower
        """
        h_description = Text(self.app, text="Horsepower (hp): ", grid=[1,4],
            align="left")
            
        input_horsepower = TextBox(self.app, grid=[1,4], width=10)
        
        update_horsepower = PushButton(self.app, command=self.updateH,
            text="Update Horsepower", grid=[1,5],align="top" )
        update_horsepower.update_command(command=self.updateH,
            args=[input_horsepower])
        
        show_info = PushButton(self.app,command=self.displayValues,
            text= "Calculate Results", grid=[1,6])


        """
        Tachometer
        """
        get_tacho = PushButton(self.app, command=self.mydyno.enable_tacho,
            text="Enable Tachometer", grid=[1,7])

        start_tacho = PushButton(self.app, command=self.mydyno.run_tacho,
            text ="Start Readings", grid=[1,8])
        
        display_speed = Text(self.app, grid=[1,15], text=self.mydyno.speed)
        display_speed.after(100, self.update_speed, [display_speed])

        self.app.display()

if __name__ == "__main__":
    """
    Initiates the dyno
    """
    mydyno = dynamometer(0, 0)
    #show_info = PushButton(app,command=displayValues, text= "Calculate Results", grid=[1,6])
    guiInstance = dynoGUI(mydyno)
    theapp = guiInstance.setup_gui()



