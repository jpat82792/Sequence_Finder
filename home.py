from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import os
import ViewSelectSequenceType
from kivy.uix.screenmanager import ScreenManager, Screen
import ControllerSecretary.ControllerSecretary as ControllerSecretary


project_directory = os.path.dirname(os.path.abspath(__file__))


class HomeApp(App):
    session_secretary = None

    def __init__(self):
        self.session_secretary = ControllerSecretary()
        sm = ScreenManager()
        sm.add_widget(ViewSelectSequenceType.ViewSelectSequenceType(name="Sequence Type", next_screen=""))
        sm.current = "Sequence Type"

    def build(self):
        return self.sm


if __name__ == '__main__':
    HomeApp().run()

