from mandel_lib import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from firebase import Firebase
from home_21442851 import *
from loginpage import *

config = {
    'apiKey': '',
    'authDomain':'comp-7510-19116.firebaseapp.com',
    'databaseURL': 'https://comp-7510-19116-default-rtdb.firebaseio.com/',
    'storageBucket':'comp-7510-19116.appspot.com',
    'serviceAccount': {
        "type": "service_account",
        "project_id": "comp-7510-19116",
        "private_key_id": "20fd0bde616dd94ee1a773cb526d011a394e8f6f",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCoakELSfpAz5DM\nRWkOhkEZ3+Mf9oYJLPNTC/9FWCORS6CwMnsuC5S6PAhNveriLc1CNZQygxalp+E2\nF2uI6HYzZh5/31sMsB5ZjWPounWvSA4zUDpGPEy3BbZH7XWMEBNvSr4WHSu1ddg9\nOmt6+YMG6zKhBXzK6B7a7CZwdlDT5piJfBTP389ld6Lku96Ee6GSMbM9zfWpckkG\nkvU8eAAVrAMvthPXDit9VZ9fSRhlWCwUYIJwISN2weJaKo/37uueqiQeep2k+Uyq\nmQ9vA6CmdR56dc7ZKRd6AbaiHYKQS01DD77BeqpkcL5RhgtKzObnd8GgfsAo/ExB\nssdbURW1AgMBAAECggEAFrvFDO+O+tmp65EBBedkeUgqAgIGhM2PCOpJKoSjxHSn\ne7FMxGHm0R7SZiAZSS+ykdnmp8zfLTxUn7cYmnH6pqSFwHAXe8Z4SlFWJ6+nvCHn\nXNDbFOkF1/zK5rmskNwIq5C0yQpmAIgoSNeOc5qjr7bm7ipt9nvP0nBnHe4yqe+x\n8SrxfiIzgIDBLRRNgD5khjaUqZwYhfIUF1/4m4B1BnTGuKKE7KSf5YNLXVCrTIwN\nJfFbIxrHoWefZpoqLD/YE+P3mMYy2FxoK2HvDZ/wIlKLURkKx532H9oJjUwr8xWR\nUSY8+OGGdTBYwcmOmcVmZlU3Xuc4uCwycpbIrG45sQKBgQDhEbYS+GIKgxMOZtJp\nZOrZvatzSMLo6BjuhXZq91Nq8zP+WFWu8kVJ3u9cwOk3Wav+VZS6WeXTxDp4O83g\no63t8kctsycPTOMNYnkA2jDrkJpvVpA6fcbdrL/YUDlJVtqvvpivqQh1PwqwNFBa\nkXL+DoJf9XAZWXYEm7Svf1K2KQKBgQC/j1x66obhcLPZuxZlWcq4nsTgEM08AoO0\nBn/XZADfTiRaoW3c8DMGVkt/AlNNXmVrbUNZ4Kt7j+ICs8CoXzxABXxBN4w6Rwj+\nIkkqTWAa+6VN0U/UNDzyWEVQmc93xDYp1N4h8fVqynsqvo8VQnWc3THQCMUwXtem\naX2wDXOcrQKBgHWqw80BLIigZFsYKJNPXnT981/vP29ywG4bOoDL00HL6nfkCM/Q\n+6aWNgABHyx/5iqu5XXTwBNJuOPZKFZ0XF9VVh8vVZFrOh1qSSbH6+GMFSF2WSsr\nTMfiI95cesa78NMGy16y+agKkHT0tLnU5xCp10GB2Nx35/qayQkjgMOZAoGAds1t\nmJm9HzHriNx77k166XcmOKSS9GXG0q65OJc/5z4qU78MSNr7ejGoztNdYH1rvu1b\nuPEayR4aGHzsvj+aOUZtonDV2grWK+6Nm9uy/+kTwyhOLxhauB5AltVdkzSwNs9b\nGIhcIWgEbSUTziaSlL+mNhRKX05ixkVkevxMuF0CgYEAsxcjWro7c744zz/Zy/o1\nb2lwGLWrzZj2Mq3l9rZ2+5vZ4aTpf/NDYqjeQeUjaiLJmyDv8PDOUB4MKtCBKQhs\ni6sWfuGvAaDoRmALnNqIMiATHjjgnTX+sewrVGZ4AECt+z8ZgPn66RIGijsA3Zio\nqLoZEX4jRM+TuUlW1V/6gUc=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-k0spe@comp-7510-19116.iam.gserviceaccount.com",
        "client_id": "113199756909304717844",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-k0spe%40comp-7510-19116.iam.gserviceaccount.com"
    }   
}

myfirebase = Firebase(config)
db = myfirebase.database() # real-time database object
storage = myfirebase.storage() # storage object

class reg(Screen):
    def back(self):
        MDApp.get_running_app().switchTo('home')
        
    def reg(self):
        #name = self.ids.name_field.text 
        #name = name.strip()
        #email = self.ids.email_field.text 
        #email = email.strip()
        password = self.ids.password_field.text 
        password = password.strip()
        phone = self.ids.phone_field.text 
        phone = phone.strip()
        receiver = (f'/{phone}')
        resultb = db.child(f'/{receiver}/phone').get().val()
        if len(password) == 0 or len(phone) == 0:
            self.show_dialog()

        elif phone == resultb:
            self.show_dialogb()
            
        else:
            #response = db.child('userinformation').get().val()
            #key = response.key()
            #value = response.val()
            receiver = (f'/{phone}')
            data = dict( password=password, phone=phone)
            response = db.child(f'/{receiver}').set(data)
            print(response)
            MDApp.get_running_app().switchTo('home')
            self.ids.password_field.text = ''
            self.ids.phone_field.text = '' 

    def show_dialog(self):
        dialog = MDDialog(
            title = 'Error',
            text = 'Please input all data!',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()
    
    def show_dialogb(self):
        dialog = MDDialog(
            title = 'Error',
            text = 'The phone number has been registered',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
        dialog.open()
    
    def login(self):
        self.ids.password_field.text = ''
        self.ids.phone_field.text = '' 
        MDApp.get_running_app().switchTo('log')

    def cancel(self):
        #password = self.ids.password_field.text 
        #phone = self.ids.phone_field.text 
        self.ids.password_field.text = ''
        self.ids.phone_field.text = '' 
        MDApp.get_running_app().switchTo('home')

    def clear(self):
        self.ids.password_field.text = ''
        self.ids.phone_field.text = '' 