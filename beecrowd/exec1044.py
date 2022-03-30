a,b = map(int, input().split())
def ismultiple(a,b):
    if a%b == 0:
        return True
    else:
        return False
if a > b:
    if ismultiple(a,b):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if ismultiple(b,a):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')