def run_program():
    display_info()

    sensitive_word_list = []
    read_sensitive_words_from_file(sensitive_word_list)

    random_text_list = []
    read_random_text_from_file(random_text_list)

    redacted_text = compare_words_in_lists(sensitive_word_list, random_text_list)

    with open("redacted_random_text.txt", "w") as file:
        for line in redacted_text:
            file.write(line + "\n")

    print("-----------------------------------------")
    print("Check out new redacted text file named; redacted_random_text")
    print("-----------------------------------------")

def display_info():
    print("Welcome to the redacted text program.")
    print("This is a program for Question of the exam")
    print("-----------------------------------------")


# A function that reads the "Sensitive words" from the text file and return the words in list.
def read_sensitive_words_from_file(sensitive_word_list):
    while True:
        try:
            filename = input("Type in the text file that contain the sensitive words: ")
            with open(filename, "r") as file:
                for word in file:
                    sensitive_word_list.append(word.strip())
            break
        except FileNotFoundError:
            print("File not found. Please try again.")


# A function that reads some text from a text file and append it to a list.
def read_random_text_from_file(random_text_list):
    while True:
        try:
            filename = input("Type in the text file that needs redacting: ")
            with open(filename, "r") as file:
                for word in file:
                    random_text_list.append(word.strip())
            break
        except FileNotFoundError:
            print("File not found. Please try again.")


# A function that compare and check if the words in sensitive word list is in the random text list and change the word if its sensitive.
def compare_words_in_lists(sensitive_word_list, random_text_list):
    redacted_text = []
    for text in random_text_list:
        for word in sensitive_word_list:
            text = text.replace(word, '*' * len(word))
        redacted_text.append(text)
    return redacted_text


run_program()
