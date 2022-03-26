A = float(input())
B = float(input())
C = float(input())

def calcmedia(A, B, C):
    return (A*2 + B*3 + C*5)/10

print(f"MEDIA = {calcmedia(A, B, C):.1f}")