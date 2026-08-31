
from colorama import just_fix_windows_console, Fore, Back, Style, init
from pathlib import Path
import sys
init(autoreset=True)
Style.RESET_ALL

FOLDER_STYLE = Fore.WHITE + Back.BLACK
ARCHIVES_STYLE = Fore.YELLOW + Back.BLACK
DOCUMENTS_STYLE = Fore.BLUE + Back.BLACK
DOCUMENTS_TXT_STYLE = Fore.MAGENTA + Back.BLACK
DOCUMENTS_PDF_STYLE = Fore.CYAN + Back.BLACK
IMAGES_STYLE = Fore.GREEN + Back.BLACK
ERROR_STYLE = Fore.RED + Back.BLACK


def cororite_name(clean_name):

    archives = ('zip', 'gztar', 'tar')
    documents_doc = ('doc', 'docx', 'xlsx', 'pptx')
    documents_txt = ('txt')
    documents_pdf = ('pdf')
    images = ('jpeg', 'png', 'jpg')

    if clean_name.endswith(archives):
        print(ARCHIVES_STYLE + clean_name)
    elif clean_name.endswith(documents_doc):
        print(DOCUMENTS_STYLE + clean_name)
    elif clean_name.endswith(documents_txt):
        print(DOCUMENTS_TXT_STYLE + clean_name)
    elif clean_name.endswith(documents_pdf):
        print(DOCUMENTS_PDF_STYLE + clean_name)
    elif clean_name.endswith(images):
        print(IMAGES_STYLE + clean_name)
    else:
        print(FOLDER_STYLE + clean_name)


def parse_folder_recursive(path):
    
    path_obj = path
    if not path_obj.exists() or not path_obj.is_dir():  # перевірки шляхів та папки
        return
    
    print(path_obj)
    def dfs_walk(current_dir, index_slash=0, old_margin=''):
        
        for item in current_dir.iterdir():  # iterdir() зчитує вміст поточної папки
            # print(f"{item}", type(item))
            item_string = str(item)
            # print(f"{item_string = }")

            index_slash = item_string.find('\\', index_slash+1)     # знаходимо індекси слешів для обрізки шляху
            # print(f"{index_slash = }", type(index_slash))

            # Обрізаємо шлях до назви файлу чи папки
            margin = len(current_dir.as_posix()) - len(old_margin) - 1
            margin_item = ' '
            margin = old_margin + ' ' + margin * margin_item
            
            for_repl = current_dir.as_posix()
            clean_name = item.as_posix().replace(f"{for_repl}/", margin)
            cororite_name(clean_name)
            
            if item.is_dir():   # Якщо це папка, пірнаємо на глибину
                dfs_walk(item, index_slash, margin)

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
