def total_salary(file_to_open):
    
    if len(file_to_open) < 1: return 'Incorrect input'

    employes_salary = 0.0
    counter = 0
    try:
        with open(file_to_open, 'r', encoding='utf-8') as salary:
            salary.seek(0)

            for line in salary:

                try:
                    line = line.rstrip()
                    employe_salary = line.split(',')
                    employes_salary += float(employe_salary[1])
                    counter += 1

                except IndexError:
                    print (f"{employe_salary[0]} dees not have a salary")
                except ValueError:
                    print (f"{employe_salary[0]} have a incorrect data")

    except FileNotFoundError as not_found:
        return not_found

    try:
        return employes_salary, (employes_salary / counter)

    except ZeroDivisionError as zero_div:
        return zero_div


file_to_open = input('Please enter name file with informaiton: ')

total, average = total_salary(file_to_open)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
