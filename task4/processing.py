import functools

def input_error_add(func):
    """This decorator handles the possible errors for the functio add_contact"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Give me name and phone please."
        except KeyError as e:
            return str(e)
        except IndexError as e:
            return "Error: You need to provide both name and phone."

    return inner

def input_error_change(func):
    """This decorator handles the possible errors for the functio change_contact"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise KeyError("Error: This name couldn't be found.")
            return result 
        except ValueError:
            return "Error: Give me name and phone please."
        except KeyError as e:
            return str(e)
        except IndexError as e:
            return str(e)
    return inner

def input_error_show(func):
    """This decorator handles the possible errors for the functio show_phone"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise KeyError("Error: Contact not found")
            return result
        except IndexError:
            return "Error: Give me name of the user."
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
    return inner

def input_error_all(func):
    """This decorator handles the possible errors for the functio show_all"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise KeyError("Error: The contact list is empty")
            return result
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)
        

    return inner

def input_parse_input(func):
    """This decorator handles the possible errors for the functio parse_input"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Error: Add a command please")
            return "Error: Add a command please" 
    return inner


@input_parse_input
def parse_input(user_input):
    "This function parses the users input"
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_add
def add_contact(args, contacts):
    "This function creats the user with phone number"
    name, phone = args
    if name in contacts:
        raise KeyError ("Error: Enter unique name please")
    contacts[name] = phone
    return "Contact added."

@input_error_change
def change_contact(args, contacts):
    "The function updated the user' phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

@input_error_show   
def show_phone(args, contacts):
    "This function shows users phone by the name"
    name = args[0]
    return contacts.get(name)

@input_error_all
def show_all(contacts):
    "This function shows all user's contacts"
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) if contacts else None
    