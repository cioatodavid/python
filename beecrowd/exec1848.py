counter = 0
add = 0
def verify(crow):
    switcher = {
        'caw caw':'count',
        '--*' : 1,
        '-*-' : 2,
        '-**' : 3,
        '*--' : 4,
        '*-*' : 5,
        '**-' : 6,
        '***' : 7,
    }
    return switcher.get(crow)

while counter < 3:
    
    cur = input()
    if verify(cur) == 'count':
        print(add)
        counter += 1
        add = 0
    else:
        add += verify(cur)


        