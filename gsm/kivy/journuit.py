from kivy.app import App
from kivy.uix.label import Label
from datetime import datetime


class TimeApp(App):
    def build(self):
        hour = datetime.now().hour
        print(hour)
        message = "Il fait jour" if 6 <= hour < 15 else "Il fait nuit"
        return Label(text=message, font_size=50)


TimeApp().run()
