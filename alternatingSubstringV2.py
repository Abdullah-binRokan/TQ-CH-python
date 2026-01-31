from typing import List
def longest_alternating_substring(digits: str) -> str:
    # initilize max_alternating with ""
    max_alternating: str = ""

    # loop through the numbers from start to len(digits)
    for start in range(len(digits)):
        # initilize current as start
        current: int = start
        print("start: ", start)

        # loop from next (start + 1) to len(digits)
        is_breaked: bool = False
        for next in range(start + 1, len(digits)):
            print("next: ", next)
            if are_alternated(digits[current], digits[next]):
                current = next
            else:                
                # they are not alternated so break the loop
                print("****** break at: ", digits[next])
                is_breaked = True
                break

        # check if next reached the final element or breaked
        current_alternating: str = digits[start:next] if is_breaked else digits[start:next + 1]
        # if the substring is bigger, assign it to max_alternating
        print("current_alternating: ", current_alternating)
        if len(max_alternating) < len(current_alternating):
            max_alternating = current_alternating
        print("-------max_alternating: ", max_alternating)
        
    print("max_alternating: ", max_alternating)
    # return max_alternating
    return max_alternating


def are_alternated(current_str: str, next_str: str) -> bool:
    """ check if two numbers are alternated """
    current: int = int(current_str)
    next: int = int(next_str)

    if (current % 2 == 0 and next % 2 != 0) or (current % 2 != 0 and next % 2 == 0):
        return True
    else:
        return False
    

# digits = "2105787220351146"
# digits = "12057872203511461"
# digits = "12357872203511461"
# digits = "21457872203511461"
# digits = "213"
# digits = "2131"
digits = "21"
# digits = "1"
# digits = ""
# digits = '2105787220351146'
# digits = '1263654081858902'
# digits = '334090830025543'
# digits = '6769423178839463'

# digits = "210556789"
# digits = "224567"
# digits = "21034"
# digits = "5"

longest_alternating_substring(digits)