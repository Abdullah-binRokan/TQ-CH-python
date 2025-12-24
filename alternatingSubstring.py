from typing import List
def longest_alternating_substring(digits: str) -> str:
    # write your code here ^_^
    # define alternating_list to store all alternating substrings
    alternating_list = []
    last_current_index: int = 0

    # call extract_alternating_substrings and store the result in the alternating_list
    extract_alternating_substrings(alternating_list, digits)

    # call find_longest to get the longest substring from alternating_list


# define extract_alternating_substrings function to extract alternating substrings
def extract_alternating_substrings(alternating_list: list, digits: str) -> None:
    """ extract alternating substrings then fill them in alternating_list """
    digits_length: int = len(digits)
    start_index: int = 0
    end_index: int = 0
    is_started: bool = False
    is_odd_started: bool = False
    # loop through the string starting from a given index
    i = 0
    # avoid not having a pair of two elements at the end of list
    while i <= digits_length - 2:
        print(f" i: {i},  1st: {digits[i]}, 2nd: {digits[i + 1]}")
        # check if alternated substring is going to start
        if not is_started and are_alternated(digits[i], digits[i + 1]):
            start_index = i
            is_started = True
            is_odd_started = True if int(digits[i]) % 2 != 0 else False
            print("start_index: ", start_index)
        # check if the substring not initiated with odd num or the current digit is not odd  
        elif not is_odd_started or not is_odd(digits[i]):
            print("is_odd: ", is_odd(digits[i]))
        
        # avoid not having a pair of two elements at the end of list
        if digits_length - i == 3:
            i += 1
        else:
            i += 2


# define find_longest function to find the longest substring from a list of substrings


# define function to check if two numbers are alternated
def are_alternated(first_num: str, second_num: str) -> bool:
    """ checks two numbers if they are alternated (odd and even) """
    int_first_num: int = int(first_num)
    int_second_num: int = int(second_num)

    if int_first_num % 2 == 0 and int_second_num % 2 != 0:
        return True
    elif int_first_num % 2 != 0 and int_second_num % 2 == 0:
        return True
    else:
        return False


# define function to check if the number is odd
def is_odd(num: str) -> bool:
    int_num: int = int(num)
    return True if int_num % 2 != 0 else False

# digits = "2105787220351146"
digits = "12057872203511461"
# digits = "213"

longest_alternating_substring(digits)