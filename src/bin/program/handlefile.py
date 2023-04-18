import os

folder_path = '../resources/'
file_name = '../resources/userdb.txt'

file_path = folder_path + file_name

abspath = os.path.abspath(file_path)


def write_to_file(usr, pw):
    try:
        if not usr or not pw:
            print("Username and password cannot be empty")
            return
        flag = False
        with open(abspath, 'a') as f:
            f.write(f"{usr}, {pw} \n")
            flag = True
        return flag
    except IOError or Exception as e:
        print(f'Writing error: {e}')


def read_from_file(usr, pw):
    try:
        token = False
        account = {}
        # Safeguard
        if not usr or not pw:
            print("Username and password cannot be empty")
            return token, account

        with open(abspath, 'rt') as f:
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
        with open(abspath, 'w') as f:
            f.write('')
    except IOError as e:
        print(f'Could not delete file: {e}')
