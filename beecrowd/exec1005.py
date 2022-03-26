A = float(input())
B = float(input())

def calcmedia(A, B):
    return (A*3.5 + B*7.5)/11

print(f"MEDIA = {calcmedia(A, B):.5f}")