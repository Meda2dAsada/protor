from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Footer, Header, Button
from textual.containers import Vertical, Center, Middle, Container
from src.components.input_screen import InputScreen
from src.components.alert_screen import AlertScreen
from src.components.warning_screen import WarningScreen
from src.components.editor_screen import EditorScreen
from src.components.new_proyect_screen import NewProyectScreen
from src.components.constants_screen import ContantsScreen

from src.classes.file import File
from src.classes.directory import Directory


# main application class that defines the UI and core logic of the app
class Protor(App):
    # path to the CSS file that styles the application
    CSS_PATH = '../../css/protor.tcss'

    def __init__(self):
        # initializes the UI components and a default file
        super().__init__()

        self.__new_proyect_button = Button('New proyect', id='new_proyect', classes='option_button')
        self.__templates_button = Button('Templates', id='templates', classes='option_button')
        self.__constants_button = Button('Constants', id='constants', classes='option_button')
        self.__configs_button = Button('Configs', id='configs', classes='option_button')        
        self.__exit_button = Button('Exit', id='exit', classes='option_button')
        #self.__file = File('protor.py')

    def __on_input_screen(self, name: str):
        # callback after receiving input from input screen; currently not implemented
        if name is not None:
            pass

    @on(Button.Pressed, '#new_proyect')
    def __on_new_proyect_button(self):
        # opens the input screen when the "new proyect" button is pressed
        self.push_screen(ContantsScreen(), self.__on_input_screen)

    @on(Button.Pressed, '#exit')
    def __on_exit_button(self, event: Button.Pressed):
        # opens the exit confirmation warning screen when the "exit" button is pressed
        self.push_screen(WarningScreen('¿Exit?'), self.__exit)

    def __exit(self, quit_app: bool):
        # exits the application if the user confirms
        if quit_app:
            self.app.exit()

    def compose(self) -> ComposeResult:
        # constructs the layout of the main menu with all buttons and a welcome label
        with Vertical():
            with Container(classes='background'):
                yield Header(True)
                with Center():
                    yield Label('Welcome again to Protor, is good to see you.')
                with Center():
                    with Middle():
                        yield self.__new_proyect_button
                        yield self.__templates_button
                        yield self.__constants_button
                        yield self.__configs_button
                        yield self.__exit_button
        yield Footer()
