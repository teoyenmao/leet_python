from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return repr((self.name, self.score))

    def comparator(a, b):
        if a.score == b.score:  # same score, sort by increasing alphabet order
            # print("B4 a {}, b {}, a<b? {}".format(a, b, a.name < b.name))
            # Note: The sort is mainly in reverse order
            #       if alphabet order is correct, 'keep' reverse order
            return -1 if a.name < b.name else 1
        return b.score - a.score   # maintain reverse score order


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)



# input
# 10
# ab 6
# bcc 0
# ade 5
# cab 2
# dee 0
# bda 2
# c 5
# db 2
# a 1
# cbb 1
#
# output
# ab 6
# ade 5
# c 5
# bda 2
# cab 2
# db 2
# a 1
# cbb 1
# bcc 0
# dee 0
