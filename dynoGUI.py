# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:48:21 2019

@author: Sandra
"""

from guizero import App, Text, TextBox, PushButton, Picture
from dynamometer import dynamometer


def updateD():
    dynodiameter = input_diameter.value
    mydyno.updateWheel(dynodiameter)
    
def updateH():
    dynohorsepower = input_horsepower.value
    mydyno.updateHorse(dynohorsepower)
    
def displayValues():
    one = Text(app, text="diammeter: " + str(mydyno.wheelDiameter), grid=[1,7], align="left")
    two = Text(app, text="horsepower: " + str(mydyno.horsepower), grid=[1,8], align="left")
    three = Text(app, text="rpm: " + str(mydyno.rpm), grid=[1,9], align="left")
    four = Text(app, text="speed: " + str(mydyno.speed), grid=[1,10], align="left")
    
    #calculates the twerk
    mydyno.calculate()    
    five = Text(app, text="torque: " + str(mydyno.torque), grid=[1,11], align="left")

app = App(title="Dyno Testing", width=500,height=500,layout="grid")

dinopicture = Picture(app, image="dinosaur.jpg", grid=[0,0])

welcome_message = Text(app, text="Welcome to the Dyno GUI",size=30, color="green", grid=[1,0], width="fill", align="center")

dinopicture2 = Picture(app, image="dinosaur.jpg", grid=[2,0])
"""
Diameter
"""
d_description = Text(app, text="Diameter (mm): ", grid=[1,1], align="left")
input_diameter = TextBox(app, grid=[1,1], width=10, align="center")
update_diameter = PushButton(app, command=updateD, text="Update Diameter",grid=[1,2],align="center" )


"""
Horsepower
"""
h_description = Text(app, text="Horsepower (hp): ", grid=[1,4], align="left")
input_horsepower = TextBox(app, grid=[1,4], width=10, align="center")
update_horsepower = PushButton(app, command=updateH, text="Update Horsepower", grid=[1,5],align="center" )


"""
initiates the dyno
"""
mydyno = dynamometer(0, 0)
show_info = PushButton(app,command=displayValues, text= "Calculate Results", grid=[1,6])

app.display()

    

