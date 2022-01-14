from mandel_lib import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from reg_21442851 import *
from loginpage import*
from home_21427593 import*
from screen1 import *
from screen2 import *
from screen3 import *
from screen4 import *
from screen5 import *
from kivy.core.window import Window
from kivy.utils import platform
if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50
class home(Screen):
    def clickme(self):
        MDApp.get_running_app().switchTo('log')

    def register(self):
        MDApp.get_running_app().switchTo('reg')

class MyApp(MDApp): 
    manager = None
    def build(self):
        Builder.load_file('home_21442851.kv') 
        Builder.load_file('reg_21442851.kv')
        Builder.load_file('home_21427593.kv')
        Builder.load_file('loginpage.kv')
        Builder.load_file('screen1.kv')
        Builder.load_file('screen2.kv')
        Builder.load_file('screen3.kv')
        Builder.load_file('screen4.kv')
        Builder.load_file('screen5.kv')
        Builder.load_file('screen6.kv')
        manager = self.manager = ScreenManager() 
        manager.add_widget(home()) 
        manager.add_widget(reg())
        manager.add_widget(log())
        manager.add_widget(ScreenB())
        manager.add_widget(Screen1())
        manager.add_widget(Screen2())
        manager.add_widget(Screen3())
        manager.add_widget(Screen4())
        manager.add_widget(Screen5())
        manager.add_widget(Screen6())
        manager.add_widget(DetailScreen())
        return manager

    def switchTo(self, screen_name): 
        self.manager.current = screen_name

if __name__ == '__main__': 
    MyApp().run()