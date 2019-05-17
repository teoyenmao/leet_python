from math import sqrt


# Prime number: number that itself can be divided by 1 only.
# Eg: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

def is_prime_number(n):
    # 1 is not prime number
    if n == 1:
        return False

    x = int(sqrt(n))
    for i in range(2, x+1):
        if n % i == 0:
            return False
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    chk = is_prime_number(n)
    print("Prime" if chk else "Not prime")
