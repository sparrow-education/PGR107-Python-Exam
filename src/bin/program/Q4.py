def equality():
    """
    Safety guard the Pythonic way for input error
    Check both inputs for empty strings AND truthiness
    I assume we are comparing the text literal not the actual ASCII value i.e. 'p' vs 'P'
    """
    print("\nCompare two string for equality!\n")
    val1 = input("Enter first word: ")
    val2 = input("Enter second word: ")

    if (val1.islower() and val2.islower()) and (val1.isalpha() and val2.isalpha()):
        unique = is_unique(val1, val2)
        shared = is_shared(val1, val2)
        non_occurring(unique, shared)
    else:
        print(f"Input error, '{val1}' AND '{val2}' has to be a lowercase alphabet.")
        return


def is_unique(word1: str, word2: str) -> list[str]:
    """
    Using Python's collection 'set' constructor passing two inputs as arguments.
    symmetric_difference method will return all characters that are not presents in both
    Then neatly using Python's collection 'list' constructor to pass in our unique set
    And return the result as list
    :param word1: input text 1
    :param word2: input text 2
    :return: A sorted list of uniques in order
    """

    unique = set(word1).symmetric_difference(word2)
    sort_unique = list(unique)
    sort_unique.sort()

    print(f"\nUnique characters: ", end="")
    if sort_unique:
        for c in sort_unique:
            print(f"%s" % c, end=", ")
    else:
        print(None)
    return sort_unique


def is_shared(word1: str, word2: str) -> list[str]:
    """
    Using intersection will also iterate through both strings
    returns a set of characters that are present in both sets
    Sorting the sets
    :param word1: input text 1
    :param word2: input text 2
    :return: a list of shared characters
    """
    shared = set(word1).intersection(word2)
    sort_shared = list(shared)
    sort_shared.sort()
    print(f"\nShared character{'' if len(sort_shared) <= 1 else 's'}: ", end="")
    if sort_shared:
        for c in sort_shared:
            print(f"%s" % c, end=", ")
    else:
        print(None)
    return sort_shared


def non_occurring(list1: list, list2: list) -> None:
    """
    1. Convert string literal into a set of strings.
    2. Then using 'union' to unify all characters from both lists
    3. And use 'difference' to return all characters existing in 'set_of_strings' but NOT in 'unified'
    4. Finally, we sort the set as list using sort method.
    :param list1: input list 1
    :param list2: input list 2
    :return: None
    """
    string = 'abcdefghijklmnopqrstuvwxyz'
    set_of_strings = set(string)

    unified = set(list1).union(list2)

    not_present = set_of_strings.difference(unified)
    sort_not_present = list(not_present)
    sort_not_present.sort()
    print("\n\nNot occurred: ", end="")
    if sort_not_present:
        for c in sort_not_present:
            print(f"%s" % c, end=", ")
    else:
        print(None)
    print()
