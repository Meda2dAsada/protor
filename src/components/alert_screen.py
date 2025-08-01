from textual import on
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Label
from textual.containers import Horizontal, Container, Center


# defines a modal screen that displays an alert message with a single "accept" button
class AlertScreen(ModalScreen):

    # defines a keyboard shortcut: ctrl+a triggers the "accept_message" action
    BINDINGS = [Binding('ctrl+a', 'accept_message', 'Accept')]

    # sets the initial focus to the button with id 'accept'
    AUTO_FOCUS = '#accept'

    def __init__(self, message: str):
        # initializes the modal screen with a message label and an accept button
        super().__init__()
        self.__message = Label(message, id='message')
        self.__accept = Button('Accept', id='accept')
    
    def compose(self):
        # defines the layout of the screen with the message centered
        # and the accept button below it
        with Container():
            with Center():
                yield self.__message

            with Horizontal():
                yield self.__accept
        yield Footer()

    # handles the button press event and dismisses the modal with a True result
    @on(Button.Pressed, '#accept')
    def __on_accept_button(self, event: Button.Pressed):
        self.dismiss(True)

    # handles the keyboard binding (ctrl+a) and dismisses the modal
    def action_accept_message(self):
        self.dismiss(True)
