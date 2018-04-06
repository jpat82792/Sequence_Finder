from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import re
import UiConstants


class ViewOutputDestination(Screen):
    current_directory = "\\"

    def __init__(self, next_screen, previous_screen, secretary, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()

        self.label_screen = Label(text="Choose save location", font_size=UiConstants.UiConstants.labe_main_screen,
                                  size_hint=(0.5, 0.2), pos_hint={'x': 0.25, 'y': 0.8}, color=[0, 0, 0, 1],
                                  font_name="fonts/RobotoMono-Bold.ttf",)
        self.file_chooser = FileChooserIconView(size_hint=(0.7, 0.4), pos_hint={'y': 0.4, 'x': 0.15})
        self.current_directory = self.file_chooser.path
        self.file_chooser.bind(path=self.okay)
        self.button_next_screen = Button(text="NEXT",font_size=UiConstants.UiConstants.label_font_size,
                                         size_hint=(0.25, 0.1), pos_hint={'x': 0.5, 'y': 0.0},
                                         background_normal="backgrounds/next-button.jpg",
                                         background_down="backgrounds/next-button-pressed.jpg",
                                         font_name="fonts/RobotoMono-Bold.ttf",
                                         on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                                       secretary=secretary,
                                                                                       screen_manager=screen_manager))
        self.button_previous_screen = Button(text="PREV", size_hint=(0.25, 0.1), pos_hint={'x': 0.25, 'y': 0},
                                             background_normal="backgrounds/back-button.jpg",
                                             font_size=UiConstants.UiConstants.label_font_size,
                                             background_down="backgrounds/back-button-down.jpg",
                                             font_name="fonts/RobotoMono-Bold.ttf",
                                             on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                                 screen_manager=screen_manager))
        self.label_current_directory_field = Label(text="Current Directory: ",
                                                   font_name="fonts/RobotoMono-Regular.ttf",
                                                   size_hint=(0.25, 0.1),
                                                   pos_hint={'x': 0.25, 'y': 0.30}, color=[0, 0, 0, 1])
        self.label_current_directory = TextInput(text=self.current_directory, size_hint=(0.25, 0.1),
                                             font_name="fonts/RobotoMono-Regular.ttf",
                                             pos_hint={'x': 0.5, 'y': 0.3}
                                                 , background_normal="backgrounds/input-background.jpg", disabled="true",
                                                 background_disabled_normal="backgrounds/input-background.jpg")

        self.label_file_name = Label(text="File name:", size_hint=(0.25, 0.1), pos_hint={'y': 0.18, 'x': 0.25},
                                     font_name="fonts/RobotoMono-Regular.ttf",
                                     color=[0, 0, 0, 1])
        self.text_input_file_name = TextInput(size_hint=(0.25, 0.1), pos_hint={'y': 0.18, 'x': 0.5},
                                              font_name="fonts/RobotoMono-Regular.ttf"
                                              , background_normal="backgrounds/input-background.jpg")
        self.text_input_file_name.input_filter = self.filename_text_filter
        self.main_layout.add_widget(self.label_screen)
        self.main_layout.add_widget(self.file_chooser)
        self.main_layout.add_widget(self.label_current_directory_field)
        self.main_layout.add_widget(self.label_current_directory)
        self.main_layout.add_widget(self.label_file_name)
        self.main_layout.add_widget(self.text_input_file_name)
        self.main_layout.add_widget(self.button_next_screen)
        self.main_layout.add_widget(self.button_previous_screen)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def file_selection(self):
        print("hello")
        print(self.file_chooser.path)

    def filename_text_filter(self, string, undo):
        string = re.sub('[~`!@#$%^&*()_=+;"{|:,<>./?]', '', string)
        return string

    def go_to_next_screen(self, next_screen, secretary, screen_manager):

        if len(self.text_input_file_name.text) > 0:
            secretary.output_file_path = self.label_current_directory.text
            secretary.output_file_name = self.text_input_file_name.text + ".txt"

            screen_manager.current = next_screen
            screen_manager.current_screen.reload_ui(secretary)

        else:
            print("no go")

    def go_back(self, previous_screen, screen_manager):
        screen_manager.current = previous_screen

    def path_changed(self, object, value):
        print('filechooser: ', object, "path changed to: ", value)

    def okay(self, object, value):
        print(object)
        self.label_current_directory.text = value
