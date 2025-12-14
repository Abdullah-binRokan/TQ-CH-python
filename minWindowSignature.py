from typing import List

def minWindowSignature(log: str, pattern: str) -> str:
    # write your code here ^_^
    # split strings into lists to help find min window
    log_list = list(log)
    pattern_list = list(pattern)

    all_windows:list = extract_all_windows(log_list, pattern_list)
    min_window:str = extract_min_window(all_windows)
    return ""


def extract_min_window(all_windows:list) -> str:
    """ compare windows then return min window or empty string """
    min_window_index:int = 0
    all_windows_len:int = len(all_windows)

    for index, value in enumerate(all_windows):
        print("^^^^^^^^^^^^^^^^^^^^^^^^")
        print("index:", index, "value: ", value)
        print("^^^^^^^^^^^^^^^^^^^^^^^^")
        # terminate the loop if you reach final element
        if index + 1 == all_windows_len:
            break 
        # compare length with smallest found window to get the min
        elif len(value) < len(all_windows[min_window_index]):
            min_window_index = index
            print("--------------------------------")
            print("min_window_index", min_window_index)
            print("--------------------------------")

    print("???????????????")
    print("min_window_index: ", min_window_index)
    print("???????????????")

def extract_all_windows(log_list:list, pattern_list:list) -> list:
    """ extract all windows then return it as a list """
    windows_collection:list = []
    log_len:int = len(log_list)
    log_counter:int = 0

    while log_counter < log_len:
        # check for window starting from specific emelent (log_counter)
        current_window = check_for_window(log_list[log_counter:], pattern_list)
        print("$$$ the window $$$: ", current_window)
        # check if log has no more window return the collection
        if current_window == "":
            return windows_collection
        else:
            windows_collection.append(current_window)
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
                print("*** window started ***")
                is_started = True
            # remove the first occurance of the pattern
            pattern_copy.remove(value)

            # check if pattern_copy is empty return window as str
            if len(pattern_copy) == 0:
                window_end = index
                print("--- window Ended ---")

                window_list = log_list[window_start:window_end+1]
                print("window list:", window_list)
                window_str = "".join(window_list)
                print("Window str: ", window_str)
                return window_str
            
    return ""

# main
# log = "ADOBECODEBANC"
log = "ADOBECODEBANCADOBEC"
# log = "ADOBE"
pattern = "ABC"

print("calling minWindow")
minWindowSignature(log, pattern)