
map_b = {'{': '}', '[':']', '(': ')'}

def is_matched(expression):
    chk_b = ''
    pivot_lb = ''
    for b in expression:
        # print("%s" % b)
        if b in map_b.keys():   # left
            pivot_lb = b
            chk_b += b
        elif b in map_b.values():   # right
            if map_b.get(pivot_lb) != b:
                return False
            chk_b = chk_b[:-1]
            if chk_b:
                pivot_lb = chk_b[-1]

    return chk_b == ''


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")


# in:
# 5
# }][}}(}][))]
# [](){()}
# ()
# ({}([][]))[]()
# {)[](}]}]}))}(())(
#
# out:
# NO
# YES
# YES
# YES
# NO
