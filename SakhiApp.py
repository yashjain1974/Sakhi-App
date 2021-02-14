from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition,FadeTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import  TwoLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFillRoundFlatButton,MDRaisedButton

from structure import helper_code
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


import time

initial = time.time()

r = time.asctime(time.localtime(time.time()))
Window.size=(300,500)


class FirstScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    def check_data_login(self):
        username = self.username.text
        password = self.password.text

        print(username)
        print(password)
class Books(Screen):
    pass
class Todo(Screen):
    pass
class Meditation(Screen):
    pass
class WomenSafety(Screen):
    pass

class NearbyHospitals(Screen):
    pass

class NearbyPolicestation(Screen):
    pass

class HelpLineNumbers(Screen):
    pass


sm=ScreenManager(transition=NoTransition())
sm.add_widget(FirstScreen(name="First"))
sm.add_widget(LoginScreen(name="Login"))
sm.add_widget(MainScreen(name="Main"))
sm.add_widget(Books(name="book"))
sm.add_widget(Todo(name="todo"))
sm.add_widget(Meditation(name="meditation"))
sm.add_widget(WomenSafety(name="womensafety"))
sm.add_widget(NearbyHospitals(name="hospital"))
sm.add_widget(NearbyPolicestation(name="policestation"))
sm.add_widget(HelpLineNumbers(name="helpline"))


class SakhiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Pink"
        self.screen=Builder.load_string(helper_code)

        return  self.screen
    def submit(self,obj):
        print("hello g")
    def clock_bar(self):
        btn = MDFillRoundFlatButton(text="OK",on_release=self.exit_dialogue)
        self.dialogue = MDDialog(title="Present time ", text=f"Time: {r}", size_hint=(0.7, None), buttons=[btn])
        self.dialogue.open()
    def exit_dialogue(self,obj):
        self.dialogue.dismiss()
    def botton_icon(self):
        btn = MDFillRoundFlatButton(text="OK",on_release=self.exit_dialogue)
        self.dialogue=MDDialog(title="Welcome ",text="Hello guys",size_hint=(0.7, None), buttons=[btn])
        self.dialogue.open()
    def navigation_draw(self):
        btn = MDFillRoundFlatButton(text="OK", on_release=self.exit_dialogue)
        self.dialogue = MDDialog(title="Welcome ", text="Coffee Time", size_hint=(0.7, None), buttons=[btn])
        self.dialogue.open()






if __name__ == '__main__':
    SakhiApp().run()