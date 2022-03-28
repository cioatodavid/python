n = int(input())

l1 = ['o', 'n', 'e']
l2 = ['t', 'w', 'o']
note1 = 0
note2 = 0

for i in range(n):
    word = input()
    if len(word) == 3:
        for j in range(3):
            if word[j] in l1[j]:
                note1 += 1
            if word[j] in l2[j]:
                note2 += 1
        if note1 > note2:
            print(1)
        else:
            print(2)
    elif len(word) == 5:
        print(3)
