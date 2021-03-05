src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [n for idx, n in enumerate(src) if n > src[idx - 1] and idx != 0]

print(result)
