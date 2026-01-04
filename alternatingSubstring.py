from typing import List
def longest_alternating_substring(digits: str) -> str:
    # write your code here ^_^
    # define alternating_list to store all alternating substrings
    alternating_list = []
    last_current_index: int = 0

    # call extract_alternating_substrings and store the result in the alternating_list
    extract_alternating_substrings(alternating_list, digits)

    # call find_longest to get the longest substring from alternating_list
    longest_substring: str = find_longest_substring(alternating_list)

    print("longest: ", longest_substring)
    return longest_substring

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
        # check if the substring pairs started with odd num but the current first digit not odd or vice versa
        started_different_than_current =  (is_odd_started and not is_odd(digits[i]) 
                                          or (not is_odd_started and is_odd(digits[i])))
        print(f" i: {i},  1st: {digits[i]}, 2nd: {digits[i + 1]}")
        # check if alternated substring is going to start
        if not is_started and are_alternated(digits[i], digits[i + 1]):
            start_index = i
            is_started = True
            is_odd_started = True if int(digits[i]) % 2 != 0 else False
            print("start_index: ", start_index)
        # check if alternated substring ended
        elif is_started and (started_different_than_current or not are_alternated(digits[i], digits[i + 1])):
            end_index = i
            print("is_odd: ", is_odd(digits[i]))
            print("end_index: ", end_index)
            # call slicing function
            slice_alternated(start_index, end_index, alternating_list, started_different_than_current)

            # reset the variables to enable extracting remaining alternating substring
            is_started = False
            is_odd_started = False
        
        # avoid jumping new alternated pairs if we ending endex
        if are_alternated(digits[i], digits[i + 1]) and (end_index == i and end_index > 0) and start_index != i:
            # run the loop with same counter to start extracting the current alternated substring
            i += 0
        # avoid missing alternated substring if we reached last pair
        elif digits_length - i == 2 and is_started:
            print("catch ending index: ", i + 1)
            end_index = i + 1
            slice_alternated(start_index, end_index, alternating_list, started_different_than_current)
            i+= 1
        # avoid not having a pair of two elements at the end of list or jumping from alternated pair
        elif digits_length - i == 3 or not are_alternated(digits[i], digits[i + 1]):
            i += 1
        else:
            # we have alternated pair so we can jump one iteration and compare with next pair
            i += 2


# define find_longest function to find the longest substring from a list of substrings
def find_longest_substring(alternating_list: list) -> str:
    """ find longest substring """
    longest_str: str = ""
    for i in alternating_list:
        if len(i) > len(longest_str):
            longest_str = i

    return longest_str

# define function to slice the alternated substring 
def slice_alternated(start_index: int, end_index: int, alternating_list: list, started_different_than_current: bool ):
    """ slice the alternated substring then append it to the list """
    # include end index since it is only 2 elements
    if end_index - start_index < 2:
        alternating_list.append(digits[start_index : end_index + 1])
    # Slicing the next item if it alternates with end_index
    elif started_different_than_current:
        alternating_list.append(digits[start_index : end_index]) 
    else:
        alternating_list.append(digits[start_index : end_index + 1])
    print("************")
    print(alternating_list)
    print("************")

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

digits = "2105787220351146"
# digits = "12057872203511461"
# digits = "12357872203511461"
# digits = "21457872203511461"
# digits = "213"
# digits = "2131"
# digits = "21"
# digits = "1"
# digits = ""

longest_alternating_substring(digits)