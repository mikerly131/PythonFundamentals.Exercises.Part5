def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    * Remove the line containing the pass statement and implement the functionality described in the docstring.
    * Run the unit tests to validate that the implementation passes unit tests. 

    """
    
    # Python has built-in sorted function that can sort strings
    if sorted(first_string) == sorted(second_string):
        return True
    else:
        return False

    # remove pass statement and implement me

