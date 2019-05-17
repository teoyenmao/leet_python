l = []

l_cmd = {'insert': l.insert,
         'remove': l.remove,
         'append': l.append,
         'sort': l.sort,
         'pop': l.pop,
         'reverse': l.reverse}

if __name__ == '__main__':
    N = int(input())
    for m in range(N):
        cmd_in = input().split(' ')
        if len(cmd_in) == 1:
            cmd_in = cmd_in[0]
            if cmd_in == 'print':
                print(l)
            else:
                l_cmd[cmd_in]()
        else:
            args = [int(v) for v in cmd_in[1:]]
            l_cmd[cmd_in[0]](*args)
