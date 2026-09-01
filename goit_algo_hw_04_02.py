def get_cats_info(path):
    
    cats_all_info = []
    
    try:
        with open(path, "r", encoding='utf-8') as ci:
            print('All right, let\'s go ahead')
            for line in ci:
                cat_info_dict = {}
                cat_info = line.rstrip().split(',')
                cat_info_dict['id'] = cat_info[0]
                cat_info_dict['name'] = cat_info[1]
                cat_info_dict['age'] = cat_info[2]
                cats_all_info.append(cat_info_dict)

    except FileNotFoundError:
        print(f"No such file or directory: {path}. Try again.") 
  
    return cats_all_info


cats_info = input(f"Please write path with name to file with info: ")

if len(cats_info) < 1: cats_info = "cats_info.txt"

cats_all_info = get_cats_info(cats_info)

print(cats_all_info)