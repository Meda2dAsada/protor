from textual.widgets import Input, Label, Button
from textual.containers import Vertical, Horizontal, Container
from textual.app import ComposeResult

class DirectoryDisplay(Container):
    def __init__(self, key: str, values: dict):
        super().__init__(classes='display')
        self.__key = key
        self.__values = values
        self.__key_input = Input(value=key, classes='key_input')
        self.__edit_button = Button('Edit', classes='edit_button')

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield self.__key_input
            yield self.__edit_button

        for subkey, subval in self.__values.items():
            yield Label(f'{subkey}: {subval}', classes='subitem_label')
