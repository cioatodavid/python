values = [4,6,1,2,5,6,1]

def getmin(values):
    min_value = min(values)
    return [i for i, x in enumerate(values) if x == min_value]
    
def removemin(lista):
    if len(lista) > 1 :
        lista.pop(max(lista))
    else:
        lista.pop()
    
    return lista

minlist = getmin(values)
print()
        

