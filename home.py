from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import os
import ViewSelectSequenceType
import ViewSelectSequenceFile
from kivy.uix.screenmanager import ScreenManager, Screen
import ControllerSecretary as ControllerSecretary


project_directory = os.path.dirname(os.path.abspath(__file__))


class HomeApp(App):
    session_secretary = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session_secretary = ControllerSecretary.ControllerSecretary()
        self.sm = ScreenManager()
        self.sm.add_widget(ViewSelectSequenceType.ViewSelectSequenceType(name="Sequence Type",
                                                                         secretary=self.session_secretary,
                                                                         next_screen="File name",
                                                                         screen_manager=self.sm))
        self.sm.add_widget(ViewSelectSequenceFile.ViewSelectSequenceFile(name="File name",
                                                                         previous_screen="Sequence Type",
                                                                         next_screen="",
                                                                         secretary=self.session_secretary,
                                                                         screen_manager=self.sm))
        self.sm.current = "Sequence Type"

    def build(self):
        return self.sm


if __name__ == '__main__':
    HomeApp().run()

