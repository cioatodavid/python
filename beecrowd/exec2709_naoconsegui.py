def invertlist(l):
    return l[::-1]


def playagain():
    num = int(input())
    values = []
    finalvalue = 0
    for i in range(num):
        values.append(int(input()))

    jump = int(input())

    nvalue = invertlist(values)

    for j in range(0, num, jump):
        finalvalue += nvalue[j]

    print(finalvalue)
    return finalvalue


win = False
while win == False:
    try:

        final = playagain()
        if final % 2 == 0:
            print("Bad boy! I’ll hit you.")
        elif final % 2 != 0:
            print('''You’re a coastal aircraft, Robbie, a large silver aircraft.''')
            win = True
    except EOFError:
        break
