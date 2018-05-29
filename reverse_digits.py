from test_framework import generic_test

def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    res = x % 10
    x = x // 10

    while x > 0:
        res *= 10
        res += x % 10
        x = x // 10

    return res * sign

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
