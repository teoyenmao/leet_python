n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

sort_count = 0

for k in range(n - 1):
    sorted = True
    for i in range(n - k - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            sort_count += 1
            sorted = False
    if sorted:
        break

print("Array is sorted in %d swaps." % sort_count)
print("First Element:", a[0])
print("Last Element:", a[n - 1])



# input
# 3
# 3 2 1
#
# 4
# 1 2 3 4
