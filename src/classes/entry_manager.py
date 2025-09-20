from src.classes.json_reader import JsonReader
from src.classes.path_manager import PathManager
from src.classes.config_creator import ConfigCreator
    

class EntryManager(JsonReader):
    """
    EntryManager is responsible for reading and flattening a hierarchical JSON
    configuration of directories and files.

    It inherits from JsonReader to access and parse the configuration file,
    and provides a method (`flattened_key`) that returns a normalized dictionary
    of all global/local directories and files starting from a given root key.
    """

    def __init__(self):
        """
        Build the absolute path to the JSON configuration file and
        initialize the parent JsonReader with that path.
        """
        dirs_path = PathManager.join_paths(
            ConfigCreator.DIRECTORIES_FILE,
            ConfigCreator.get_json_dir()
        )
        super().__init__(dirs_path)

    def __walk(
        self,
        key: str,
        prefix: list[str],
        dirs_global: set[tuple],
        dirs_local: set[tuple],
        files_global: set[tuple],
        files_local: set[tuple],
        stack: list[str]
    ):
        # Stop if the key is not defined in the configuration
        if key not in self.get_config():
            return

        # Detect circular references within the current branch
        if key in stack:
            return

        stack.append(key)  # Mark current key as visited
        node = self.get_config()[key]
        content = node["content"]

        # ---- Global files ----
        for path in content.get("files", {}).get("global", []):
            files_global.add(tuple(prefix + path))

        # ---- Local files ----
        for path in content.get("files", {}).get("local", []):
            last = path[-1]
            # Handle inline objects with {"name":..., "content":...}
            if isinstance(last, dict) and "name" in last and "content" in last:
                last_tuple = (last["name"], last["content"])
                full_path = prefix + path[:-1] + [last_tuple]
            else:
                full_path = prefix + path
            files_local.add(tuple(full_path))

        # ---- Global directories ----
        for path in content.get("directories", {}).get("global", []):
            next_key = path[-1]
            if next_key in stack:
                continue  # Skip cycles

            full_path = prefix + path
            dirs_global.add(tuple(full_path))

            # Recurse if this directory name is also a key in the config
            if next_key in self.get_config():
                self.__walk(next_key, full_path,
                            dirs_global, dirs_local,
                            files_global, files_local,
                            stack)

        # ---- Local directories ----
        for path in content.get("directories", {}).get("local", []):
            last = path[-1]
            # Handle inline objects that define a directory name
            if isinstance(last, dict) and "name" in last:
                last_name = last["name"]
                full_path = prefix + path[:-1] + [last_name]
            else:
                last_name = last
                full_path = prefix + path

            if last_name in stack:
                continue  # Skip cycles
            dirs_local.add(tuple(full_path))

            if last_name in self.get_config():
                self.__walk(last_name, full_path,
                            dirs_global, dirs_local,
                            files_global, files_local,
                            stack)

        stack.pop()  # Backtrack when leaving this branch

    def flattened_key(self, key: str) -> dict:
        dirs_global, dirs_local = set(), set()
        files_global, files_local = set(), set()

        # Start the recursive walk with an empty stack
        self.__walk(key, [], dirs_global, dirs_local,
                    files_global, files_local, [])

        node = self.get_config().get(key)
        if not node:
            return {}

        return {
            "name": node["name"],
            "content": {
                "directories": {
                    "global": [list(dir_global) for dir_global in sorted(dirs_global, key=len)],
                    "local": [list(dir_local) for dir_local in sorted(dirs_local, key=len)],
                },
                "files": {
                    "global": [list(file_global) for file_global in sorted(files_global, key=len)],
                    "local": [list(file_local) for file_local in sorted(files_local, key=len)],
                },
            },
        }
