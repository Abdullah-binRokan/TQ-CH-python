from typing import List

def minWindowSignature(log: str, pattern: str) -> str:
    # write your code here ^_^
    log_counter:int = 0

    # split strings into lists to help find min window
    log_list = list(log)
    pattern_list = list(pattern)

    min_window = check_for_window(log_list, pattern_list)
    print("min window:", min_window)
    return ""



def check_for_window(log_list:list, pattern_list: list) -> str:
    """ loop through log and extract a window """
    is_started = False
    is_log_finished = False
    log_len = len(log_list)
    pattern_len = len(pattern_list)
    window_start = 0
    window_end = 0
    # create a copy of pattern_list using slicing
    pattern_copy = pattern_list[:]

    # register start and end of window
    for index, value in enumerate(log_list):
        print("Looping index", index, "value:", value)
        if value in pattern_copy:
            # check if not started the window
            if not is_started:
                window_start = index
                is_started = True
            # remove the first occurance of the pattern
            pattern_copy.remove(value)

            # check if pattern_copy is empty return window as str
            if len(pattern_copy) == 0:
                window_end = index
                window_list = log_list[window_start:window_end+1]
                print("window list:", window_list)
                window_str = "".join(window_list)
                print("Window str: ", window_str)
                return window_str



log = "ADOBECODEBANC"
pattern = "ABC"

print("calling minWindow")
minWindowSignature(log, pattern)