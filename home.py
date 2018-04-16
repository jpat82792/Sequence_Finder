from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import kivy
from kivy.resources import resource_add_path
import os
import ViewSelectSequenceType
import ViewSelectSequenceFile
from kivy.uix.screenmanager import ScreenManager, Screen
import ControllerSecretary as ControllerSecretary
import ViewTargetSequence
import ViewOutputDestination
import ViewReview
import sys
import ViewSuccess
from kivy.deps import sdl2, glew
from kivy.core.window import Window
Window.clearcolor = (.901, .901, .901, 1)


project_directory = os.path.dirname(os.path.abspath(__file__))


class SequenceFinderApp(App):
    session_secretary = None

    def resource_path(self):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS)
        return os.path.join(os.path.abspath("."))



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kivy.resources.resource_add_path(self.resource_path())
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
        self.sm.add_widget(ViewSuccess.ViewSuccess(name="Success", previous_screen="Review",
                                                   secretary=self.session_secretary,
                                                   screen_manager=self.sm, home=self))
        self.sm.current = "Sequence Type"

    def set_screens(self):
        '''
        self.session_secretary = ControllerSecretary.ControllerSecretary()
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
        self.sm.add_widget(ViewSuccess.ViewSuccess(name="Success", previous_screen="Review",
                                                   secretary=self.session_secretary,
                                                   screen_manager=self.sm, home=self))
        self.sm.current = "Sequence Type"
        '''

    def build(self):
        return self.sm


if __name__ == '__main__':
    SequenceFinderApp().run()

