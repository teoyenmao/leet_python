# Complete the function below.

def  oddNumbers(l, r):
  return [i for i in range(l, r+1) if i%2]


l = 3
r = 9
print(oddNumbers(l, r))
