import os

class EntryCreator:
    @staticmethod
    def write_directory(directory: str):
        try:
            os.makedirs(directory)

        except (PermissionError, FileExistsError):
            pass

    @staticmethod
    def write_file(entry: str, content: str | None):
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
