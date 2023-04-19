def display_menu():
    menu_list = ["Opt 1", "Opt 2", "Opt 3", "Exit"]
    separator = "-" * 25
    print(separator)
    for i in range(len(menu_list)):
        val = menu_list[i]
        print(f"|%4s - %-16.30s|" % (i + 1, val))
    print(separator)
    return menu_list


def run_program():
    display_menu()
    while True:
        val = input("Enter choice: ")

        if val == "1":
            print(1)
        elif val == "2":
            print(2)
        elif val == "3":
            print(3)
        elif val == "4":
            print("See you again!")
            return
        else:
            print("N/A")
