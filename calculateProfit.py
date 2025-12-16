from typing import List
def calculate_Profit(buy_prices: List[float], sell_prices: List[float]) -> float:
    buy_prices = buy_prices
    sell_prices = sell_prices

    buy_sum = calculate_sum(buy_prices)
    sell_sum = calculate_sum(sell_prices)

    print(f"Total Buy Price: {buy_sum}")
    print(f"Total Sell Price: {sell_sum}")
    print(f"Total Profit: {sell_sum - buy_sum}")

    return sell_sum - buy_sum

def calculate_sum(prices):
    sum = 0
    for i in prices:
        sum += i 

    return sum

buy_prices = [120, 80, 100]
sell_prices = [130, 90, 110]
calculate_Profit(buy_prices, sell_prices)