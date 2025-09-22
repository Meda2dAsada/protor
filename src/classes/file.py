from src.classes.entry import Entry
from src.constants.const import FILE
from src.classes.entry_creator import EntryCreator

class File(Entry):
    def __init__(self, name: str, path: str = None, content: str | None = None):
        super().__init__(name, path, FILE)
        self.__split_name: tuple[str, str] = None
        self.__file_name: str = None
        self.__extension: str = None
        self.__content: str = None

        self.split_name: tuple[str, str] = name
        self.content: str = content

    @property
    def split_name(self) -> tuple[str, str]:
        return self.__split_name
    
    @split_name.setter
    def split_name(self, split_name: str) -> None:
        if self.not_empty(split_name) and not self.split_name:
            self.__split_name = EntryCreator.trim_extension(split_name)
            self.__file_name, self.__extension = self.__split_name

    @property
    def file_name(self) -> str:
        return self.__file_name
    
    @property
    def extension(self) -> str:
        return self.__extension

    @property
    def content(self) -> str:
        return self.__content
    
    @content.setter
    def content(self, content: str) -> None:
        self.__content = content if self.not_empty(content) else ''

    @property
    def is_empty(self) -> bool:
        return not bool(self.__content)

    def write_self(self):
        EntryCreator.write_entry(self.absolute_path, self.content, self.entry_type)

    def __hash__(self):
        return super().__hash__() + hash(self.content)

    def __eq__(self, other: 'File'):
        if not isinstance(other, File):
            return False
        return super().__eq__(other) and self.content == other.content
