from textual.widgets import Input, Label, Button, Static
from textual.containers import Vertical, Horizontal
from textual.app import ComposeResult

class FileDisplay(Static):
    def __init__(self, key: str, values: dict):
        super().__init__()
