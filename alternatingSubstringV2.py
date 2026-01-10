from typing import List
def longest_alternating_substring(digits: str) -> str:
    # initilize max_alternating with ""
    max_alternating: str = ""

    # loop through the numbers from start to len(digits)
        # initilize current as digits[start]

        # loop from next (start + 1) to len(digits)
            # if current and next are alternated
                # assign current as next
            # else
                # they are not alternated so break the loop

        # if the substring is bigger, assign it to max_alternating

    # return max_alternating




digits = "2105787220351146"
# digits = "12057872203511461"
# digits = "12357872203511461"
# digits = "21457872203511461"
# digits = "213"
# digits = "2131"
# digits = "21"
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