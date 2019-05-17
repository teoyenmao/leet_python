arr = [5,1,4,6,1]


x = 6, y = 1
d = 0, min = 0
for i in range(arr):
  if a == arr[i]:
    x = i
  if b == arr[i]:
    y = i
  d = x - y
  d = d if d > 0 else y - x

  if d < min:
    min = d
