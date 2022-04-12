def fastremainder(num, div):

    vec = []
    mod = 0

    for i in range(len(num)):
        digit = ord(num[i]) - ord('0')
        mod = mod * 10 + digit
        mod = mod % div

    return mod


x = input()
y = int(input())

print(fastremainder(x, y))
