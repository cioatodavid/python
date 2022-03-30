notas = list(map(float, input().split()))
exame = bool
notaf = (notas[0]*2 + notas[1]*3 + notas[2]*4 + notas[3])/10
print(f'Media: {notaf:.1f}')
if notaf < 5 and notaf >= 0:
    print("Aluno reprovado.")
elif notaf >= 5 and notaf < 7:
    print("Aluno em exame.")
    exame = True
elif notaf >= 7 and notaf <= 10:
    print("Aluno aprovado.")
        
if exame == True:
    notaexame = float( input())
    print(f"Nota do exame: {notaexame:.1f}")
    if notaf + notaexame /2 >= 5:
        print("Aluno aprovado.")
        
    else:
        print("Aluno reprovado.")
    print(f'Media final: {((notaf + notaexame)/2):.1f}')
        
