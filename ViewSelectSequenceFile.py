from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.clock import Clock
import UiConstants as sqFdUi
from kivy.uix.button import Button


class ViewSelectSequenceFile(Screen):

    def __init__(self, next_screen, previous_screen, screen_manager, secretary, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = RelativeLayout()
        self.label_select_sequence_file = Label(text="Select Sequence File", size_hint_y=0.2,
                                                size_hint_x=0.5, pos_hint={'y': 0.8, 'x': 0.25},
                                                font_size=sqFdUi.UiConstants.label_font_size)
        self.file_chooser_icon_view = FileChooserIconView(size_hint_y=0.4, size_hint_x=0.5,
                                                          pos_hint={'y': 0.4, 'x': 0.25})
        self.button_next_screen = Button(text="NEXT", size_hint_y=0.2, size_hint_x=0.5, pos_hint={'y': 0.2, 'x': 0.25},
                                         font_size=sqFdUi.UiConstants.label_font_size,
                                         on_release=lambda btn: self.go_to_next_screen(next_screen=next_screen,
                                                                                       secretary=secretary,
                                                                                       screen_manager=screen_manager,
                                                                                       btn=btn
                                                                                       ))
        self.button_previous_screen = Button(text="PREV", size_hint_y=0.2, size_hint_x=0.5, pos_hint={'y': 0.0, 'x': 0.25},
                                             font_size=sqFdUi.UiConstants.label_font_size,
                                             on_release=lambda btn: self.go_back(previous_screen=previous_screen,
                                                                                 screen_manager=screen_manager))
        self.main_layout.add_widget(self.file_chooser_icon_view)
        self.main_layout.add_widget(self.label_select_sequence_file)
        self.main_layout.add_widget(self.button_next_screen)
        self.main_layout.add_widget(self.button_previous_screen)
        Clock.schedule_once(self.custom_init, 1)

    def custom_init(self, *args):
        self.add_widget(self.main_layout)

    def go_to_next_screen(self, next_screen, secretary, screen_manager, btn):
        secretary.target_file_path = self.file_chooser_icon_view.path + self.file_chooser_icon_view.selection[0]
        screen_manager.current = next_screen

    def go_back (self, previous_screen, screen_manager):
        screen_manager.current = previous_screen
