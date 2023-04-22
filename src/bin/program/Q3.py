def palindrome():
    print("Welcome to Palindrome checker!")
    val = input("Enter a word: ")
    val = val.strip().lower()
    is_palindrome(val)


def is_palindrome(word: str) -> bool:
    """
    By using the stack and queue algorithm principle
    We can compare each character from both end.
    If they match, then the input is palindromic.
    :param word: input string
    :return: True if palindrome or False if not
    """
    if word and word.isalpha():
        queue = []  # FIFO follows First In First Out
        stack = []  # LIFO follows Last In First Out
        for char in word:
            queue.append(char)
            stack.append(char)

        while queue:
            dequeue = queue.pop(0)  # dequeue first
            top = stack.pop()  # pop top
            if dequeue != top:  # If not equals return False
                print(f"'%s' is not a Palindrome" % word)
                return False  # False, not a palindrome

        print(f"'%s' is a Palindrome" % word)
        return True  # If code is here, it means truthiness.
    else:
        print(f'Input error, `{word}` is empty or not an alphabet.')
        return False


palindrome()
