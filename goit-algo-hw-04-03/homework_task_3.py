
from colorama import just_fix_windows_console, Fore, Back, Style, init
from pathlib import Path
import sys
init(autoreset=True)
Style.RESET_ALL




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
            # old_margin = ' ' * len(old_margin)
            margin = old_margin + ' ' + margin * margin_item
            
            for_repl = current_dir.as_posix()
            clean_path = item.as_posix().replace(f"{for_repl}/", margin)
            print(clean_path)
            
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
