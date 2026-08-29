
from colorama import colorama_text, just_fix_windows_console
from pathlib import Path
import sys


if len(sys.argv) < 0:
    user_input = ''
else:
    user_input = sys.argv[1]
parent_folder_path = Path(user_input)
# print(path)


def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is a folder - {element.name}")
        if element.is_file():
            print(f"Parsle folder: This is a file - {element.name}")


def main():
    parse_folder(parent_folder_path)


if __name__ == '__main__':
    main()
