
from colorama import just_fix_windows_console, Fore, Back, Style, init
from pathlib import Path
import sys
init(autoreset=True)
Style.RESET_ALL

FOLDER_STYLE = Fore.WHITE + Back.BLACK
ARCHIVES_STYLE = Fore.YELLOW + Back.BLACK
DOCUMENTS_STYLE = Fore.BLUE + Back.BLACK
VIDEOS_STYLE = Fore.MAGENTA + Back.BLACK
MUSIC_STYLE = Fore.CYAN + Back.BLACK
IMAGES_STYLE = Fore.GREEN + Back.BLACK
CODE_STYLE = Fore.BLACK + Back.YELLOW
SOMETHING_STYLE = Fore.RED + Back.BLACK


def cororite_name(clean_name):

    archives = ('zip', 'gztar', 'tar' 'gz', 'rar')
    documents_doc = ('doc', 'docx', 'xlsx', 'pptx', 'txt', 'pdf')
    videos = ("avi", "mp4", "mov", "mkv")
    music = ("mp3", "ogg", "wav", "flac") 
    images = ('jpeg', 'png', 'jpg' 'gif')
    code_file = ('py', 'pyc', 'md', 'cfg', 'ps1', 'bat', 'exe', 'pth', "js", "html", "css", 'scss', 'bmp')

    if clean_name.is_dir():
        return FOLDER_STYLE
    elif clean_name.as_posix().endswith(archives):
        return ARCHIVES_STYLE
    elif clean_name.as_posix().endswith(documents_doc):
        return DOCUMENTS_STYLE
    elif clean_name.as_posix().endswith(videos):
        return VIDEOS_STYLE
    elif clean_name.as_posix().endswith(music):
        return MUSIC_STYLE
    elif clean_name.as_posix().endswith(images):
        return IMAGES_STYLE
    elif clean_name.as_posix().endswith(code_file):
        return CODE_STYLE
    else:
        return SOMETHING_STYLE


def parse_folder_recursive(path):
    
    path_obj = path
    if not path_obj.exists() or not path_obj.is_dir():  # перевірки шляхів та папки
        return

    index_slash_for_start_folder = str(path_obj).rfind('\\')
    name_folder = str(path_obj)[index_slash_for_start_folder+1:]
    print(name_folder)
    def dfs_walk(current_dir, old_margin=''):
        
        for item in current_dir.iterdir():  # iterdir() зчитує вміст поточної папки
            # print(f"{item = }")
            item_string = str(item).strip()
            # print(f"{item_string = }")

            # Обрізаємо шлях до назви файлу чи папки
            path_len_to_folder = len(item_string[:index_slash_for_start_folder+1])

            margin = len(current_dir.as_posix()) - len(old_margin) - 1 - path_len_to_folder
            # print(f"First_margin = {margin}")
            margin_item = ' '
            margin = old_margin + ' ' + margin * margin_item
            # print(f"New_margin = {len(margin)}")
            
            for_repl = current_dir.as_posix()
            clean_name = item.as_posix().replace(f"{for_repl}/", margin)
            
            print(f"{cororite_name(item)}{clean_name}")
            
            if item.is_dir():   # Якщо це папка, пірнаємо на глибину
                dfs_walk(item, margin)

    dfs_walk(path_obj)


def main():

    if len(sys.argv) < 2:
        print('Folder is not found')
        return
    else:
        file_name = Path(sys.argv[1])
    # print(f"{file_name = }")

    parent_folder_path = Path(file_name)
    # print(f"{parent_folder_path = }")

    parse_folder_recursive(parent_folder_path)
    # print(path)

if __name__ == '__main__':
    main()
