from textual import on
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Header
from textual.containers import Container, Center, Vertical, Middle

from src.components.editor import Editor
from src.components.warning_screen import WarningScreen

from src.classes.file import File
from src.constants.const import MAX_NAME_LENGTH, MAX_EXTENSION_LENGTH, EXTENSIONS


# defines a screen for editing a file with save and leave functionality
class EditorScreen(Screen):
    # binds keyboard shortcuts: ctrl+s to save, ctrl+l to leave
    BINDINGS = [Binding('ctrl+s', 'save', 'Save'), Binding('ctrl+l', 'leave', 'Leave')]

    def __init__(self, file: File):
        # initializes the screen with the file content and its syntax highlighting
        super().__init__()
        self.__file = file
        self.__is_saved = True
        self.__editor = Editor(
            self.__file.get_content(),
            EXTENSIONS.get(self.__file.get_extension()),
            'editor'
        )
        self.__set_title()

    def compose(self) -> ComposeResult:
        # creates the layout with header, centered editor, and footer
        with Vertical():
            with Container(classes='background'):
                yield Header(True)
                with Center():
                    with Middle():
                        yield self.__editor
        yield Footer()

    def __get_title_format(self):
        # returns a formatted title based on file name and extension, truncating if needed
        name, extension = self.__file.get_split_name()
        if len(name) > MAX_NAME_LENGTH:
            name = f'[{name[:MAX_NAME_LENGTH]}]'
        if len(extension) > MAX_EXTENSION_LENGTH:
            extension = f'[{extension[:MAX_EXTENSION_LENGTH]}]'
        return f'{name}.{extension}'

    def __set_title(self):
        # updates the screen title to show file name and save status
        self.title = f'{self.__get_title_format()} @ {'Saved  ' if self.__is_saved else 'Unsaved'}'

    # listens to changes in the editor to update save status and title
    @on(Editor.Changed, '#editor')
    def __on_editor(self, event: Editor.Changed):
        if self.__file.get_content() != self.__editor.text:
            self.__is_saved = False
        else:
            self.__is_saved = True
        self.__set_title()

    # saves the editor content to the file and updates the title
    def action_save(self):
        self.__is_saved = True
        self.__file.set_content(self.__editor.text)
        self.__set_title()

    # attempts to leave the editor; shows a warning if there are unsaved changes
    def action_leave(self):
        if not self.__is_saved:
            self.app.push_screen(WarningScreen('¿Leave editing? Changes are unsaved'), self.__leave_unsaved)
        else:
            self.dismiss()

    # called after the warning screen; closes the editor if the user confirms
    def __leave_unsaved(self, quit_warning: bool):
        if quit_warning:
            self.dismiss()
