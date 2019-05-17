
def viral_ad(n):

    p_like = 0

    p_recv = 5
    for d in range(n):
        pl = int(p_recv/2)
        # print("pl %d" % pl)
        p_like += pl
        p_recv = pl * 3
        # print("next p_recv %d" % p_recv)

    return p_like


n = int(input().strip())
ppl_like = viral_ad(n)
# print("ppl_like %s" % ppl_like)
print(ppl_like)


# in: 3
# out: 9
