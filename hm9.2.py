def difference(*args):
    if len(args) > 0:
        max_args = max(args)
        min_args = min(args)
        result = max_args - min_args
    else: result = 0
    return round(result, 2)
print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())