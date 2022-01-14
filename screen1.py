from kivy.uix.screenmanager import Screen
from home_21427593 import *

class Screen1(Screen):
    def back(self):
        MDApp.get_running_app().switchTo('screenB')
