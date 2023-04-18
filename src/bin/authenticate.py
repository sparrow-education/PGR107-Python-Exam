import handlefile as make


def login():
    usr = input("Enter user: ")
    pw = input("Enter password: ")

    token = make.read_from_file(usr, pw)
    if token:
        print(f"Welcome back, {usr.capitalize()}")
    else:
        print(f"Couldn't find {usr}")
        val = input("Create user y/n: ")

        choice = ['y', 'n']
        val = val.strip().lower()
        while val in choice:
            if val == 'y':
                print('Creating...')
                break
            else:
                return


login()
