def count_ones(x):
    num = 0
    while x:

        num += x & 1
        x = x >> 1
    return num

