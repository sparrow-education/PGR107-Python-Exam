from . import handlefile as make
from . import user as new_user


def create():
    usr = input("Create username: ")
    pw = input("Create password: ")
    return make.write_to_file(usr.strip(), pw.strip())


def verify():
    usr = input("Enter user: ")
    pw = input("Enter password: ")

    token, account = make.read_from_file(usr, pw)
    logged_in = False
    current = None

    if token:
        current = new_user.User(account.keys(), account.values())
        print(f"Welcome back, {str(current.get_user()).capitalize()}!")
        logged_in = True
        return logged_in, current
    else:
        print(f"Couldn't find '{usr}'")
        val = input("Create user y/n: ")
        # TODO: Sentinel value of while may be 'choice' or 'True' not decided yet
        choice = ['y', 'n']
        val = val.strip().lower()
        while True:
            if val == 'y':
                token, account = create()
                if token:
                    print("\nCreate successful!\n")
                    logged_in = True
                    current = new_user.User(str(account.keys()), str(account.values()))
                else:
                    print("\nCreate unsuccessful!\n")
                    logged_in = False
                return logged_in, current
            elif val == 'n':
                return logged_in, current
            else:
                print("Not a valid option!")
                val = input("Create user y/n: ")
