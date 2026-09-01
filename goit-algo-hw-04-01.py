def total_salary(file_to_open):
    
    if len(file_to_open) < 1:
        file_to_open = "employers_salary.txt"

    employes_salary = 0.0
    counter = 0
    try:
        with open(file_to_open, 'r') as salary:
            salary.seek(0)

            for line in salary:
                
                line = line.rstrip()
                employe_salary = line.split(',')
                employes_salary += float(employe_salary[1])
                counter += 1

    except FileNotFoundError:
        return f"No such file or directory: {file_to_open}. Try again."

    try:
        return f"Total salary amount: {employes_salary}, Average salary: {employes_salary / counter:2}"

    except ZeroDivisionError as e:
        return e


file_to_open = input('Please enter name file with informaiton: ')

print(total_salary(file_to_open))
