import kivy
from kivy.app import App
from kivy.uix.label import Label

# kivy.require('1.11.1')  # replace with your current kivy version !


class MyApp(App):
    def build(self):
        return Label(text='Hello world')


myApp = MyApp()
myApp.run()
