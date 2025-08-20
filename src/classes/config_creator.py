from src.classes.file import File
from src.classes.directory import Directory
from src.classes.json_reader import JsonReader
from src.classes.path_checker import PathChecker
from src.classes.system_creator import SystemCreator

class ConfigCreator:
    PROTOR_DIR = '.protor'
    JSON_DIR = 'json'
    STYLE_DIR = 'style'
    FILES_FILE: str = 'files.json'
    DIRECTORIES_FILE: str = 'directories.json'
    TEMPLATES_FILE: str = 'templates.json'
    PROTOR_FILE: str = 'protor.json'
    STYLE_FILE: str = 'style.tcss'


    @staticmethod
    def working_dir(protor_path: bool):
        return PathChecker.get_user_path() if not protor_path else f'{PathChecker.get_user_path()}/{ConfigCreator.PROTOR_DIR}'

    @staticmethod
    def get_style_file():
        return ConfigCreator.join_paths(
            ConfigCreator.working_dir(True),
            ConfigCreator.STYLE_FILE
        )

    @staticmethod
    def get_json_dir():
        return ConfigCreator.join_paths(
            ConfigCreator.working_dir(True),
            ConfigCreator.JSON_DIR
        )
    
    @staticmethod
    def join_paths(directory: str, entry: str):
        return '/'.join([directory, entry])


    @staticmethod
    def create_config():
        root_path = ConfigCreator.working_dir(False)
        # config files

        style_file = File(ConfigCreator.STYLE_FILE)
        files_file = File(ConfigCreator.FILES_FILE, content='{}')
        directories_file = File(ConfigCreator.DIRECTORIES_FILE, content='{}')
        templates_file = File(ConfigCreator.TEMPLATES_FILE, content='{}')
        protor_file = File(ConfigCreator.PROTOR_FILE, content='{}')

        # protor styles folder
        styles_dir = Directory(ConfigCreator.STYLE_DIR)
        styles_dir.add_entry(style_file)

        json_dir = Directory(ConfigCreator.JSON_DIR)
        json_dir.set_content([files_file, directories_file, templates_file])

        # protor root folder
        protor_dir = Directory(ConfigCreator.PROTOR_DIR, root_path)
        protor_dir.set_content([styles_dir, json_dir])
        protor_dir.write_self()
        ConfigCreator.__re_write_config(protor_dir.get_content())
    
    @staticmethod
    def __re_write_config(directories: list[Directory]):

        for directory in directories:
            for entry in directory.get_content():
                path = entry.get_absolute_path()

                if isinstance(entry, File):
                    if not JsonReader.is_valid_json(path, False) or entry.get_is_empty():
                        SystemCreator.delete_file(path)
                    entry.write_self()