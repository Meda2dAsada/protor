from src.classes.file import File
from src.classes.directory import Directory
from src.classes.path_checker import PathChecker
from src.classes.json_reader import JsonReader
from src.classes.system_creator import SystemCreator
from src.constants.const import FILES, DIRECTORIES, TEMPLATES


class ConfigCreator:
    PROTOR_DIR = '.protor'
    JSON_DIR = 'json'
    STYLES_DIR = 'styles'


    @staticmethod
    def working_dir(protor_path: bool):
        return PathChecker.get_user_path() if not protor_path else f'{PathChecker.get_user_path()}/{ConfigCreator.PROTOR_DIR}'

    @staticmethod
    def style_file():
        return f'{ConfigCreator.working_dir(True)}/{ConfigCreator.STYLES_DIR}/style.tcss'


    @staticmethod
    def json_dir():
        return f'{ConfigCreator.working_dir(True)}/{ConfigCreator.JSON_DIR}'


    @staticmethod
    def create_config():
        root_path = ConfigCreator.working_dir(False)
        style_file = File('style.tcss')
                          
        files_file = File(f'{FILES}.json', content='{}')
        directories_file = File(f'{DIRECTORIES}.json', content='{}')
        templates_file = File(f'{TEMPLATES}.json', content='{}')

        # files

        # protor styles folder
        styles_dir = Directory(ConfigCreator.STYLES_DIR)
        styles_dir.add_entry(style_file)

        json_dir = Directory(ConfigCreator.JSON_DIR)
        json_dir.set_content([files_file, directories_file, templates_file])

        # protor root folder
        protor_dir = Directory(ConfigCreator.PROTOR_DIR, root_path)
        protor_dir.set_content([styles_dir, json_dir])
        protor_dir.write_self()

        ConfigCreator.__re_write_json(protor_dir.get_content())

    @staticmethod
    def __re_write_json(directories: list[Directory]):

        for directory in directories:
            for entry in directory.get_content():
                path = entry.get_absolute_path()

                if isinstance(entry, File):
                    if not JsonReader.is_valid_json(path, False) or entry.get_is_empty():
                        SystemCreator.delete_file(path)
                    entry.write_self()