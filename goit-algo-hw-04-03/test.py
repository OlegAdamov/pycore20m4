from colorama import just_fix_windows_console, Fore, Back, Style, init
from pathlib import Path
import sys
init(autoreset=True)
Style.RESET_ALL

FOLDER_STYLE = Fore.WHITE + Back.RED
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

    if clean_name.is_dir():
        print(FOLDER_STYLE + clean_name)
    elif clean_name.as_posix().endswith(archives):
        print(ARCHIVES_STYLE + clean_name.as_posix())
    elif clean_name.as_posix().endswith(documents_doc):
        print(DOCUMENTS_STYLE + clean_name.as_posix())
    elif clean_name.as_posix().endswith(documents_txt):
        print(DOCUMENTS_TXT_STYLE + clean_name.as_posix())
    elif clean_name.as_posix().endswith(documents_pdf):
        print(DOCUMENTS_PDF_STYLE + clean_name.as_posix())
    elif clean_name.as_posix().endswith(images):
        print(IMAGES_STYLE + clean_name.as_posix())
    else:
        print(ERROR_STYLE + "I don't know what is it")

cororite_name(Path(f"Hello, I am a clean_name"))
cororite_name(Path(f"Hello, I am a clean_name.zip"))
cororite_name(Path(f"Hello, I am a clean_name.pdf"))
cororite_name(Path(f"Hello, I am a clean_name.txt"))
cororite_name(Path(f"Hello, I am a clean_name.doc"))
cororite_name(Path(f"Hello, I am a clean_name.jpg"))






