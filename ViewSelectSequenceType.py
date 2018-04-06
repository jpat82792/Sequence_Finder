from kivy.uix.label import Label
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown
from kivy.uix.relativelayout import RelativeLayout

project_directory = os.path.dirname(os.path.abspath(__file__))


class ViewSelectSequenceType(Screen):

    sequence_types = ["Nucleotide", "Amino Acid"]

    def __init__(self, next_screen, secretary, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.dropdown_sequence_type = DropDown()
        for index in range(len(self.sequence_types)):
            btn = Button(text=self.sequence_types[index], height=60, size_hint_y=None,
                         font_name="fonts/RobotoMono-Bold.ttf", background_normal="backgrounds/dropdown-options.jpg",
                         background_down="backgrounds/dropdown-background-pressed.jpg"
                         )
            btn.bind(on_release=lambda btn: self.dropdown_sequence_type.select(btn.text))
            self.dropdown_sequence_type.add_widget(btn)
        self.button_dropdown = Button(text="Select Sequence Type", size_hint_x=0.5, size_hint_y=0.2, font_size="30sp",
                                      pos_hint={'y': 0.5, 'x': 0.25}, font_name="fonts/RobotoMono-Bold.ttf"
                                      , background_normal="backgrounds/dropdown-background.jpg",
                                      background_down="backgrounds/dropdown-background-pressed.jpg")
        self.button_dropdown.bind(on_release=self.dropdown_sequence_type.open)
        self.dropdown_sequence_type.bind(on_select=lambda instance, x: setattr(self.button_dropdown, 'text', x))
        self.main_layout.add_widget(self.button_dropdown)
        self.button_next_screen = Button(text="NEXT", size_hint_x=0.5, size_hint_y=0.1, font_size="30sp",
                                         background_color=[0, .05, 1, 1],
                                         background_normal="backgrounds/next-button.jpg",
                                         background_down="backgrounds/next-button-pressed.jpg",
                                         pos_hint={'y': 0.0, 'x': 0.25}, font_name="fonts/RobotoMono-Bold.ttf",
                                         on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                                       secretary=secretary,
                                                                                       screen_manager=screen_manager,
                                                                                       btn=btn))
        self.label_screen_id = Label(text="Sequence Type", font_size='40sp', size_hint_x=0.5, size_hint_y=0.20,
                                     pos_hint={'y': .8, 'x': 0.25}, font_name="fonts/RobotoMono-Bold.ttf",
                                     color=[0, 0, 0, 1])
        self.main_layout.add_widget(self.label_screen_id)
        self.main_layout.add_widget(self.button_next_screen)
        Clock.schedule_once(self.my_init, 1)

    def my_init(self, *args):
        self.add_widget(self.main_layout)

    def go_to_next_screen(self, next_screen, secretary, screen_manager, btn):
        if self.button_dropdown.text != "Select Sequence Type" :

            print("Got here")
            secretary.sequence_type = self.button_dropdown.text
            screen_manager.current = next_screen
        else:
            print("invalid input")



