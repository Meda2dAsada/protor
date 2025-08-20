from src.classes.path_checker import PathChecker

class SystemEntry:
    def __init__(self, name: str, path: str = None, entry_type: str = None):
        self.__name: str = None
        self.__path: str = None
        self.__entry_type: str = None
        self.__absolute_path: str | None = None
        self.set_name(name)
        self.set_path(path)
        self.__set_entry_type(entry_type)

    def not_empty(self, string: str):
        return isinstance(string, str) and bool(string.strip())

    def set_name(self, name: str): 
        if self.not_empty(name):
            self.__name = name
        else:
            raise ValueError('Name must not be empty.')

    def set_path(self, path: str):
        if self.not_empty(path):
            self.__path = path.replace('\\', '/')
            self.__absolute_path = f'{self.get_path()}/{self.get_name()}'

    def __set_entry_type(self, entry_type: str):
        if self.not_empty(entry_type):
            self.__entry_type = entry_type

    def get_name(self): return self.__name
    def get_path(self): return self.__path
    def get_entry_type(self): return self.__entry_type
    def get_absolute_path(self): return self.__absolute_path
    def __repr__(self):
        return f'{self.get_absolute_path()}'
    

