import kivy
import AbstractScreen
from kivy.uix.label import Label
from kivy.lang.builder import Builder
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.filechooser import FileChooser
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout

project_directory = os.path.dirname(os.path.abspath(__file__))


class ViewSelectSequenceType(Screen):

    sequence_types = ["Nucleotide", "Amino Acid"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.main_layout = AnchorLayout(anchor_x="left", anchor_y="top")
        self.main_layout = RelativeLayout()

        self.button_dropdown = Button(text="hello", size_hint_x=0.5, size_hint_y=0.05, pos_hint={'y': 0.95, 'x': 0.25})
        self.main_layout.add_widget(self.button_dropdown)
        Clock.schedule_once(self.my_init, 1)

    def my_init(self, *args):
        self.add_widget(self.main_layout)


