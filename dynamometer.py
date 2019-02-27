# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:06:06 2019

@author: Sandra
"""

import math

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
        self.torque = 0
        self.power = 0
        self.horsepower = h
        self.rpm = 1000.0 #temporary for the sake of calculating
        self.speed = 0
    
    def calculate(self):
        # 1 horsepower = 746 watts
        # 1 watt = 1 newton
        
        # subject to change lol
        self.horsepower = float(self.horsepower)
        self.torque = (self.horsepower * 746.0 ) / (self.rpm * 1.0)
        
        
        """
        More calculations to come once we get the sensors hooked up*
        """
        
    def updateWheel(self, dd):
        self.wheelDiameter = dd
       
    def updateHorse(self, hh):
        self.horsepower = hh
