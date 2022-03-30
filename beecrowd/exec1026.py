def int2binary(n):
    s = ''
    i = 0
    while(i < 32):
        if n & 1 == 1:
            s = '1' + s
        else:
            s = '0' + s
        n = n >> 1
        i += 1
    return s


def binary2int(s):
    n = 0
    i = 0
    while(i < 32):
        if s[i] == '1':
            n += 1 << (31 - i)
        i += 1
    return int(n)


def str2list(s):
    l = []
    for i in s:
        l.append(i)
    return l


def list2str(l):
    s = ''
    for i in l:
        s += i
    return s


def listscompare(list1, list2):
    i = 0
    listsum = []
    while(i < len(list1)):
        if list1[i] == list2[i]:
            listsum.append('0')
            i += 1
        elif list1[i] > list2[i]:
            listsum.append(list1[i])
            i += 1
        else:
            listsum.append(list2[i])
            i += 1
    return listsum


while True:
    try:
        x, y = map(int, input().split())
        x, y = int2binary(x), int2binary(y)
        x, y = str2list(x), str2list(y)
        xy = listscompare(x, y)
        xys = list2str(xy)
        final = binary2int(xys)
        print(final)

    except EOFError:
        break
