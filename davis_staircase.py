
# Tip: refer to Finbonacci

ways = {1: 1, 2: 2, 3: 4}

def counting(n):
    if n not in ways.keys():
        ways[n] = counting(n - 1) + counting(n - 2) + counting(n - 3)
    return ways[n]

# OR:
# def get_mod_fib(n):
#     f1, f2, f3 = 1, 2, 4
#     for i in range(n-1):
#         f1, f2, f3 = f2, f3, f1 + f2 + f3
#     return f1


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    c = counting(n)
    # c = get_mod_fib(n)
    print("count", c)
    print("ways", ways)
