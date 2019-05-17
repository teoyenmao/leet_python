def isSubstring(x, y):
    return x in y

def isStringRotation(s1, s2):
    if len(s1) == len(s2) == 0:
        return False

    # Check rotation: to identify xy, can use yxyx to check isSubstring
    chk_s1 = s1 + s1
    return isSubstring(s2, chk_s1)


input_str1 = input().strip()
input_str2 = input().strip()
print("string rotation:", isStringRotation(input_str1, input_str2))



# Input:
# waterbottle erbottlewat
