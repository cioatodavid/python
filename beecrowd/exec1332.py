n = int(input())

for i in range(n):
    word = str(input())
    if len(word) == 5:
        print(3)
    elif (word[0] == 't' and word[1] == 'w') or (word[0] == 't' and word[2] == 'o') or (word[1] == 'w' and word[2] == 'o'):
        print(2)
    else:
        print(1)
