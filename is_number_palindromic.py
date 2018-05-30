from test_framework import generic_test


def is_palindrome_number(x):
    original = x
    if x < 0:
        return False
    reversed = 0
    while x:
        reversed = (reversed * 10) + x % 10
        x = x // 10

    return original == reversed


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
