l = int(input())
c = int(input())

if l%2 == 0 and c%2 != 0:
    print(0)
elif l%2 != 0 and c%2 == 0:
    print(0)
elif l == c:
    print(1)
elif l%2 == 0 and c%2 == 0:
    print(1)
elif l%2 != 0 and c%2 != 0:
    print(1)