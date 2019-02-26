# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:48:21 2019

@author: Sandra
"""

from guizero import App

app = App(title="Hello bitches")

welcome_message = Text(app, text="Welcome to my app")

app.display()