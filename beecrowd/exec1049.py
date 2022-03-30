x = input()
if x == "vertebrado":
    y = input()
    if y == 'mamifero':
        z = input()
        if z == 'onivoro':
            print('homem')
        elif z == 'herbivoro':
            print('vaca')
    if y == 'ave':
        z = input()
        if z == 'onivoro':
            print('pomba')
        elif z == 'carnivoro':
            print('aguia')
if x == 'invertebrado':
    y = input()
    if y == 'inseto':
        z = input()
        if z == 'hematofago':
            print('pulga')
        elif z == 'herbivoro':
            print('lagarta')
    if y == 'anelideo':
        z = input()
        if z == 'hematofago':
            print('sanguessuga')
        elif z == 'onivoro':
            print('minhoca')
