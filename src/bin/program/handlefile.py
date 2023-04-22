import os

folder_path = 'resources/'
file_name = 'userdb.txt'

file_path = folder_path + file_name
# TODO: Is absolute path needed or will content root suffice?
abspath = os.path.abspath(file_path)


def write_to_file(usr: str, pw: str) -> tuple[bool, dict]:
    """
    Function appends new userinfo to existing text file
    :param usr: input new username
    :param pw:  input new user password
    :return:  tuple containing boolean and new user
    """
    try:
        token = False
        account: {str, str} = {}

        if usr.isalnum() and pw.isalnum():

            with open(file_path, 'a') as file:             # mode: append to existing file
                account = {usr: pw}
                file.write(f"{usr}, {pw}\n")
                token = True

        return token, account                              # return tuple with boolean and dictionary regardless
    except IOError or Exception as e:
        print(f'Writing error: {e}')


def read_from_file(usr: str, pw: str) -> tuple[bool, dict]:
    """
    Function reads from a file, the parameter is typed declared with the expecting returning value.
    :param usr: username
    :param pw:  password
    :return:  a tuple with boolean and dictionary
    """
    try:
        token = False
        account: {str, str} = {}

        # Safeguard
        if usr.isalnum() and pw.isalnum():                # Only alphabet + numerical vals

            with open(file_path, 'rt') as file:           # auto closable resource, mode: read-text = default
                for line in file:
                    line = line.strip().replace(",", "")  # split comma
                    usr_data, usr_pw = line.split()       # tokenize usr + pws
                    if usr == usr_data and pw == usr_pw:  # evaluate input ~ data
                        account = {usr_data: usr_pw}      # args from destructuring a list[0] - [1]
                        token = True
                        break

        return token, account                             # Return bool and dictionary regardless
    except IOError or Exception as e:
        print(f"Reading error: {e}")


def delete_data():
    try:
        with open(file_path, 'w') as f:
            f.write('')
    except IOError as e:
        print(f'Could not delete file: {e}')
