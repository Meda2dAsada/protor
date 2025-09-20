import os
from src.constants.const import DIRECTORY, FILE

class EntryCreator:
    @staticmethod
    def trim_file(file_name: str):
        if '.' not in file_name:
            return file_name, ''

        split = file_name.split('.')
        extension = split.pop()
        
        return '.'.join(split), extension
    
    @staticmethod
    def reduce_strings(files: tuple[str], sizes: tuple[int]):
        return [f'[{file[:size]}\u2026]' if len(file) > size else file for file, size, in zip(files, sizes)]

    @staticmethod
    def join_file(file_name: list[str] | tuple[str]):
        start, end = file_name
        if end:
            return '.'.join(file_name)
        
        return ''.join(start)

    @staticmethod
    def write_entry(entry: str, content: str | None, entry_type: str):
        if entry_type == DIRECTORY:
            EntryCreator.__write_directory(entry)
        elif entry_type == FILE:
            EntryCreator.__write_file(entry, content)

    @staticmethod
    def __write_directory(directory: str):
        try:
            os.makedirs(directory)

        except (PermissionError, FileExistsError):
            pass

    @staticmethod
    def __write_file(entry: str, content: str | None):
        if entry:
            try: 
                with open(entry, 'x', encoding='utf-8') as file:
                    file.write(content or '')

            except (PermissionError, FileExistsError):
                pass

    @staticmethod
    def delete_file(path: str):
        try:
            os.remove(path)

        except FileNotFoundError:
            pass
        except PermissionError as error:
            raise error   
