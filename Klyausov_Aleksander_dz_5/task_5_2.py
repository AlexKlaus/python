from itertools import islice


def odd_nums(n):
    return (odd_number for odd_number in range(1, n + 1, 2))


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(next(odd_to_15))
print(*islice(odd_to_15, 7))
print(next(odd_to_15))  # StopIteration
