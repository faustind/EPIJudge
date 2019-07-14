from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_so_far, max_so_far = float('inf'), float('-inf')
    for price in prices:
        min_so_far = min(min_so_far, price)
        max_so_far = max(max_so_far, price-min_so_far)
    return max_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
