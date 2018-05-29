from test_framework import generic_test


def power(x, y):
    # print(bin(y))
    curr = x
    res = 1
    is_negative = False
    if y < 0:
        is_negative = True
        y = -y
    while y:
        if 1 & y:
           res *= curr
        y = y >> 1
        curr = curr * curr
        # print(curr)
    if is_negative:
        return 1/res
    else:
        return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
