from pathlib import Path
from colorama import Fore


# return tree of folders and files
def draw_folder_tree(path: Path, level: int = 0):
    if not path.exists() or not path.is_dir():
        print(Fore.RED + "Passed path is not a directory or does not exist")
        return None

    indent = " " * (level * 2)
    print(indent + Fore.BLUE + path.name + "/")

    for item in path.iterdir():
        if item.is_dir():
            draw_folder_tree(item, level + 1)  # Execute recursion for sub directories
        else:
            print(indent + "  " + Fore.GREEN + item.name)  # Green color for files
