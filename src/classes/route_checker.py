import os

class RouteChecker:
    @staticmethod
    def is_valid_file(file: str):
        return os.path.isfile(file)

    @staticmethod
    def is_valid_directory(directory: str): 
        return os.path.isdir(directory)

    @staticmethod
    def get_current_directory(): return os.getcwd()
    