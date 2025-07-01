#COMMENT: protor(proyect - creator)
import os
from src.constants.const import DIRECTORY, FILE

class SystemCreator:

    @staticmethod
    def trim_file(name: str):

        if not '.' in name:
            return name, ''
        
        split = name.split('.')
        extension = split.pop()
        
        return '.'.join(split), extension


    @staticmethod
    def write_entry(system_entry: str, content: str, entry_type: str):

        if entry_type == DIRECTORY:
            SystemCreator.__write_directory(system_entry)
        elif entry_type == FILE:
            SystemCreator.__write_file(system_entry, content)
    
    @staticmethod    
    def __write_directory(directory: str):
        try:
            os.makedirs(directory)

        except (PermissionError, FileExistsError):
            pass

    @staticmethod
    def __write_file(entry: str, content: str):
        if entry:
            try: 
                with open(entry, 'x', encoding='utf-8') as file:
                    file.write(content or '')

            except (PermissionError, FileExistsError):
                pass
