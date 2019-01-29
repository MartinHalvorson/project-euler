# Finds sum of all eleven truncatable primes

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    string = str(n)
    for i in range(len(string)):
        if not is_prime(int(string[i:])):
            return False
        if not is_prime(int(string[:i+1])):
            return False
    return True


sum = 0
for i in range(11, 1000000):
    if is_truncatable_prime(i):
        print(i)
        sum += i

print("Sum: %d" % sum)

