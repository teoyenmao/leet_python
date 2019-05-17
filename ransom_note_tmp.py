from collections import defaultdict


def ransom_note(magazine, ransom):
    # make magazine to hash dict
    magazine_dict = defaultdict(int)
    for w in magazine:
        magazine_dict[w] += 1
    print(magazine_dict)

    for w in ransom:
        if magazine_dict[w] == 0:
            return False
        magazine_dict[w] -= 1
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
