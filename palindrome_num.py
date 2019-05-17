
def isPalindrome(x):
    """
    :type x: int
    :rtype: int
    """
    print("x %s, y %s" % (str(x), str(x)[::-1]))
    return str(x) == str(x)[::-1]

a = -2147447412
b = 'powerrewop'
print(isPalindrome(a))
print(isPalindrome(b))
