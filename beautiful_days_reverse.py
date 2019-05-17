
def is_beautiful(i, j, k):
    b_list = []
    for v in range(i, j+1):
        reverse_v = int(str(v)[::-1])
        if abs(v - reverse_v) % k == 0:
            b_list.append(v)
    return b_list

i, j, k = input().strip().split(' ')

ret = is_beautiful(int(i), int(j), int(k))
# print("ret %s" % ret)
print(len(ret))
