from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    list_result = create_list(num)
    print(list_result)


def create_list(num:int) -> List[int]:
    new_list = []
    if num < 3:
        return [0]
    else:
        for i in range(num, 0, -3):
            new_list.append(i)
        return new_list


countdown(10)