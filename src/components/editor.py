from textual.events import Key
from textual.widgets import TextArea
from src.constants.const import INSERTIONS

# custom text editor widget with automatic bracket/quote insertion
class Editor(TextArea):
    def __init__(self, text: str = '', language: str | None = None, id: str = None, classes: str = None):
        super().__init__(text, language=language, tab_behavior='indent', show_line_numbers=True, id=id, classes=classes)

    def _on_key(self, event: Key) -> None:
        # intercepts key events to handle auto-insertion of matching characters
        char = INSERTIONS.get(event.character)
        if char:
            # inserts the matching character and moves the cursor back between the pair
            self.insert(char)
            self.move_cursor_relative(columns=-1)
            event.prevent_default()