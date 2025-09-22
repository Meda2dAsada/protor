import os
from src.constants.const import USERPROFILE

class PathManager:
    @staticmethod
    def is_file(file_name: str):
        return os.path.isfile(file_name)

    @staticmethod
    def not_empty(content: str, strict_alnum: bool = False):
        is_instance = isinstance(content, str) and bool(content.strip())
        return is_instance and content.replace('.', '').isalnum() if strict_alnum else is_instance
    
    @staticmethod
    def is_directory(directory_name: str):
        return os.path.isdir(directory_name)
        
    @staticmethod
    def get_current_directory(): return os.getcwd()

    @staticmethod
    def get_user_path(): return PathManager.get_env(USERPROFILE).replace('\\', '/')
    
    @staticmethod
    def get_env(key: str): return os.environ.get(key)

    @staticmethod
    def join_paths(name: str, *dirs: str):
        return '/'.join([*dirs, name])

    @staticmethod
    def split_paths(path: str):
        return path.replace('\\', '/').split('/')
