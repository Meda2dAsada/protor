
EXTENSIONS: dict[str, str] = {
    'sh': 'bash',
    'bash': 'bash',
    'css': 'css',
    'go': 'go',
    'html': 'html',
    'htm': 'html',
    'java': 'java',
    'js': 'javascript',
    'mjs': 'javascript',
    'cjs': 'javascript',
    'json': 'json',
    'kt': 'kotlin',
    'kts': 'kotlin',
    'md': 'markdown',
    'markdown': 'markdown',
    'py': 'python',
    'pyw': 'python',
    'ipynb': 'python',
    'rs': 'rust',
    're': 'regex',
    'regex': 'regex',
    'sql': 'sql',
    'toml': 'toml',
    'yaml': 'yaml',
    'yml': 'yaml',
}

INSERTIONS: dict[str] = {'(': '()', '{': '{}', '[': '[]',  '<': '<>', '\"': '""', '\'': '\'\''}
FORBIDDEN_CHARS: list[str] = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
MAX_NAME_LENGTH: int = 12
MAX_EXTENSION_LENGTH: int = 9
FILE: str = 'file'
DIRECTORY: str = 'directory'
FILES: str = 'files'
DIRECTORIES: str = 'directories'
TEMPLATES: str = 'templates'
USERPROFILE: str = 'USERPROFILE'
