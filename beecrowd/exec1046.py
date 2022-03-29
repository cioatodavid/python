ini, fim = map(int,input().split())

if ini > fim:
    time = (ini - fim) - 24
    if time < 0:
        time = time * -1
    print(f'O JOGO DUROU {time} HORA(S)')
elif ini == fim:
    print('O JOGO DUROU 24 HORA(S)')
elif ini < fim:
    time = fim - ini
    print(f'O JOGO DUROU {time} HORA(S)')

