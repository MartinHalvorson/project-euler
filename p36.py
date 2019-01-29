# Finds sum of all numbers, less than one million, which are palindromic in base 10 and base 2

sum = 0


def is_palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    else:
        return False

for i in range(1, 1000000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        print(i)
        sum += i

print("Sum: %d" % sum)