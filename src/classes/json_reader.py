import json

class JsonReader:
    def __init__(self, path: str) -> None:
        """
        JsonReader is a class for reading and modifying JSON configurations.

        param json_file: The path to the JSON file that will be used for reading and writing.
        This parameter cannot be changed after the object is created for security reasons.
        """

        self.__path: str = path
        self.__READ: str = 'r'
        self.__WRITE: str = 'w'
        self.__config: dict = None
        self.__is_valid: bool = False
        self.__set_config()
    
    def __set_config(self) -> None:
        """
        Updates the internal configuration by reading the latest content from the JSON file.
        """
        self.__config = self.__read_file()

        if self.__config is None:
            raise ValueError('Json file must be readable.')
        
        self.__is_valid = True
    
    def get_config(self) -> dict:
        """
        Retrieves the current configuration from the JSON file.

        return: A list of dictionaries representing the JSON content.
        """
        return self.__config
    
    def __read_file(self) -> dict | None:
        """
        Reads the JSON file and returns its content as a list of dictionaries.

        return: A list of dictionaries representing the content of the JSON file.
        
        raises: None if an error occurs.
        
        PermissionError: If there are permission issues while reading the file.
        raises FileNotFoundError: If the file is not found.
        """

        config = None

        try:
            with open(self.__path, self.__READ) as file:
                config = json.load(file)

        except (PermissionError, FileNotFoundError):
            pass

        return config
    
    def get_attribute(self, attribute: str):
        if self.__is_valid:
            return self.get_config().get(attribute)

    
    def remove_config(self, key: str):
        try:
            self.__config.pop(key)
        except KeyError:
            pass

    def add_config(self, new_config: dict[str, int | str]) -> None:
        """
        Adds a new entry to the JSON configuration file.

        param new_config: A dictionary containing the configuration data for the new entry.
        """
        self.__config.update(new_config)


    def write_self(self) -> None:
        """
        Writes the current configuration to the JSON file.

        raises PermissionError: If there are permission issues while writing the file.
        raises FileNotFoundError: If the file is not found.
        """
        try:
            with open(self.__path, self.__WRITE) as file:
                json.dump(self.__config, file, indent=4)

        except (PermissionError, FileNotFoundError) as error:
            raise error
