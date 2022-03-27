nome = str(input())
salario = float(input())
montante = float(input())


def calcula(salario, montante):
    sal = salario + (montante * 0.15)
    return sal


print(f'TOTAL = R$ {calcula(salario, montante):.2f}')
