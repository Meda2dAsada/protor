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
        self.__json: dict = None
        self.__set_json()
    
    def __set_json(self) -> None:
        """
        Updates the internal configuration by reading the latest content from the JSON file.
        """
        self.__json = self.__read_json()

        if self.__json is None:
            raise ValueError('Json file must be readable.')
    
    def get_json(self) -> dict:
        """
        Retrieves the current configuration from the JSON file.

        return: A list of dictionaries representing the JSON content.
        """
        return self.__json
    
    def __read_json(self) -> dict:
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
        
        current_json = self.get_json()

        if isinstance(current_json, dict):
            return current_json.get(attribute)

    
    def remove_config(self, key: str):
        try:
            self.__json.pop(key)
        except KeyError:
            pass


    def add_config(self, new_config: dict[str, int | str]) -> None:
        """
        Adds a new entry to the JSON configuration file.

        param new_config: A dictionary containing the configuration data for the new entry.
        """
        self.__json.update(new_config)
        #self.__write_json()

    def write_self(self) -> None:
        """
        Writes the current configuration to the JSON file.

        raises PermissionError: If there are permission issues while writing the file.
        raises FileNotFoundError: If the file is not found.
        """
        try:
            with open(self.__path, self.__WRITE) as file:
                json.dump(self.__json, file, indent=4)

        except (PermissionError, FileNotFoundError) as error:
            raise error
