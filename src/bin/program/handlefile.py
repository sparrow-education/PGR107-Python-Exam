import os

folder_path = 'resources/'
file_name = 'userdb.txt'

file_path = folder_path + file_name
# TODO: Is absolute path needed or will content root suffice?
abspath = os.path.abspath(file_path)


def write_to_file(usr, pw):
    token = False
    try:
        if not usr or not pw:
            print("Username and password cannot be empty")
            return token
        with open(file_path, 'a') as f:
            f.write(f"{usr}, {pw} \n")
            token = True
        return token
    except IOError or Exception as e:
        print(f'Writing error: {e}')
    return token


def read_from_file(usr, pw):
    try:
        token = False
        account = {}
        # Safeguard
        if not usr or not pw:
            print("Username and password cannot be empty")
            return token, account

        with open(file_path, 'rt') as f:
            for line in f:
                line = line.strip().replace(",", "")  # split comma
                usr_data, usr_pw = line.split()  # tokenize usr + pw
                if usr == usr_data and pw == usr_pw:  # evaluate input ~ data
                    account = {usr_data: usr_pw}
                    token = True
                    break
        return token, account
    except IOError or Exception as e:
        print(f"Reading error: {e}")


def delete_data():
    try:
        with open(file_path, 'w') as f:
            f.write('')
    except IOError as e:
        print(f'Could not delete file: {e}')
