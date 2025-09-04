def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not defined!"
    return inner


@input_error
def parse_input(user_input: str) -> list[str]:
    """
    takes a user input string user_input and splits it into words 
    using the split() method. It returns the first word as the 
    command cmd and the rest as a list of arguments *args
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts: dict) -> str:
    """
    The add_contact function is designed to add a new contact to the contacts dictionary. 
    It takes two arguments: args, which is a list containing the name and phone number, 
    and contacts, which is a dictionary where the contacts are stored.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict) -> str:
    """
    stores a new phone number for the contact
    username that already exists in the dictionary
    """
    name, phone = args
    if contacts.get(f"{name}"):
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts: dict) -> str:
    """
    return the phone number for the
    specified contact username to the console
    """
    name = args[0]
    if contacts.get(f"{name}"):
        phone = contacts[name]
        return f"{name} {phone}"
    else:
        raise KeyError


def show_all(contacts: dict) -> str:
    """
    return the phone number for all contacts
    """
    for contact in contacts.items():
        print(f"{contact[0]} {contact[1]}")


def main():
    # create an empty list for further filling
    contacts = {}
    print("Welcome to the assistant bot!")
    # an infinite loop in which the main logic of the program is processed
    while True:
        # receive input from the user
        user_input = input("Enter a command: ")
        # separate user input into commands and arguments
        command, *args = parse_input(user_input)
        # condition for completing an infinite loop
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # condition for making changes to an existing contact
        elif command == "change":
            print(change_contact(args, contacts))
        # condition for displaying one contact in the console
        elif command == "phone":
            print(show_phone(args, contacts))
        # condition for displaying all contacts in the console
        elif command == "all":
            show_all(contacts)
        # condition for displaying a welcome message
        elif command == "hello":
            print("How can I help you?")
        # condition for adding new phone number to dictionary
        elif command == "add":
            print(add_contact(args, contacts))
        # condition for all unforeseen commands
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
