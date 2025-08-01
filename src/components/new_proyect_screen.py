from textual import on
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Label
from textual.containers import Container, Center, Vertical, Middle, ScrollableContainer, Horizontal

class NewProyectScreen(Screen):
    def __init__(self):
        super().__init__()

    
    def compose(self) -> ComposeResult:
        with Vertical():
            with Container(classes='background'):
                yield Header(True)
        yield Footer()

