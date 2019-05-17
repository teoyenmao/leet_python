# Keyword: Natural numbers / counting numbers: 1, 2, 3, 4, 5, ... (no zero)

def find_largest_permutation(arr, n, k):
    # TOO SLOW: O(n2)
    # # use selection sort
    # for i in range(0, len(arr) - 1):
    #     if k == 0:
    #         return arr, k
    #     max_val = i
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] > arr[max_val]:
    #             max_val = j
    #     if max_val != i:
    #         # swap
    #         arr[max_val], arr[i] = arr[i], arr[max_val]
    #         k -= 1

    # make a temp dict of arr index
    pos = {}
    for i in range(n):
        pos[arr[i]] = i

    for i in range(n):
        if k == 0:  # k is exhausted
            break
        max_val = n - i # i-th largest value (In natural nums, largest val = len(arr))
        if arr[i] == max_val:
            continue
        # swap in pos
        temp_i = pos[max_val]
        pos[max_val] = i
        pos[arr[i]] = temp_i
        # swap in arr
        arr[i], arr[temp_i] = arr[temp_i], arr[i]
        k -= 1
        # print("i", i)
        # print("arr",arr)
        # print("pos",pos)

    return arr, k

n, k = map(int, input().strip().split(' '))
array = [int(x) for x in input().strip().split(' ')]
l_permutation, k_left = find_largest_permutation(array, n, k)
print(' '.join(map(str, l_permutation)))
# print("l_permutation", l_permutation)
# print("k_left", k_left)
