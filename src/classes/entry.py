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
        name = name.strip() # delete white spaces on the start & end in name
        if self.not_empty(name) and self.__name is None:
                self.__name = name
        else:
            raise ValueError('Name must not be empty.')
        
    @property
    def path(self) -> str:
        return self.__path
    
    @path.setter
    def path(self, path: str) -> None:
        if self.not_empty(path):
            self.__path = path.strip().replace('\\', '/')

    @property
    def absolute_path(self) -> str:
        return PathManager.join(self.name, self.path) if self.path else PathManager.join(self.name)
    
    @property
    def entry_type(self) -> str:
        return self.__entry_type
    
    @entry_type.setter
    def entry_type(self, entry_type: str) -> None:
        if self.not_empty(entry_type) and self.__entry_type is None:
            self.__entry_type = entry_type

    def not_empty(self, content: str):
        return PathManager.not_empty(content)

    def __repr__(self):
        return self.absolute_path

    def __hash__(self):
        return hash(self.name) + hash(self.absolute_path)
    
    def __eq__(self, other: 'Entry'):
        if not isinstance(other, Entry):
            return False
        return self.absolute_path == other.absolute_path