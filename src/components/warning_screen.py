from textual import on
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Label
from textual.containers import Horizontal, Container, Center

class WarningScreen(ModalScreen):

    BINDINGS = [Binding('ctrl+c', 'cancel_message', 'Cancel')]
    AUTO_FOCUS = '#cancel'

    def __init__(self, message: str):
        super().__init__()
        self.__message = Label(message, id='message')
        self.__accept = Button('Accept', id='accept')
        self.__cancel = Button('Cancel', id='cancel')

    def compose(self):
        with Container():
            with Center():
                yield self.__message

            with Horizontal():
                yield self.__accept
                yield self.__cancel
        yield Footer()

    @on(Button.Pressed, '#accept, #cancel')
    def __on_accept_cancel_button(self, event: Button.Pressed):
        self.dismiss(event.button.id == 'accept')

    def action_cancel_message(self):
        self.dismiss(False)