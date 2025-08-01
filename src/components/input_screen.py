from textual import on
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Input
from textual.containers import Horizontal, Container

from src.constants.const import FORBIDDEN_CHARS

# modal screen to prompt the user for text input, optionally allowing empty values
class InputScreen(ModalScreen):
    # binds ctrl+c to cancel the input screen, with high priority
    BINDINGS = [Binding('ctrl+c', 'cancel_message', 'Cancel', priority=True)]
    # automatically focuses the input field when the screen is shown
    AUTO_FOCUS = '#data_input'

    def __init__(self, message: str, is_optional: bool = False):
        # initializes the input screen with a placeholder message and optionality flag
        super().__init__()
        self.__is_optional = is_optional
        self.__data_input = Input(placeholder=message, id='data_input')
        self.__accept_button = Button('Accept', id='accept', disabled=not self.__is_optional)
        self.__cancel_button = Button('Cancel', id='cancel')

    def compose(self):
        # builds the UI layout: input field, accept/cancel buttons, and footer
        with Container():
            yield self.__data_input
            with Horizontal():
                yield self.__accept_button
                yield self.__cancel_button
        yield Footer()

    @on(Input.Changed, '#data_input')
    @on(Input.Submitted, '#data_input')
    def set_input(self, event: Input.Changed | Input.Submitted):
        # triggered when the input changes or is submitted
        data = event.value.strip()

        if not self.__is_optional:
            if data:
                # check for forbidden characters; disable button if any are found
                disabled = False
                for char in [*data]:
                    if char in FORBIDDEN_CHARS:
                        disabled = True
                        break
                self.__accept_button.disabled = disabled
            else:
                # disable the accept button if input is empty and not optional
                self.__accept_button.disabled = True

    @on(Button.Pressed, '#accept, #cancel')
    def __on_accept_cancel_button(self, event: Button.Pressed):
        # dismisses the screen with the input value or None depending on which button was pressed
        self.dismiss(self.__data_input.value if event.button.id == 'accept' else None)

    def action_cancel_message(self):
        # action triggered by ctrl+c to cancel input and dismiss the screen
        self.dismiss()
    