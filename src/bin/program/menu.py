from program import Q1, Q2, Q3, Q4, Q5
from . import user as new_user


def display_menu():
    menu_list = ["Q1", "Q2", "Q3", "Q4", "Q5", "Get user", "Exit"]
    separator = "-" * 30
    print(separator)
    for i in range(len(menu_list)):
        val = menu_list[i]
        print(f"|%4s - %-21.30s|" % (f"{'q' if (i+1) == 7 else i + 1}", val))
    print(separator)
    return menu_list


def run_program(user: new_user) -> None:
    display_menu()
    while True:
        val = input("Enter choice: ")

        if val == "1":
            question_one()
        elif val == "2":
            question_two()
        elif val == "3":
            question_three()
        elif val == "4":
            question_four()
        elif val == "5":
            question_five()
        elif val == "6":
            print(f"Current logged in: %s" % user.get_user())
        elif val == "q":
            print("See you again!")
            return
        else:
            print("N/A")
        display_menu()


def question_one():
    while True:
        Q1.run_program()
        val = input("Run again? y/n: ")
        val.strip().lower()

        if val == 'n':
            break


def question_two():
    while True:
        Q2.Bug.main()
        val = input("Run again? y/n: ")
        val.strip().lower()

        if val == 'n':
            break


def question_three():
    while True:
        Q3.palindrome()
        val = input("Run again? y/n: ")
        val.strip().lower()

        if val == 'n':
            break


def question_four():
    while True:
        Q4.equality()
        val = input("Run again? y/n: ")
        val.strip().lower()

        if val == 'n':
            break


def question_five():
    while True:
        Q5.play_game()
        val = input("Run again? y/n: ")
        val.strip().lower()

        if val == 'n':
            break

def boarding() -> bool:
    txt = """
    \u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510
    \u2502                    \u2502
    \u2502  Welcome to PGR107 \u2502
    \u2502                    \u2502
    \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518
    """
    menu = {
        '': f'{txt}\n',
        '1': 'Log in',
        '2': 'Exit',
    }
    print('-' * 35)
    for key, v in menu.items():
        print(f"%s %s" % (key, v))
    print('-' * 35)
    while True:
        val = input("\nSelect an option: ")
        val = val.strip()
        if val in menu.keys():
            if val == '1':
                return True
            elif val == '2':
                return False
        else:
            print('N/A')
