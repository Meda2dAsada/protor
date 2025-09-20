import json

class JsonReader(dict):
    READ: str = 'r'
    WRITE: str = 'w'

    def __init__(self, path: str) -> None:
        """
        JsonReader is a class for reading and modifying JSON configurations that already exist.

        param path: The path to the JSON file that will be used for reading and writing.
        """
        self.__path: str = path
        config = self.__read_file()

        if config is None:
            raise ValueError('Json file must be readable.')
        
        super().__init__(config)

    def __read_file(self) -> dict | None:
        """
        Reads the JSON file and returns its content as a dict.
        """
        try:
            return JsonReader.is_valid_json(self.__path)
        except PermissionError as error:
            raise error

    def get_config(self) -> dict:
        """
        Retrieves the current configuration as a dictionary.
        """
        return dict(self)

    def remove_config(self, key: str) -> None:
        """
        Removes a key from the configuration safely.
        """
        self.pop(key, None)

    def add_config(self, new_config: dict[str, int | str]) -> None:
        """
        Adds a new entry to the JSON configuration.
        """
        self.update(new_config)

    def write_self(self) -> None:
        """
        Writes the current configuration to the JSON file.
        """
        try:
            with open(self.__path, self.WRITE) as file:
                json.dump(self, file, indent=4)
        except PermissionError as error:
            raise error

    @staticmethod
    def is_valid_json(path: str, return_data: bool = True) -> dict | bool | None:
        """
        Tries to read a JSON file.

        Returns:
            dict: Parsed JSON data if successful and return_data is True.
            bool: True if valid JSON (when return_data is False), otherwise False.
            None: If an error occurs and return_data is True.
        """
        try:
            with open(path, JsonReader.READ) as file:
                data = json.load(file)
                return data if return_data else True

        except (FileNotFoundError, json.JSONDecodeError):
            return None if return_data else False
        except PermissionError as error:
            raise error
