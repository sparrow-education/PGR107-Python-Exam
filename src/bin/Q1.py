# read a txt file
# compare that file with a list of words
# replace the words in the file with the "******"
# write the new file to a new file

def run_program():
    sensitiv_word_list = []
    read_sensitive_words_from_file(sensitiv_word_list)

    random_text_list = []
    read_random_text_from_file(random_text_list)

    redacted_text = []
    compare_words(sensitiv_word_list, random_text_list, redacted_text)

    print(redacted_text, end="")



def read_sensitive_words_from_file(sensitiv_word_list):
    filename = "sensitive_words.txt"
    file = open(filename, "r")
    for word in file:
        sensitiv_word_list.append(word)
    file.close()


def read_random_text_from_file(random_text_list):
    filename = "random_text.txt"
    file = open(filename, "r")
    for word in file:
        random_text_list.append(word.strip())
    file.close()

def compare_words(sensitiv_word_list, random_text_list, redacted_text):
    for word in random_text_list:
        if word.lower() in  sensitiv_word_list:
            redacted_text.append("******")
        else:
            redacted_text.append(word)

run_program()