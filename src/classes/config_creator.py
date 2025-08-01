from src.classes.file import File
from src.classes.directory import Directory
from src.classes.route_checker import RouteChecker
from src.constants.const import FILES, DIRECTORIES, TEMPLATES


class ConfigCreator:
    @staticmethod
    def create_config():
        root_path = RouteChecker.get_user_path()
        
        # Construcción de archivos
        style_file = File('style.tcss')
        files_file = File(f'{FILES}.json', content='{}')
        directories_file = File(f'{DIRECTORIES}.json', content='{}')
        templates_file = File(f'{TEMPLATES}.json', content='{}')

        # Carpetas internas
        styles_dir = Directory('styles')
        styles_dir.add_entry(style_file)

        json_dir = Directory('json')
        json_dir.set_content([files_file, directories_file, templates_file])

        # Carpeta raíz .protor
        protor_dir = Directory('.protor', root_path)
        protor_dir.set_content([styles_dir, json_dir])

        # Intentar crear toda la estructura
        if not protor_dir.write_self():
            for entry in protor_dir.get_content():
                entry.write_self()
