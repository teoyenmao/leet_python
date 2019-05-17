def maximum_subarray(arr, n):
    max_so_far = 0
    max_end_here = 0
    start = 0; end = 0; s = 0;
    for i in range(len(arr)):
        max_end_here += arr[i]
        if max_end_here < 0:  # reset
            max_end_here = 0
            s = i + 1
        elif max_so_far < max_end_here: # record max_so_far
            max_so_far = max_end_here
            start = s
            end = i
    return max_so_far, start, end

a = [-2,1,-3,4,-1,2,1,-5,4]
output, s, e = maximum_subarray(a, len(a))
print("max %d, start %d, end %d" %(output, s, e))
