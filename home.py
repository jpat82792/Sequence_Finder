from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import os
import ViewSelectSequenceType
from kivy.uix.screenmanager import ScreenManager, Screen


project_directory = os.path.dirname(os.path.abspath(__file__))
sm = ScreenManager()
sm.add_widget(ViewSelectSequenceType.ViewSelectSequenceType(name="Sequence Type", next_screen=""))
sm.current = "Sequence Type"


class HomeApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    HomeApp().run()

