from test_framework import generic_test

def simple_parity(x):
    curr = 0
    while x:
        curr = curr ^ 1
        x = x & (x - 1)
    return curr

arr = []
for i in range(2**16):
    arr.append(simple_parity(i))

def parity(x):
    BIT_MASK = 0xFFFF
    MASK_SIZE = 16
    x1 = x >> (3 * MASK_SIZE)
    x2 = x >> (2 * MASK_SIZE) & BIT_MASK
    x3 = x >> MASK_SIZE & BIT_MASK
    x4 = x & BIT_MASK
    derp = [x1, x2, x3, x4]
    return arr[x1] ^ arr[x2] ^ arr[x3] ^ arr[x4]

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
