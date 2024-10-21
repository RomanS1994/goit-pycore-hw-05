def input_error(func):
    '''
    Decorator for handling errors in command processing functions.
   Parameters:
    func (function): The function to which the decorator is applied.

    Returns:
    function: Internal function that handles errors
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please." 
        except KeyError:
            return 'The number is not found in the address book'
        except IndexError:
            return 'Not enough arguments.'
        
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
 
@input_error
def show_all(contacts):
    return contacts


def main():
    '''
    The main function for launching an assistant bot.

    Accepts commands from the user and executes them.
    '''


    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
