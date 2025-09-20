#import sys
#sys.setrecursionlimit(n)
#COMMENT: protor(proyect - creator)
from src.components.protor import Protor
from src.classes.directory import Directory
from src.classes.json_reader import JsonReader
from src.classes.file import File
from src.classes.entry_creator import EntryCreator



# # Crear directorio raíz
# folder = Directory('folder', r'C:\Users\ASADA\Desktop\py_projects\protor')

# files = [File(f'file{i}.txt', content=f'Contenido del archivo {i}') for i in range(1, 6)]

# r = r'C:\Users\ASADA\Desktop\py_projects\protor\json\constants.json'

Protor().run()