from typing import List

def minWindowSignature(log: str, pattern: str) -> str:
    # write your code here ^_^
    # split strings into lists to help find min window
    log_list = list(log)
    pattern_list = list(pattern)

    all_windows:list = extract_all_windows(log_list, pattern_list)
    return ""


def extract_all_windows(log_list:list, pattern_list:list) -> list:
    """ extract all windows then return it as list """
    windows_collection:list = []
    is_log_finished:bool = False
    log_len:int = len(log_list)
    pattern_len:int = len(pattern_list)
    log_counter:int = 0

    while log_counter < log_len:
        # check for window starting from specific emelent (log_counter)
        windows_collection.append(check_for_window(log_list[log_counter:], pattern_list))
        log_counter += 1
    
    print("all windows: ", windows_collection)
    return windows_collection


def check_for_window(log_list:list, pattern_list: list) -> str:
    """ loop through log and extract a window """
    is_started:bool = False
    window_start:int = 0
    window_end:int = 0
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


# main
log = "ADOBECODEBANC"
pattern = "ABC"

print("calling minWindow")
minWindowSignature(log, pattern)