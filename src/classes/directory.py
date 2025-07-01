
from src.classes.file import File
from src.constants.const import DIRECTORY
from src.classes.system_entry import SystemEntry
from src.classes.system_creator import SystemCreator

class Directory(SystemEntry):

    def __init__(self, name: str, path: str = None, content: list['Directory', File] = []):
        super().__init__(name, path, DIRECTORY)
        self.__content: list[Directory, File] = []
        self.set_content(content)

    def __validate_system_entry(self, system_entry: SystemEntry):
        return isinstance(system_entry, (Directory, File)) and system_entry.get_absolute_path() is None

    def write_self(self):
        SystemCreator.write_entry(self.get_absolute_path(), None, self.get_entry_type())
        self.write_content()

    def write_content(self):
        path = self.get_absolute_path()

        for entry in self.get_content():
            if isinstance(entry, (Directory, File)):
                entry.set_path(path if path else self.get_name())
                print(entry.get_name())
                entry.write_self()

    def add_entry(self, system_entry: SystemEntry):

        if self.__validate_system_entry(system_entry):
            self.__content.append(system_entry)
    

    def set_content(self, content: list['Directory', File]):
        for entry in content:
            self.add_entry(entry)

    def get_content(self): return self.__content
