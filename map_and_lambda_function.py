#!/bin/python3


cube = lambda x: x ** 3 # complete the lambda function

# METHOD 1
# def fibonacci(n):
#     # return a list of fibonacci numbers
#     return [_fibonacci(i) for i in range(n)]
#
# def _fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return _fibonacci(n-1) + _fibonacci(n-2)

# METHOD 2
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    #n = int(input())
    n = 5
    print(list(fibonacci(n)))
    print(list(map(cube, fibonacci(n))))
