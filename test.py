from src.classes.file import File
from src.classes.directory import Directory   # tu clase modificada
from src.classes.entry import Entry

# 1. Crear un directorio vacío
root = Directory("root", 'home/asada')

print(root)

print("Inicial:", root.content)      # []
print("is_empty:", root.is_empty)    # True

# 2. Agregar un archivo directamente con add
f1 = File("test.txt", content="hola")
root.add(f1)

print("\nDespués de add(File):", [e for e in root.content])  # ['test.txt']
print("is_empty:", root.is_empty)                                # False
print("Ruta del archivo:", f1.path)                              # root

# 3. Agregar varios elementos con el setter content (append, no replace)
f2 = File("otro.txt")
subdir = Directory("subdir")
root.content = [f2, subdir]     # Usa el setter, que en realidad hace add
print("\nDespués de content = [f2, subdir]:", [e for e in root.content])
# ['test.txt', 'otro.txt', 'subdir']

# 4. Verificar que los subelementos de subdir pueden tener hijos con path correcto
subfile = File("child.txt")
subdir.add(subfile)
print("Subdir contiene:", [e for e in subdir.content])  # ['child.txt']
print("Path de subfile:", subfile.path)                     # root/subdir

# 5. Intentar asignar contenido inválido (no se agrega nada)
root.content = ["cadena", 123]

print("\nDespués de intento inválido:", [e for e in root.content])