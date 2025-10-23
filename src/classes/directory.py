
from src.classes.file import File
from src.classes.entry import Entry
from src.constants.const import DIRECTORY
from src.classes.entry_creator import EntryCreator

class Directory(Entry):
    def __init__(self, name: str, path: str = None, content: list[Entry] = None):
        super().__init__(name, path, DIRECTORY)
        self.__content: list[Entry] = None
        self.content: list[Entry] = content

    @property
    def content(self) -> list[Entry]:
        return self.__content

    @content.setter
    def content(self, content: list[Entry]) -> None:
        if self.__content is None:
            self.__content = []

        if isinstance(content, list):
            for entry in content:
                self.add(entry)

    @property
    def is_empty(self) -> bool:
        return len(self.__content) == 0

    def add(self, entry: Entry):
        if entry == self:
            raise TypeError(f"Can't add {self.absolute_path}, because is the same object." )
        
        if isinstance(entry, (Directory, File)):
            entry.path = self.absolute_path
            if isinstance(entry, Directory):
                entry.__update_content_paths()

            self.__content.append(entry)

    def __update_content_paths(self):
        for entry in self.content:
            entry.path = self.absolute_path
            if isinstance(entry, Directory):
                entry.__update_content_paths()

    def extends(self, entries: list[Entry]):
        for entry in entries:
            self.add(entry)

    def write_self(self):
        EntryCreator.write_directory(self.absolute_path)
        self.write_content()

    def write_content(self):
        for entry in self.content:
            if isinstance(entry, (Directory, File)):
                entry.write_self()

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other: 'Directory'):
        if not isinstance(other, Directory):
            return False
        return super().__eq__(other) and self.content == other.content

