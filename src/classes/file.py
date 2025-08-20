from src.constants.const import FILE
from src.classes.system_entry import SystemEntry
from src.classes.system_creator import SystemCreator

class File(SystemEntry):

    def __init__(self, name: str, path: str = None, content: str | None = None):
        super().__init__(name, path, FILE)
        self.__content: str = None
        self.__split_name: tuple = None
        self.__file_name: str = None
        self.__extension: str = None
        self.__is_empty: bool = None
        
        self.set_content(content)
        self.__set_split_name(name)

    def __set_split_name(self, name: str):
        self.__split_name = SystemCreator.trim_file(name)
        self.__file_name, self.__extension = self.__split_name

    def write_self(self):
        SystemCreator.write_entry(self.get_absolute_path(), self.get_content(), self.get_entry_type())

    def set_content(self, content: str):
        if self.not_empty(content):
            self.__content = content
        else:
            self.__content = ''
        
        self.__set_is_empty(bool(self.__content))

    def __set_is_empty(self, is_empty: bool):
        if isinstance(is_empty, bool):
            self.__is_empty = is_empty

    def get_is_empty(self): return self.__is_empty
    def get_content(self): return self.__content
    def get_split_name(self): return self.__split_name
    def get_extension(self): return self.__extension
    def get_file_name(self): return self.__file_name

