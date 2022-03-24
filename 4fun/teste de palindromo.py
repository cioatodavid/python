
txtStr = input('Escreva algo para descobrir se é um palíndromo! : ')
txtStr = txtStr.lower()
txtStr = txtStr.replace(' ','')
txtInvert = txtStr[::-1]

if txtStr == txtInvert:
    print(f"{txtInvert} é um palíndromo!")
else:
    print(f"Ops, {txtStr} não é um palíndromo")


    