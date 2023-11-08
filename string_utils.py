
def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(str_in) 
    # remove pass statement and implement me
    


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    first_letter = str_in[0:1]
    return first_letter 
    # remove pass statement and implement me
    

def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    last_letter = str_in[-1]
    return last_letter # remove pass statement and implement me


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    string_finder = str_in.find(sub_str_in)
    if string_finder == -1:
        return False
    else:
        return True
    # remove pass statement and implement me

    """
    This way works as well....the POWER of in on display
    if sub_str_in in str_in:
        return True
    else:
        return False    
    """


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    sub_string = str_in[start:stop]
    return sub_string
      # remove pass statement and implement me


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """

    # well there is the .swapcase method
    return str_in.swapcase()

    """
       for letter in str_in:
        
        if letter < 'a':
            letter = letter.upper()
        elif:
            letter = letter.upper()

    """
     # remove pass statement and implement me
