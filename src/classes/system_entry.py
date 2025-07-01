from src.classes.route_checker import RouteChecker

class SystemEntry:

    def __init__(self, name: str, path: str = None, entry_type: str = None):
        self.__name: str = None
        self.__path: str = None
        self.__entry_type: str = None

        self.set_name(name)
        self.set_path(path)
        self.__set_entry_type(entry_type)


    def __set_entry_type(self, entry_type: str):
        if self.validate_strings(entry_type):
            self.__entry_type = entry_type

    def get_entry_type(self): return self.__entry_type
    
    def validate_strings(self, string: str):
        return isinstance(string, str) and bool(string.strip())

    def set_name(self, name: str): 
        if self.validate_strings(name):
            self.__name = name
        else:
            raise ValueError('Name must not be empty.')

    def set_path(self, path: str): 
        if self.validate_strings(path):
            self.__path = path.replace('\\', '/')


    def get_name(self): return self.__name
    def get_path(self): return self.__path

    def get_absolute_path(self):
        path = self.get_path()
        if self.validate_strings(path) and RouteChecker.is_valid_directory(path):
            return f'{path}/{self.get_name()}'
        
    def __repr__(self):
        return f'{self.get_path()}/{self.get_name()}'