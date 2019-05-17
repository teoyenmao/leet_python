def swap(i, j):
    array_list[i], array_list[j] = array_list[j], array_list[i]

def max_heapify(end, i):
    max_v = i
    l = 2 * i + 1
    r = 2 * i + 2
    # compare left & right node
    if l < end and array_list[l] > array_list[max_v]:  # left node > root
        max_v = l
    if r < end and array_list[r] > array_list[max_v]:  # right node > root
        max_v = r
    if max_v != i:
        swap(i, max_v)
        max_heapify(end, max_v)

def heap_sort():
    end = len(array_list)
    # build heap
    start = end // 2 - 1  # get mid point, //: divide to get int only
    for i in range(start, -1, -1):
        max_heapify(end, i)
    for i in range(end - 1, -1, -1):
        swap(i, 0)        # swap root & end node
        max_heapify(i, 0)


#### test code

array_list = [2, 7, 1, -2, 56, 5, -4, 99, 10, 6]
print("before: ", array_list)
heap_sort()
print("after: ", array_list)
