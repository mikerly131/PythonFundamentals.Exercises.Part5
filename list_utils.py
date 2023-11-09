from typing import List
import math


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """

    return list_in[pos]

    # remove pass statement and implement me


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    for item in list_in:
        print(item)
    return None
    # remove pass statement and implement me


def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
   
    """
    I should try to figure out a bubble sort again sometime
    smallest = list_in[0][1]
    length = len(list_in)
    
    for num in range(0, length-1):

        number = list_in[num][1]
        
        if number < smallest:
            list_in[0][1] = list_in[num][1]
            smallest = number
    
    return list_in
    
    """
    # I looked up sorted method, that creates a new list and i need same list
    # I found that .sort can take an argument to sort by
    # I need to put in key= not just what I want they function to sort by to be
    list_in.sort(key=lambda x: x[1])
    return list_in
         

    # remove pass statement and implement me


def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    num_list = []
    for num in  range(0, n):
        num_list.append((num))

    return num_list

    # remove pass statement and implement me


def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    list_len = len(list_in)
    half_num_odd = math.ceil(list_len / 2)
    half_num_even = list_len // 2

    if (list_len % 2) != 0:
        if (half == 1):
                halved_list = list_in[0:half_num_odd]
        else:
                halved_list = list_in[half_num_odd:list_len]
    else:
        if (half == 1):
                halved_list = list_in[0:half_num_even]
        else: 
                halved_list = list_in[half_num_even:list_len]

    return halved_list
      # remove pass statement and implement me


def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    
    for num in list_in:

        if (num % 2 == 0):
            pass
        else:
            list_in.remove(num)
    
    return None

    # remove pass statement and implement me


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """

    for num in list_in:

        if (num % 2 == 0):
            list_in.remove(num)
    
    return None
    # remove pass statement and implement me


def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    new_list = list_a + list_b
    return new_list

    # remove pass statement and implement me


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    new_list = list_in * scalar
    return new_list
    # remove pass statement and implement me
