def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    temp = value.lower()
    word = temp.replace(" ", "")
    reverse = word[::-1]

    print(word)
    print(reverse)

    if word == reverse:
        return True
    else:
        return False
        
    # remove pass statement and implement me
