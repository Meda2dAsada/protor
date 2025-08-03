from src.classes.file import File
from src.classes.directory import Directory
from src.classes.path_checker import PathChecker
from src.classes.json_reader import JsonReader
from src.classes.system_creator import SystemCreator
from src.constants.const import FILES, DIRECTORIES, TEMPLATES
class ConfigCreator:

    @staticmethod
    def create_config():
        root_path = PathChecker.get_user_path()
        style_file = File('style.tcss')
        files_file = File(f'{FILES}.json', content='{}')
        directories_file = File(f'{DIRECTORIES}.json', content='{}')
        templates_file = File(f'{TEMPLATES}.json', content='{}')

        # files

        # protor styles folder
        styles_dir = Directory('styles')
        styles_dir.add_entry(style_file)

        json_dir = Directory('json')
        json_dir.set_content([files_file, directories_file, templates_file])

        # protor root folder
        protor_dir = Directory('.protor', root_path)
        protor_dir.set_content([styles_dir, json_dir])
        protor_dir.write_self()

        for entry in json_dir.get_content():
            path = entry.get_absolute_path()

            if isinstance(entry, File):
                if not JsonReader.is_valid_json(path, False):
                    SystemCreator.delete_file(path)
                
                entry.write_self()

    @staticmethod
    def __re_write_files():
        pass