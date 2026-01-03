from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    list_result = create_list(num)
    print(list_result)

    filter_even_numbers(list_result)
    list_result.reverse()
    print(list_result)
    return list_result

def create_list(num:int) -> List[int]:
    new_list = []
    if num <= 3:
        return [0]
    else:
        # start from num-3 untill 0 with step -3
        for i in range(num-3, 0, -3):
            new_list.append(i)
        return new_list

def filter_even_numbers(created_list: list) -> None:
    for i in created_list:
        if i % 2 != 0:
            created_list.remove(i)
    

countdown(10)