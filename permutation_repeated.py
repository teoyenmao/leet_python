
def permutation_recur(string, result, last, index):
    for i in range(len(string)):
        result[index] = string[i]
        if index == last:
            print(''.join(result))
        else:
            permutation_recur(string, result, last, index+1)

def permutation_repeated(string):
    n = len(string)
    result = [''] * n
    permutation_recur(string, result, n-1, 0)


input_string = 'abc'
permutation_repeated(input_string)
