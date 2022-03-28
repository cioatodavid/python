cod1, num1, val1 = input().split()
cod2, num2, val2 = input().split()

val = (float(val1)*int(num1)) + (float(val2)*int(num2))
print(f'VALOR A PAGAR: R$ {val:.2f}')