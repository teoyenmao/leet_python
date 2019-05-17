def isPalindromePermutation(x):
    x = x.lower()           # lowercase
    y = x.replace(' ', '')  # remove all whitespace
    set_y = set(y)
    odd_amt = 0
    for char in set_y:
        count_char = y.count(char)
        if count_char % 2 == 1:
            odd_amt += 1
            if odd_amt > 1:
                print("odd_amt is > 1")
                return False
    print("odd_amt", odd_amt)
    return True   # Palindome only allows 1 odd character at most

val = input().strip()
r = isPalindromePermutation(val)
print(r)


# Input:
# powerrewop
# Tact Coa
