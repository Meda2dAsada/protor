
from src.classes.file import File
from src.constants.const import DIRECTORY
from src.classes.system_entry import SystemEntry
from src.classes.system_creator import SystemCreator

class Directory(SystemEntry):

    def __init__(self, name: str, path: str = None, content: list[SystemEntry] = []):
        super().__init__(name, path, DIRECTORY)
        self.__content: list[Directory, File] = []
        self.set_content(content)


    def write_self(self):
        print(self.get_absolute_path(), self.get_entry_type())
        SystemCreator.write_entry(self.get_absolute_path(), None, self.get_entry_type())
        self.write_content()

    def write_content(self):
        for entry in self.get_content():
            if isinstance(entry, (Directory, File)):
                print(entry)
                entry.write_self()

    def add_entry(self, system_entry: SystemEntry):

        if isinstance(system_entry, SystemEntry):
            system_entry.set_path(self.get_absolute_path())
            
            if isinstance(system_entry, Directory):
                for entry in system_entry.get_content():
                    entry.set_path(system_entry.get_absolute_path())

            self.__content.append(system_entry)

    def set_content(self, content: list[SystemEntry]):
        for entry in content:
            self.add_entry(entry)

    def get_content(self): return self.__content
