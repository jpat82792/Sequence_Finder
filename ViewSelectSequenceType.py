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

    def __init__(self, next_screen, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.dropdown_sequence_type = DropDown()
        for index in range(len(self.sequence_types)):
            btn = Button(text=self.sequence_types[index], height=60, size_hint_y=None)
            btn.bind(on_release=lambda btn: self.dropdown_sequence_type.select(btn.text))
            self.dropdown_sequence_type.add_widget(btn)
        self.button_dropdown = Button(text="Select Sequence Type", size_hint_x=0.5, size_hint_y=0.1, font_size="30sp",
                                      pos_hint={'y': 0.8, 'x': 0.25})
        self.button_dropdown.bind(on_release=self.dropdown_sequence_type.open)
        self.dropdown_sequence_type.bind(on_select=lambda instance, x: setattr(self.button_dropdown, 'text', x))
        self.main_layout.add_widget(self.button_dropdown)
        self.button_next_screen = Button(text="NEXT", size_hint_x=0.5, size_hint_y=0.10, font_size="30sp",
                                         pos_hint={'y': 0.7, 'x': 0.25})
        self.label_screen_id = Label(text="Select Sequence Type", font_size='40sp', size_hint_x=0.5, size_hint_y=0.10,
                                     pos_hint={'y':.9, 'x': 0.25})
        self.main_layout.add_widget(self.label_screen_id)
        self.main_layout.add_widget(self.button_next_screen)
        Clock.schedule_once(self.my_init, 1)

    def my_init(self, *args):
        self.add_widget(self.main_layout)


