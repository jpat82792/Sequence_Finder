from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import os


class ViewSuccess(Screen):

    def __init__(self, secretary, screen_manager, previous_screen, home, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()
        self.text_input_show_results = TextInput(size_hint=(.7, .6), pos_hint={'x': 0.15, 'y': .4})
        self.button_start_new_sequence = Button(text="Run another sequence", size_hint=(.5, .2), pos_hint={'x': 0.25,
                                                                                                           'y': .2},
                                                on_release=lambda btn: self.next_sequence(home))
        self.screen_manager = screen_manager
        self.secretary = secretary
        self.main_layout.add_widget(self.text_input_show_results)
        self.main_layout.add_widget(self.button_start_new_sequence)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def on_pre_enter(self, *args):
        self.render_output_file(text_input=self.text_input_show_results, secretary=self.secretary)

    def load_file(self, secretary):
        print(secretary.output_file_path + secretary.output_file_name)
        result_file_path = os.path.join(secretary.output_file_path, secretary.output_file_name)
        file = open(result_file_path, "r")
        if file.mode == 'r':
            file_content = file.read()
            return file_content
        else:
            return

    def render_output_file(self, text_input, secretary):
        text_input.text = self.load_file(secretary=secretary)

    def next_sequence(self, home):
        self.screen_manager.current= "Sequence Type"
        #self.screen_manager.clear_widgets()
        #home.set_screens()
