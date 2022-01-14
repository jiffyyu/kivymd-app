from kivy.uix.screenmanager import Screen
from home_21427593 import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform
from kivy.uix.image import Image

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from firebase import Firebase

config = {

 'apiKey': '',

    'authDomain':'comp7510-11b96.firebaseapp.com',

    'databaseURL': 'https://comp7510-11b96-default-rtdb.firebaseio.com/',

    'storageBucket':'comp7510-11b96.appspot.com',

    'serviceAccount': {

        "type": "service_account",

        "project_id": "comp7510-11b96",

        "private_key_id": "1403d68b539f7a74eb01d9e8adb868bfba47864e",

        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5Fl7o9H+NbJW9\nMicBgRm4XDz6YMm04r/1+5KFoKU8itTeojxQScGwB+nWRPuu9sXzFV3vTMde6fj6\nbOXKitDdlnuEXR52+6tnPrlV9wYdVMXwji63jbkzejxi3k7ZSEyM24X9yVN59Dyx\n4pl4N1POfLJZi209uQrqG4VS6sFbXTmAlG5gwFFN1T/LczbfWrlyMAET8sxmQczZ\nqxAqx6Swu6G7gDHTjTv0j8Uq/vNcJgsYUuYgKw1MgNKka+UpiOycBqxbUiyQeVko\nYMDmNH0jhgq1l0DBldAbk7fDW9o8G2HSexI4NH4u6t11q69/+vRjMCF2aICo+ZB7\n8g4w9AJ9AgMBAAECggEARtZPg9QTv1JIKu13bUV2TQ+MTP1fJYpFEsVyag82Pmoa\nF407DTV1WkRlFBs5wlhzIVpTpcMaaPKeVmX4OqEPWEeARYQIJVyj2LNyZnrRDcfE\nrBEWwyyMLa4CT4qq3dEkbyKTcTKs7rdxxVknCJIQUq556fiJWj6odToMOFRdpXPs\nQqHNWfJGpqepO2HP6T4oprZRoqRxEK9oiKEzw5llEORc9OwhN7TadkVbhpPOnnu+\nIBDkwdW6s0A207ZUdvxD3jlPffH+lnQxSthmXSykrG56EEYFwp+/Up3xPzUKEQpC\nuZx4/mOg8R4mjlXchYGaJa2REOVSSWdLtrScsPnwNwKBgQD1Hb6oj6uKt3Zxn2g4\nnhxPlZFhRDqfbCZE1Mu0BiYpXWRnN57NRuxa1l2Kx7mYRTKhCkOd4prM6ocpBw93\nD9+fYGiiLOVGmUaXf6mOsAZO+fK+rPtSDt1HFxFps8QHXpt7rfU2WvBBDMon00xC\nKBV3c9uwRhxeiyq+Kj87t3QskwKBgQDBTkYWnM2XPGIVLpwAZxkr94YW/v/aQON9\nxYEQmRK0L+e19SojCq+a+UgjVRX54GjgsKVrQDzYWEUYvzgK8VA7jj7x/q96mH2w\nUr7uLkAAihW1Uxa+pTE5ueH+45NMq/cKLWkbSF7T9wKel/kugm4VLf/j+CS0UyPi\nisTY+vCOrwKBgQCAs4SHZyBwLpJ/aG7Fw6cj1mnGQ5fwW03guEbZGJ1y/LmaRKca\nK9Iwg/wLwYDexf6mdgg432HelIoxbaaeInSNb4ahGKeuIQ7iv0JdTGmTkEP4AEXZ\nuTpQeHlJIf2czP0gvJ9TUf5yeW+v549T8U4MMYY5kSaWMcZYoUAgb9wNBwKBgAMx\nAaM574MBsjTbUiQHj7jUG1ih2SOHUrou2pSlklN7Pv4YEBwH/yI132UF8JjxhYnA\nINsGcnq36lwgPBKiLUrubEeehtMlVV3l39Ua2l+n5/fYaVW4cHmdggetRi9L34ZB\nfay/oyEowNhRdgG4kYyz97eRzzlS7hK9a8aRTgttAoGAYvX90T6IHfDotsmLJXfa\nPqnYX7H+sj8A/emMDabX9miFuKd7V3IZiur5WdcmvxmbVpLumMuXkjfQI17fOpWn\nR41aAIv8g6DXn4CuVmoboZX1Lvr36peA13m30OKbHldizSRUuxlQ9buvwJSASdab\nlfe1sVw3I88sq4Nk2gqJfYc=\n-----END PRIVATE KEY-----\n",

        "client_email": "firebase-adminsdk-e44jf@comp7510-11b96.iam.gserviceaccount.com",

        "client_id": "110974287057288712905",

        "auth_uri": "https://accounts.google.com/o/oauth2/auth",

        "token_uri": "https://oauth2.googleapis.com/token",

        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",

        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-e44jf%40comp7510-11b96.iam.gserviceaccount.com"

    }

}

if platform in ('win', 'macosx'):

    Window.size = (414, 736)

    Window.top = 50

myfirebase = Firebase(config)

db = myfirebase.database() # real-time database object 

storage = myfirebase.storage() # storage object
class Screen3(Screen):
    def button_back(self):
        MDApp.get_running_app().switchTo('screenB')
    def button_clickme(self):

        age = self.ids.age.text
        age = int(age)
        if age < int(18):  

            dialog = MDDialog(

                title = 'You can not make the appointment!',

                text = 'Your age < 18.', 

                buttons = [

                    MDRaisedButton(

                        text = 'Close',

                        on_release = lambda x: dialog.dismiss()),

                ]

            )

            dialog.open()
        
        else:
               
            MDApp.get_running_app().switchTo('screen6')
        print('Oh, you click me!')

class Screen6(Screen):
    def button_back(self):


        MDApp.get_running_app().switchTo('screen3')
    
    def click(self):
    
        name = self.ids.name.text
        name = name.strip()
        
        idnumber = self.ids.idnumber.text
        idnumber = idnumber.strip()
        
        address = self.ids.address.text
        address = address.strip()

        phonenumber = self.ids.phonenumber.text
        phonenumber = phonenumber.strip()

        if len(name) == 0 or len(idnumber) == 0 or len(address) == 0 or len(phonenumber) == 0:  

            dialog = MDDialog(

                title = 'Appointment Fail.',

                text = 'Please input your information/Input the correct information.', 

                buttons = [

                    MDRaisedButton(

                        text = 'Close',

                        on_release = lambda x: dialog.dismiss()),

                ]

            )

            dialog.open()

        else:
            self.ids.label.text = 'Successful Appointment.' 
           
            myfirebase = Firebase(config)

            db = myfirebase.database() # real-time database object 

            storage = myfirebase.storage() # storage object

            response =db.child('userinfo').get()

            key = response.key()

            value = response.val()

            data = dict( name=name.strip(), idnumber=idnumber.strip(),phonenumber=phonenumber.strip(),address=address.strip())

            respsonse = db.child('appointmentinfo').push(data)

            MDApp.get_running_app().switchTo('screen3')

        print(f'You inputted:{name}/{idnumber}/{phonenumber}/{address}')
    def clear(self):
        self.ids.name.text = ''
        self.ids.idnumber.text = '' 
        self.ids.phonenumber.text = ''
        self.ids.address.text = ''    


        
    
class MDApp(MDApp):

    def build(self):
       
        Builder.load_file('screen3.kv')
        Builder.load_file('screen6.kv')
       
        manager = self.manager = ScreenManager()

       

        manager.add_widget(Screen3())

        manager.add_widget(Screen6())
        

        return manager

    def switchTo(self, screen_name):

        self.manager.current = screen_name
if __name__ == '__main__':
    MDApp().run()

