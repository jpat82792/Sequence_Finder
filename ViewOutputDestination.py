from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ViewOutputDestination(Screen):
    current_directory = "\\"

    def __init__(self,next_screen, previous_screen, secretary, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = RelativeLayout()

        self.label_screen = Label(text="Choose save location", size_hint=(0.5, 0.2), pos_hint={'x': 0.25, 'y': 0.8})
        self.file_chooser = FileChooserIconView(size_hint=(0.5, 0.4), pos_hint={'y': 0.4, 'x': 0.25})
        self.current_directory = self.file_chooser.path
        self.file_chooser.bind(path=self.okay)
        #self.current_directory.set(self.file_chooser.path)
        self.button_next_screen = Button(text="NEXT", size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 0.1},
                                         on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                                       secretary=secretary,
                                                                                       screen_manager=screen_manager))
        self.button_previous_screen = Button(text="PREV", size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 0},
                                             on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                                 screen_manager=screen_manager))
        self.label_current_directory_field = Label(text="Current Directory: ", size_hint=(0.25, 0.1),
                                                   pos_hint={'x': 0.25, 'y': 0.30})
        self.label_current_directory = Label(text=self.current_directory, size_hint=(0.25, 0.1),
                                             pos_hint={'x': 0.5, 'y': 0.3})
        self.label_file_name = Label(text="File name:", size_hint=(0.25, 0.1), pos_hint={'y': 0.2, 'x': 0.25})
        self.text_input_file_name = TextInput(size_hint=(0.25, 0.1), pos_hint={'y': 0.2, 'x': 0.5})
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

    def go_to_next_screen(self, next_screen, secretary, screen_manager):
        screen_manager.current = next_screen

    def go_back(self, previous_screen, screen_manager):
        screen_manager.current = previous_screen

    def path_changed(self, object, value):
        print('filechooser: ', object, "path changed to: ", value)

    def okay(self, object, value):
        print(object)
        self.label_current_directory.text = value
