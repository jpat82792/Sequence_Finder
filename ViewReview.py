from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.button import Button


class ViewReview(Screen):

    def __init__(self, next_screen, previous_screen, secretary, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.label_screen = Label(text="Review", size_hint=(0.5, 0.2), pos_hint={'x': 0.25, 'y': 0.8})
        self.main_layout.add_widget(self.label_screen)
        self.label_sequence_type = Label(text="Sequence Type:", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.7})
        self.text_input_sequence_type = TextInput(text="secretary",
                                                  size_hint=(0.25, 0.1),
                                                  pos_hint={'x': 0.5, 'y': 0.7})
        self.label_units_before = Label(text="Units before", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y':0.6})
        self.label_units_target = Label(text="Target sequence", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.5})
        self.label_units_after = Label(text="Units after", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.4})
        self.label_units_path = Label(text="Path", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.3})
        self.label_units_file_name = Label(text="File name", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0.2})
        self.text_input_units_before = TextInput(text=secretary.before_target_sequence, size_hint=(0.25, 0.1),
                                                 pos_hint={'x': 0.5, 'y': 0.6})
        self.text_input_target = TextInput(text=secretary.target_sequence, size_hint=(0.25, 0.1),
                                           pos_hint={'x': 0.5, 'y': 0.5})
        self.text_input_units_after = TextInput(text=secretary.after_target_sequence, size_hint=(0.25, 0.1),
                                                pos_hint={'x': 0.5, 'y': 0.4})
        self.text_input_units_path = TextInput(text=secretary.output_file_path, size_hint=(0.25, 0.1),
                                               pos_hint={'x': 0.5, 'y': 0.3})
        self.text_input_units_file_name = TextInput(text=secretary.output_file_name,
                                                    size_hint=(0.25, 0.1), pos_hint={'x': 0.5, 'y': 0.2})
        self.button_run_analysis = Button(text="Run analysis", size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 0.1},
                                          on_release=lambda btn: self.run_analysis(secretary=secretary,
                                                                                   screen_manager=screen_manager,
                                                                                   next_screen=next_screen))
        self.button_previous_screen = Button(text="Previous", size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 0},
                                             on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                                 screen_manager=screen_manager))

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

