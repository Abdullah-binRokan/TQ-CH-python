from typing import List
def top3Average(scores: List[int]) -> float:
    # write your code here ^_^
    # if the array has more than 3 elements
    if len(scores) > 3:
        # initialize max values
        max1, max2, max3 = scores[0], scores[1], scores[2]
        # start the loop from the 4th element
        for score in scores[3:]:
            if score > max1 or score > max2 or score > max3:
                # figuer out smallest max then update it
                if max1 <= max2:
                    if max1 <= max3:
                        max1 = score
                    else:
                        max3 = score
                elif max2 <= max3:
                    max2 = score
                else:
                    max3 = score

        average:float = (max1 + max2 + max3) / 3
        print(average)
        return average
    else:
        sum:float = 0
        for score in scores:
            sum += score

        average = sum / len(scores)
        print(average)
        return average


scores = [10, 80, 90, 50, 95]
# scores = [100, 100, 100]
# scores = [70, 80]
# scores = [55]



top3Average(scores)