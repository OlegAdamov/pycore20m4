
def parse_input(user_input):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):

    name, phone = args
    if name in contacts:
        return (f"This name is in your dictionary. Please write another name\n")
    contacts[name] = phone
    return "Contact added."


def all(contacts):

    all_contacts = ""

    for key, value in contacts.items():
        all_contacts += (f"{key.capitalize()} has a phone number {value}\n")
    return all_contacts


def change_contact(args, contacts):

    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def save_contacts(contact_file, contacts):

    with open(contact_file, 'w') as file:
        for contact, phone in contacts.items():
            file.write(f"{contact}: {phone}\n")


def read_file(contact_file):

    contacts = {}

    try:
        with open(contact_file, 'r') as file:

            for line in file:    #  mike: 000-000-00-00
                name, phone = line.strip().split(': ')
                contacts[name] = phone

    except FileNotFoundError:
        return contacts
    
    return contacts
    


def phone_username(args, contacts):

    name = args[0]
    return (name, contacts[name])


def init(contact_file):

    contacts = read_file(contact_file)
    return contacts


def main():

    contacts = {}  # {"Alex": "0931234567"}
    contact_file = "contacts.txt"

    commands = '''
    1) exit or close - to exit the application
    2) help - to print this menu
    3) add username phone - to add a new contact
    4) change username phone - to change the phone number your username
    5) all - to print all contacts
    6) phone username - to print phone number your username
    '''
    contacts = init(contact_file)

    print("CONTACTS BOT\n")
    print("Welcome to the assistant bot!")
    print(commands)


    while True:

        user_input = input("Enter your command (enter 'exit' or 'close' to stop): ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print('Goodbye!')
            save_contacts(contact_file, contacts)
            break

        elif command == 'hello':
            print("How can I help you?")

        elif command == 'help':
            print(commands)

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            user, phone = phone_username(args, contacts)
            print(f"Phone number {user.capitalize()} is: {phone}")

        elif command == 'all':
            print (all(contacts))

        else:
            print("Invalid command.")
            continue


if __name__ == "__main__":
    main()
