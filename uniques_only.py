def uniques_only(items):
    result = dict()
    for item in items:
        result[item] = 0
    return iter(list(result.keys()))

uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']])