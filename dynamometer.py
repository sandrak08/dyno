# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:06:06 2019

@author: Sandra
"""
import matplotlib.pyplot as plt
import math
import time
from tacho_reader import HallEffectReader, calculate_speed
from dynograph import LineGraph


class dynamometer:
    def __init__(self, d, h):
        """
        Constructor
                
        This initalizes a dyno instance
------------------------------------------------------------------------
        REQUIRED PARAMETERS:
               - d (Wheel Diameter)
               - h (Motor Horsepower)
               
        PARAMETERS GIVEN FROM SENSORS:
               - r (Revolutions Per Minute)
               - p (Mechanical Power)
               
        CALCULATED PARAMETERS:
               - t (torque)

        OPTIONAL PARAMETERS:
               - s (Targeted Speed)
               
------------------------------------------------------------------------
        Below describes the parameters in further detail
        
        :param d = wheel diameter           (meters)
               * Constant
               * Must be provided in initialization or won't construct
        :param t = torque                   (newton * meter)
               * NOT constant
               * Does not have to be provided in initialization
        :param p = power                    (watts)
               * NOT constant, must be read from pedals/sensors
               * Mechanical Power from the Rider (not rly sure how to find this lol)
        :param h = horsepower               (foot-pounds / second) (also 1HP = 746 watts)
               * The Power Rating of a Motor (max)
               * Must be provided in initialization or won't construct
        :param r = revolutions per minute
               * NOT constant
               * Does not have to be provided in initialization
        :param s = speed                    (miles per hour)
               * Targeted speed
               * Does not have to be provided, however can be later changed
        """
        self.wheelDiameter = d
        self.mass = 0
        self.torque = 0
        self.power = 0
        self.horsepower = h
        self.rpm = 1000.0 #temporary for the sake of calculating
        self.speed = 0
        self.tacho = HallEffectReader(12)
        self.degree = 0
        self.incline = None
        
        self.readingamount = 10
        self.xreadings = [] #speed readings
        self.yreadings = [] #power readings
        self.treadings = [] #torque readings
        self.run = 0 #tacho true/false run
    
    def enable_tacho(self):
        self.tacho = HallEffectReader(12)
        
        
    def switch_tacho(self):
        # turns tacho on state
        if self.run == 0:
            self.run = 1
            
        # tacho off state
        else:
            self.run = 0
            
    def run_tacho(self):
        
        #turns on and off tacho every time this function/button is clicked
        self.switch_tacho()
        
        if not self.tacho:
            print("Reader is not initialized")
            return
        

        if self.run == 1:
            try:
                for x in range (0, self.readingamount):
                    # calculate speed
                    elapse = self.tacho.get_elapse()
                    self.speed = self.calculate(elapse)

                    self.torque = self.mass * (self.wheelDiameter /2) * self.speed
                    self.power = (self.torque * 2 * 3.1415 * self.speed) / 33000
                    self.treadings.append(self.torque)
                    self.yreadings.append(self.power)
                    self.xreadings.append(self.speed)
                    # display content every second
                    print("Speed (mph): {:.3f}".format(self.speed))
                    time.sleep(0.5)
            
            # loop until keyboard interrupt (CTRL+C)
            except KeyboardInterrupt:
                reader.clean_up()
        


        """

        if self.run == 1:
            try:
                elapse = 0
                for x in range (0, self.readingamount):
                    # calculate speed
                    #elapse = self.tacho.get_elapse()
                    elapse += 1
                    self.speed = elapse
                    
                    self.torque = self.mass * (self.wheelDiameter /2) * self.speed
                    self.power = (self.torque * 2 * 3.1415 * self.speed) / 33000
                    self.treadings.append(self.torque)
                    self.yreadings.append(self.power)
                    self.xreadings.append(self.speed)
                    
                    #self.speed = self.calculate(elapse)
                    # display content every second
                    print("Speed (mph): {:.3f}".format(self.speed))
                    
                    time.sleep(0.5)
                    
                    
            # loop until keyboard interrupt (CTRL+C)
            except KeyboardInterrupt:
                reader.clean_up()
        """        

    def calculate(self, elapse_time):
        # 1 horsepower = 746 watts
        # 1 watt = 1 newton
        
        # subject to change lol
        self.horsepower = float(self.horsepower)
        #self.torque = (self.horsepower * 746.0 ) / (self.rpm * 1.0)
        self.torque = .5 * self.mass * (self.wheelDiameter /2) * self.rpm
        
        """
        More calculations to come once we get the sensors hooked up*
        """
        
        # to avoid error in frequency calculation
        if elapse_time == 0:
            return 0;
        
        # calculate frequency (rps) and scale (rph)
        frequency = 1 / elapse_time
        frequency = frequency * 3600 
        
        # calculate circumference (mm) and scale (mile)
        circumference = math.pi * self.wheelDiameter
        circumference = circumference * 6.2137e-7
        
        
        
        
        # speed calculation (mph)
        return circumference * frequency
        
    def updateWheel(self, dd):
        self.wheelDiameter = float(dd)
       
    def updateHorse(self, hh):
        self.horsepower = float(hh)
        
    def updateReading(self, r):
        self.readingamount = int(r)
        
    def updateMass(self, m):
        self.mass = int(m)
    """    
    def updateIncline(self, i = 0, direction):
        if i == 0:
            self.degree = 0
    """    
        
    def graphSpeed(self):
        graph1 = LineGraph()
        graph1.addx(self.xreadings)
        graph1.addy(self.yreadings)
        graph1.addt(self.treadings)
        graph1.display_graph()
        

