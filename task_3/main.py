import sys
from pathlib import Path
from folder_tree_recursion import draw_folder_tree


def main():
    try:
        path = sys.argv[1]
        draw_folder_tree(Path(path))
    except IndexError:
        print("You forgot to enter the path")


if __name__ == "__main__":
    main()
