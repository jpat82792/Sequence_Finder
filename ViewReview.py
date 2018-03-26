from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.button import Button
import UiConstants


class ViewReview(Screen):

    def __init__(self, next_screen, previous_screen, secretary, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.label_screen = Label(text="Review", size_hint=(0.5, 0.15), pos_hint={'x': 0.25, 'y': 0.85},
                                  font_name="fonts/RobotoMono-Bold.ttf",
                                  font_size=UiConstants.UiConstants.labe_main_screen, color=[0,0,0,1])
        self.main_layout.add_widget(self.label_screen)
        self.label_sequence_type = Label(text="Sequence Type:", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.73},
                                         color=[0, 0, 0, 1])
        self.text_input_sequence_type = TextInput(text="secretary",
                                                  size_hint=(0.25, 0.1),
                                                  pos_hint={'x': 0.5, 'y': 0.73}
                                                  , background_normal="backgrounds/input-background.jpg")
        self.label_units_before = Label(text="Units before", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.61}
                                        , color=[0, 0, 0, 1])
        self.label_units_target = Label(text="Target sequence", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.49}
                                        , color=[0, 0, 0, 1])
        self.label_units_after = Label(text="Units after", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.37}
                                       , color=[0, 0, 0, 1])
        self.label_units_path = Label(text="Path", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.25}
                                      , color=[0, 0, 0, 1])
        self.label_units_file_name = Label(text="File name", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.13}
                                           , color=[0, 0, 0, 1])
        self.text_input_units_before = TextInput(text=secretary.before_target_sequence, size_hint=(0.25, 0.1),
                                                 pos_hint={'x': 0.5, 'y': 0.61}, background_normal="backgrounds/input-background.jpg")
        self.text_input_target = TextInput(text=secretary.target_sequence, size_hint=(0.25, 0.1),
                                           pos_hint={'x': 0.5, 'y': 0.49},background_normal="backgrounds/input-background.jpg")
        self.text_input_units_after = TextInput(text=secretary.after_target_sequence, size_hint=(0.25, 0.1),
                                                pos_hint={'x': 0.5, 'y': 0.37},background_normal="backgrounds/input-background.jpg")
        self.text_input_units_path = TextInput(text=secretary.output_file_path, size_hint=(0.25, 0.1),
                                               pos_hint={'x': 0.5, 'y': 0.25},background_normal="backgrounds/input-background.jpg")
        self.text_input_units_file_name = TextInput(text=secretary.output_file_name,
                                                    size_hint=(0.25, 0.1), pos_hint={'x': 0.5, 'y': 0.13}
                                                    , background_normal="backgrounds/input-background.jpg")
        self.button_run_analysis = Button(text="Run analysis", size_hint=(0.25, 0.1), pos_hint={'x': 0.5, 'y': 0},
                                          on_release=lambda btn: self.run_analysis(secretary=secretary,
                                                                                   screen_manager=screen_manager,
                                                                                   next_screen=next_screen),
                                          font_size=UiConstants.UiConstants.label_font_small_size,
                                          background_normal="backgrounds/next-button.jpg",
                                          background_down="backgrounds/next-button-pressed.jpg",
                                          font_name="fonts/RobotoMono-Bold.ttf",)
        self.button_previous_screen = Button(text="Previous", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0},
                                             font_size=UiConstants.UiConstants.label_font_small_size,
                                             on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                                 screen_manager=screen_manager),
                                             background_normal="backgrounds/back-button.jpg",
                                             background_down="backgrounds/back-button-down.jpg",
                                             font_name="fonts/RobotoMono-Bold.ttf")

        self.main_layout.add_widget(self.label_sequence_type)
        self.main_layout.add_widget(self.text_input_sequence_type)

        self.main_layout.add_widget(self.label_units_before)
        self.main_layout.add_widget(self.text_input_units_before)

        self.main_layout.add_widget(self.label_units_target)
        self.main_layout.add_widget(self.text_input_target)

        self.main_layout.add_widget(self.label_units_after)
        self.main_layout.add_widget(self.text_input_units_after)
        self.main_layout.add_widget(self.label_units_path)
        self.main_layout.add_widget(self.text_input_units_path)
        self.main_layout.add_widget(self.label_units_file_name)
        self.main_layout.add_widget(self.text_input_units_file_name)
        self.main_layout.add_widget(self.button_run_analysis)
        self.main_layout.add_widget(self.button_previous_screen)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def reload_ui(self, secretary):
        self.text_input_units_before.text = secretary.before_target_sequence
        self.text_input_target.text = secretary.target_sequence
        self.text_input_units_after.text = secretary.after_target_sequence
        self.text_input_sequence_type.text = secretary.sequence_type
        self.text_input_units_file_name.text = secretary.output_file_name
        self.text_input_units_path.text = secretary.output_file_path

    def go_back(self, previous_screen, screen_manager):
        screen_manager.current = previous_screen

    def run_analysis(self, secretary, screen_manager, next_screen):
        print("run_analysis()")
        secretary.get_target_sequences()
        screen_manager.current = next_screen

