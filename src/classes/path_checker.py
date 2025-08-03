import os
from src.constants.const import USERPROFILE

class PathChecker:
    @staticmethod
    def is_file(file: str):
        return os.path.isfile(file)

    @staticmethod
    def is_directory(directory: str):
        return os.path.isdir(directory)
        
    @staticmethod
    def get_current_directory(): return os.getcwd()

    @staticmethod
    def get_user_path(): return PathChecker.get_env(USERPROFILE).replace('\\', '/')
    

    @staticmethod
    def get_env(key: str): return os.environ.get(key)
