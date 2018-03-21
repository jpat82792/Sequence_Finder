from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button


class ViewTargetSequence(Screen):

    def __init__(self, next_screen, previous_screen, screen_manager, secretary, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.label_screen = Label(text="Target Sequence", size_hint_y=0.2, size_hint_x=0.5,
                              pos_hint={'y': 0.8, 'x': 0.25})
        self.text_input_before_target_sequence = TextInput(hint_text="Units before target", size_hint_y=0.1,
                                                       size_hint_x=0.5, pos_hint={'y': 0.7, 'x': 0.25})
        self.text_input_target_sequence = TextInput(hint_text="Target sequence", size_hint_y=0.2, size_hint_x=0.5,
                                                pos_hint={'y': 0.5, 'x': 0.25})
        self.text_input_after_target_sequence = TextInput(hint_text="Units after target", size_hint_y=0.1,
                                                      size_hint_x=0.5, pos_hint={'y': 0.4, 'x': 0.25})
        self.button_next_screen = Button(text="NEXT", size_hint_y=0.1,
                                 size_hint_x=0.5, pos_hint={'y': 0.3, 'x': 0.25},
                                 on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                               screen_manager=screen_manager,
                                                                               secretary=secretary, btn=btn))
        self.button_prev_screen = Button(text="PREV", size_hint_y=0.1,
                                         size_hint_x=0.5, pos_hint={'y': 0.2, 'x': 0.25},
                                         on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                         screen_manager=screen_manager))

        self.main_layout.add_widget(self.label_screen)
        self.main_layout.add_widget(self.text_input_before_target_sequence)
        self.main_layout.add_widget(self.text_input_target_sequence)
        self.main_layout.add_widget(self.text_input_after_target_sequence)
        self.main_layout.add_widget(self.button_next_screen)
        self.main_layout.add_widget(self.button_prev_screen)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def go_back(self, previous_screen, screen_manager):
        screen_manager.current = previous_screen

    def go_to_next_screen(self, next_screen, secretary, screen_manager, btn):
        screen_manager.current = next_screen
