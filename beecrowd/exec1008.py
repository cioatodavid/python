num = int(input())
horas = int(input())
salhora = float(input())


def calcula(horas, salhora):
    sal = horas * salhora
    return sal


salar = calcula(horas, salhora)

print(f'NUMBER = {num}')
print(f'SALARY = U$ {salar:.2f}')
