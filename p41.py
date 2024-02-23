"""
Uses all digits 1-9
Iterate largest to smallest
Also check if it is prime
"""


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True


def gen_nums(nums_list, res):
    if len(nums_list) == 0:
        n = int("".join(res))
        if is_prime(n):
            print(n)
            exit(0)
        else:
            return
    else:
        for i in range(len(nums_list)):
            gen_nums(nums_list[:i]+nums_list[i+1:], res + [nums_list[i]])


# Start with '9' and '8' in the list. Remove digits until a prime is found.
digits = ['7', '6', '5', '4', '3', '2', '1']

gen_nums(digits, [])
