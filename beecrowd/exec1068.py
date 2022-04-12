while True:
    try:
        string = input()
        balance = 0
        for i in range(len(string)):
            if(string[i] == '('):
                balance += 1
            elif(string[i] == ')'):
                balance -= 1
            if(balance < 0):
                break
        if(balance != 0):
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break
