from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import os
import ViewSelectSequenceType
import ViewSelectSequenceFile
from kivy.uix.screenmanager import ScreenManager, Screen
import ControllerSecretary as ControllerSecretary
import ViewTargetSequence
import ViewOutputDestination
import ViewReview


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
                                                                         next_screen="Target",
                                                                         secretary=self.session_secretary,
                                                                         screen_manager=self.sm))
        self.sm.add_widget(ViewTargetSequence.ViewTargetSequence(name="Target",
                                                                 next_screen="Save",
                                                                 previous_screen="File name",
                                                                 secretary=self.session_secretary,
                                                                 screen_manager=self.sm
                                                                 ))
        self.sm.add_widget(ViewOutputDestination.ViewOutputDestination(
            name="Save",
            next_screen="Review",
            previous_screen="Target",
            secretary=self.session_secretary,
            screen_manager=self.sm
        ))
        self.sm.add_widget(ViewReview.ViewReview(name="Review", next_screen="Success", previous_screen="Save",
                                                 screen_manager=self.sm, secretary=self.session_secretary))
        self.sm.current = "Save"

    def build(self):
        return self.sm


if __name__ == '__main__':
    HomeApp().run()

