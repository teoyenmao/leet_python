
# Too slow!!
# contacts = {}
# find_c = []
#
# def add(contact):
#     contacts[contact] = contact
#
# def find(search_contact):
#     ret = [k for k in contacts if k.startswith(search_contact)]
#     print("ret %s" % ret)
#     find_c.append(len(ret))

contacts = {}

def add(c):
    # generate all permutations in all chars to dict
    for i in range(len(c)):
        i += 1
        if not contacts.get(c[:i]):
            contacts[c[:i]] = [c]
        else:
            contacts[c[:i]].append(c)

def find(sc):
    ret = contacts.get(sc, [])
    print('find sc %s' % ret)
    print(len(ret))


# in: 4
#     add hack
#     add hackerrank
#     find hac
#     find hak
# out: 2
#      0

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    eval(op)(contact)

print("contacts %s" % contacts)
