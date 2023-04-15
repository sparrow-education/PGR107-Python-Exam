import os

folder_path = 'resources/'
file_name = 'userdb.txt'

file_path = folder_path + file_name

abspath = os.path.abspath(file_path)


def write_to_file(value):
    try:
        with open(abspath, 'a') as f:
            f.write(value + "\n")
    except IOError as e:
        print(f'Writing error: {e}')
    except Exception as e:
        print(e)


def delete_data():
    try:
        with open(abspath, 'w') as f:
            f.write('')
    except IOError as e:
        print(f'Could not delete file: {e}')
