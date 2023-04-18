import handlefile as make
import user as new_user


def create():
    usr = input("Enter username: ")
    pw = input("Enter password: ")
    return make.write_to_file(usr.strip(), pw.strip())


def login():
    usr = input("Enter user: ")
    pw = input("Enter password: ")
    token, account = make.read_from_file(usr, pw)
    if token:
        current = new_user.User(account.keys(), account.values())
        print(f"Welcome back, {str(current.get_user()).capitalize()}!")
    else:
        print(f"Couldn't find {usr}")
        val = input("Create user y/n: ")

        choice = ['y', 'n']
        val = val.strip().lower()
        while val in choice:
            if val == 'y':
                if create():
                    print("Create successful\n")
                else:
                    print("Create unsuccessful\n")
                break
            else:
                return


login()
