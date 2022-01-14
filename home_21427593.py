from os import name
from firebase import Firebase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton
from mandel_lib import *
from kivy.utils import platform

from screen1 import *
from screen2 import *
from screen3 import *
from screen4 import *
from screen5 import *

if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50
config = { 
    'apiKey': '',
    'authDomain': 'lab2-cb31f.firebaseapp.com',
    'databaseURL': 'https://lab2-cb31f-default-rtdb.firebaseio.com/',
    'storageBucket': 'lab2-cb31f.appspot.com',
    'serviceAccount': {
        "type": "service_account",
        "project_id": "lab2-cb31f",
        "private_key_id": "2c3645b4370d9d9b3be6dc006beb99f82457d902",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCzGEKwZilnpAJT\nM2t5mTobQYJECO4I3ydEk2AJCSmJpObSwP+Z5jOi6eMzzBuLdsS9Zz5FnGQF0C3i\nLq/uvZbDPSxplV4v8a3l4C2oJsZFOIAUh+ypb3hxkVxthVwZsc5THFCJrrWrMkgO\n8/8+vByaGvt2TLbSTyLAsQMKZho2GB0VxOP3rrtzvGDQBgmkDYYNeMTm6cUrcP5e\n9oyoybQ8GPLqSAe84Gs49nE6e4xiu/AY2iEmoaheeHq536oafYLfcl3Bm04wUIRM\njNKQA1h0EQuSBCB5SoUDaUf8paw+8JDWUiMhloyko6YT3SaY2JMZ+XJxryuF+wlp\nZvvlaksRAgMBAAECggEAUXjgYanf/RdlvV6/bi5P+jU3YubjDmMh1Hbssb+ax1Se\nctK8lFDePacDpj0cbLnnbzhH4lfuQpy9Os89VrClpISwLwn1sn7RuqjcbEnTWYsF\n7REWjs+4bYWQk/wedUvnTfSsCK5TU6GImVDTVUEzC8Hpkhv88Thx2VHNTc47704O\n41QZZc26tkdVhFY27OiZ7KdujtyDvZY2zjKFSy1KwA5UOMg1qV2lDew3Jaq/JR1F\npj7DM6iu+S8XLsWl30p/Nbt8oFRK5AZz8q2l0qD90ZkVYSpsfgGmEHfW5NI8R+Dy\ncjdb7rkHID27RwzYIxFBIfEHwfpnFS1o4cROZeACpwKBgQDg+RHUrvG3R361FgzU\nCPDO6hvVaamyhsCNaBHMHqjj8rGDVoUuEzvKJsFP9dMVKBl3aDJY510yGJppFXS/\n6Kfc4vD68lPwS1kp7zD3geIbdJc/KXoVifMuBRUl81zNEaF/R8ZvL5/LEtzqNMUN\nwkHGNJxeqIb6giLw41Sx2iSHxwKBgQDLy2i9YFVjLRhKUTsSUD6PtKxFR+izvxKB\nuxJIgiv+gHG3T0UReKugx1ILjJKdOfhLG3qrBvg5RieRawRT/xNIp8dTcxr669QO\nujx2cCCXJisY3dpEW/LymLtBm7VfZI/6IGa8X1DnsTAO79mdO7Ygla1vMPb2m4UY\nmpD56C8GZwKBgFjLlfEXN8p6SpWY5WlPOhTBLEk4kkUnkJp/h/7D3y9RXCUVoi1E\nZCXu1AAGa9D+6cZKdwzGDO+37EIruNACOTciz7CMsvq2ErRNd0tJlX/2rbe9XDVi\nJHx2fxlii69ZFSASqUy7RFu3z0AVoe1DTgi4PTvTUqtPcBEZ+RTVn/ODAoGAcpYH\naVuuBxqG6tprnWtzEbgjmLzK8a4AiOMXb5+JfwrXZZtzmVRBJCCOWCINGcxLeGeV\n/G3pycJRYylKALSOMi7sG1bAF8/bpwA+GNYI7ROv7cZoAEG3A4Ku3z/epilT7u6i\n9U2envd4rx1bPVYinIWsQ7XDVnuxRVk7JNjRAAcCgYA6mfhO2lovikHPysSi5y/W\nzl8fPgx6w6PB1rYol9eQoeZXHKKSJnQLL96FGsC2W4CqaERZRt4FCLS0usUMOWYI\nGVd3MYikc9ON90s4DTCt32AOjayr5KP+sZd3tYVKPFjxaA5GT39a5KC7Uvv2FiBV\nxnQQwDIwY7fKALtT34zTJw==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-xt752@lab2-cb31f.iam.gserviceaccount.com",
        "client_id": "100711858812053144964",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xt752%40lab2-cb31f.iam.gserviceaccount.com"
    }
}
myfirebase = Firebase(config)
storage = myfirebase.storage() 
storage.child('1.jpg').download("firebase2.jpg")

class ScreenB(Screen):

    def to(self):
        MDApp.get_running_app().switchTo('screen1')

    def too(self):
        MDApp.get_running_app().switchTo('screen2')

    def tooo(self):
        MDApp.get_running_app().switchTo('screen3')

    def toooo(self):
        MDApp.get_running_app().switchTo('screen4')

    def tooooo(self):
        MDApp.get_running_app().switchTo('screen5')

