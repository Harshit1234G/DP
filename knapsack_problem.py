"""
Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w. Implement recursive, memoization and dp solutions and compare there time complexity.
"""
from jovian.pythondsa import evaluate_test_case


# Recursive solution
def max_profit_recursive(
    capacity: int,
    weights: list[int],
    profits: list[int],
    index: int = 0
) -> int:
    if index == len(weights):
        return 0

    if weights[index] > capacity:
        return max_profit_recursive(capacity, weights, profits, index + 1)

    else:
        return max(
            max_profit_recursive(capacity, weights, profits, index + 1),
            profits[index] + max_profit_recursive(
                capacity - weights[index], weights, profits, index + 1)
        )


# Memoization solution
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def max_profit_memo(
    capacity: int,
    weights: list[int],
    profits: list[int],
    index: int = 0
) -> int:
    if index == len(weights):
        return 0

    if weights[index] > capacity:
        return max_profit_recursive(capacity, weights, profits, index + 1)

    else:
        return max(
            max_profit_recursive(capacity, weights, profits, index + 1),
            profits[index] + max_profit_recursive(
                capacity - weights[index], weights, profits, index + 1)
        )


# DP solution
def max_profit_dp(
    capacity: int,
    weights: list[int],
    profits: list[int]
) -> int:
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c],
                                        profits[idx] + results[idx][c-weights[idx]])

    return results[-1][-1]


if __name__ == '__main__':
    test_case = {
        'input': {
            'capacity': 365,
            'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82, 24, 32, 30, 45, 54, 39, 64, 86, 90, 83],
            'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72, 93, 58, 50, 69, 61, 44, 68, 85, 88, 73]
        },
        'output': 657
    }

    print('Recursive approach:')
    evaluate_test_case(max_profit_recursive, test_case)
    print('Memoization approach:')
    evaluate_test_case(max_profit_memo, test_case)
    print('DP approach:')
    evaluate_test_case(max_profit_dp, test_case)
