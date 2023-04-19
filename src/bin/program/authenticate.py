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
    if token:
        current = new_user.User(account.keys(), account.values())
        print(f"Welcome back, {str(current.get_user()).capitalize()}!")
        logged_in = True
        return logged_in
    else:
        print(f"Couldn't find {usr}")
        val = input("Create user y/n: ")

        choice = ['y', 'n']
        val = val.strip().lower()
        while True:
            if val == 'y':
                if create():
                    print("\nCreate successful!\n")
                    logged_in = True
                else:
                    print("\nCreate unsuccessful!\n")
                    logged_in = False
                return logged_in
            elif val == 'n':
                return logged_in
            else:
                print("Not a valid option!")
                val = input("Create user y/n: ")


