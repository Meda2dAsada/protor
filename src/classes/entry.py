from src.classes.path_manager import PathManager

class Entry:
    def __init__(self, name: str, path: str = None, entry_type: str = None):
        self.__name: str = None
        self.__path: str = None
        self.__entry_type: str = None
        self.name: str = name
        self.path: str = path
        self.entry_type: str = entry_type

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if self.not_empty(name, True) and not self.__name:
                self.__name = name.strip()
    
    @property
    def path(self) -> str:
        return self.__path
    
    @path.setter
    def path(self, path: str) -> None:
        if self.not_empty(path):
            self.__path = path.strip().replace('\\', '/')

    @property
    def absolute_path(self) -> str:
        return f'{self.__path}/{self.name}'
    
    @property
    def entry_type(self) -> str:
        return self.__entry_type
    
    @entry_type.setter
    def entry_type(self, entry_type: str) -> None:
        if self.not_empty(entry_type, True) and not self.__entry_type:
            self.__entry_type = entry_type

    def not_empty(self, content: str, strict_alnum: bool = False):
        return PathManager.not_empty(content, strict_alnum)

    def __repr__(self):
        return f'{self.absolute_path or self.name}'

    def __hash__(self):
        return hash(self.name) + hash(self.absolute_path)
    
    def __eq__(self, other: 'Entry'):
        if not isinstance(other, Entry):
            return False
        return self.name == other.name and self.absolute_path == other.absolute_path