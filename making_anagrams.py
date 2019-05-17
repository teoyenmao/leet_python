
def number_needed(a, b):
    # la = list(a)
    # lb = list(b)
    # for x in la[:]:
    #     for y in lb[:]:
    #         if x == y:
    #             la.remove(x)
    #             lb.remove(y)
    # print("la %s" % la)
    # print("lb %s" % lb)
    # return len(la) + len(lb)


    # list an alphabet array
    # count each alphabet in a, then deduct counts in b
    # sum up left over
    freq = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
    ret = 0
    for i in freq:
        amt = abs(a.count(i) - b.count(i))
        freq[i] = amt
        ret += amt

    return ret


# in: fsqoiaidfaukvngpsugszsnseskicpejjvytviya
#     ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget
# out: 42

a = input().strip()
b = input().strip()

print(number_needed(a, b))
