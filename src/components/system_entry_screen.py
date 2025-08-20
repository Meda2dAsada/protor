from textual import on
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button
from textual.containers import Container, Vertical, ScrollableContainer

from src.classes.json_reader import JsonReader
from src.components.file_display import FileDisplay
from src.classes.config_creator import ConfigCreator
from src.components.directory_display import DirectoryDisplay


class SystemEntryScreen(JsonReader, Screen):
    BINDINGS = [Binding('ctrl+b', 'go_back', 'Go back')]

    def __init__(self, for_directories: bool):
        self.__for_directories = for_directories
        self.__back_button = Button('Go back', id='back', classes='option_button')
        
        json_path = f'{ConfigCreator.get_json_dir()}/{ConfigCreator.DIRECTORIES_FILE if self.__for_directories else ConfigCreator.FILES_FILE}'
        print(json_path)
        JsonReader.__init__(self, json_path)
        Screen.__init__(self)

    def compose(self) -> ComposeResult:
        with Vertical():
            with Container(classes='background'):
                yield Header(show_clock=True)

                with ScrollableContainer(id='scroll'):
                    for k, v in self.get_config().items():
                        
                        if self.__for_directories:
                            yield DirectoryDisplay(k, v)
                        else:
                            yield FileDisplay(k, v)
                        

            yield self.__back_button
        yield Footer()

    @on(Button.Pressed, '#back')
    def on_back_button(self, event: Button.Pressed):
        self.app.pop_screen()

    def action_go_back(self):
        self.app.pop_screen()
