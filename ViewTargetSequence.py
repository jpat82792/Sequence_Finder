from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button
import re
import UiConstants


class ViewTargetSequence(Screen):

    def __init__(self, next_screen, previous_screen, screen_manager, secretary, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.label_screen = Label(text="Target Sequence", size_hint_y=0.2, size_hint_x=0.5, color=[0, 0, 0, 1],
                                  pos_hint={'y': 0.8, 'x': 0.25}, font_size=UiConstants.UiConstants.labe_main_screen,
                                  font_name="fonts/RobotoMono-Bold.ttf")
        self.text_input_before_target_sequence = TextInput(hint_text="Units before target", size_hint_y=0.1,
                                                           font_name="fonts/RobotoMono-Regular.ttf",
                                                           background_normal="backgrounds/input-background.jpg",
                                                           size_hint_x=0.35, pos_hint={'y': 0.68, 'x': 0.40})
        self.text_input_target_sequence = TextInput(hint_text="Target sequence",font_name="fonts/RobotoMono-Regular.ttf",
                                                    size_hint_y=0.2, size_hint_x=0.35,
                                                    pos_hint={'y': 0.46, 'x': 0.4}, background_normal="backgrounds/input-background.jpg")
        self.text_input_after_target_sequence = TextInput(hint_text="Units after target",
                                                          background_normal="backgrounds/input-background.jpg",
                                                          font_name="fonts/RobotoMono-Regular.ttf", size_hint_y=0.1,
                                                          size_hint_x=0.35, pos_hint={'y': 0.34, 'x': 0.4})
        self.text_input_target_sequence.input_filter = self.target_input_filter
        self.text_input_after_target_sequence.input_filter = self.target_input_filter
        self.text_input_before_target_sequence.input_filter = self.target_input_filter
        self.button_next_screen = Button(text="NEXT", size_hint_y=0.1,
                                         size_hint_x=0.25, pos_hint={'y': 0.0, 'x': 0.5},
                                         background_normal="backgrounds/next-button.jpg",
                                         background_down="backgrounds/next-button-pressed.jpg",
                                         font_size=UiConstants.UiConstants.label_font_size,
                                         font_name="fonts/RobotoMono-Bold.ttf",
                                         on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                                       screen_manager=screen_manager,
                                                                                       secretary=secretary, btn=btn))
        self.button_prev_screen = Button(text="PREV", size_hint_y=0.1,
                                         size_hint_x=0.25, pos_hint={'y': 0, 'x': 0.25},
                                         background_normal="backgrounds/back-button.jpg",
                                         font_size=UiConstants.UiConstants.label_font_size,
                                         background_down="backgrounds/back-button-down.jpg",
                                         font_name="fonts/RobotoMono-Bold.ttf",
                                         on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                             screen_manager=screen_manager))
        self.label_units_before_target = Label(text="Units before target", size_hint_x=0.25, size_hint_y=0.1,
                                               pos_hint={'x': 0.15, 'y': 0.68}, color=[0, 0, 0, 1])
        self.label_target_sequence = Label(text="Target Sequence", size_hint_x=0.25, size_hint_y=0.2,
                                           pos_hint={'x': .15, 'y': .46}, color=[0, 0, 0, 1])
        self.label_units_after_target = Label(text="Units after target", size_hint_x=0.25, size_hint_y=0.1,
                                              pos_hint={'x': .15, 'y': .34}, color=[0, 0, 0, 1])

        self.main_layout.add_widget(self.label_screen)
        self.main_layout.add_widget(self.text_input_before_target_sequence)
        self.main_layout.add_widget(self.label_units_before_target)
        self.main_layout.add_widget(self.text_input_target_sequence)
        self.main_layout.add_widget(self.label_target_sequence)
        self.main_layout.add_widget(self.text_input_after_target_sequence)
        self.main_layout.add_widget(self.label_units_after_target)
        self.main_layout.add_widget(self.button_next_screen)
        self.main_layout.add_widget(self.button_prev_screen)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def target_input_filter(self, string, undo):
        string = re.sub('[~`!@#$%^&*()_=+\\\[\];"{}|:,<>./?1234567890]', '', string)
        return string.upper()

    def go_back(self, previous_screen, screen_manager):
        screen_manager.current = previous_screen

    def go_to_next_screen(self, next_screen, secretary, screen_manager, btn):
        secretary.target_sequence = self.text_input_target_sequence.text
        secretary.before_target_sequence = self.text_input_before_target_sequence.text
        secretary.after_target_sequence = self.text_input_after_target_sequence.text
        secretary.translate_target()
        screen_manager.current = next_screen
