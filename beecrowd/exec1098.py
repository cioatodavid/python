j1,j2,j3 = 1,2,3
iall = 0.0
for i in range(11):
    iall = round(iall,1)
    if iall == 0.0 or iall == 1.0 or iall == 2.0:
       if j1 == 1.0 or j1 == 2.0 or j1 == 3.0:
            print(f'I={iall:.0f} J={j1:.0f}')
            print(f'I={iall:.0f} J={j2:.0f}')
            print(f'I={iall:.0f} J={j3:.0f}')
            iall += 0.2
            j1,j2,j3 = 1+iall,2+iall,3+iall
       else:
            print(f'I={iall:.0f} J={j1:.1f}')
            print(f'I={iall:.0f} J={j2:.1f}')
            print(f'I={iall:.0f} J={j3:.1f}')
            iall += 0.2
            j1,j2,j3 = 1+iall,2+iall,3+iall
    else:
        if j1 == 1.0 or j1 == 2.0 or j1 == 3.0:
            print(f'I={iall:.1f} J={j1:.0f}')
            print(f'I={iall:.1f} J={j2:.0f}')
            print(f'I={iall:.1f} J={j3:.0f}')
            iall += 0.2
            j1,j2,j3 = 1+iall,2+iall,3+iall
        else:
            print(f'I={iall:.1f} J={j1:.1f}')
            print(f'I={iall:.1f} J={j2:.1f}')
            print(f'I={iall:.1f} J={j3:.1f}')
            iall += 0.2
            j1,j2,j3 = 1+iall,2+iall,3+iall
        
        