from collections import defaultdict

def ransom_note(magazine, ransom):
    if len(magazine) < len(ransom):
        return False

    # Spent too much time!!
    # magazine_dict = {x: magazine.count(x) for x in magazine}      <- stupid O(n^2)
    # ransom_dict = {y: ransom.count(y) for y in ransom}            <- stupid O(n^2)
    # result = [(i, j) for i, j in magazine_dict.items()
    #           if i in ransom_dict and j >= ransom_dict[i]]
    # print("result: %d, ransom_dict: %d" % (len(result), len(ransom_dict)))
    # return len(result) == len(ransom_dict)

    # Still too slow
    # ransom_dict = {x: ransom.count(x) for x in ransom}            <- stupid O(n^2)
    # for c in magazine:
    #     v = ransom_dict.get(c)
    #     if v is not None:   # found word
    #         if v > 0:
    #             ransom_dict[c] = v - 1
    #         else:
    #             if all(i == 0 for i in ransom_dict.values()):
    #                 return True
    #             continue
    # # make sure all
    # return all(i == 0 for i in ransom_dict.values())

    def_dict = defaultdict(int)
    for c in magazine:
        def_dict[c] += 1
    for c in ransom:
        if def_dict[c] == 0:    # not found or no more in def_dict
            return False
        def_dict[c] -= 1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
