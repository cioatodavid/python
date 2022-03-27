while True:
    try:
        x, y, m = map(int, input().split())

        for i in range(m):

            xc, yc = map(int, input().split())

            if xc <= x and yc <= y or xc <= y and yc <= x:
                print("Sim")
            else:
                print("Nao")

    except EOFError:
        break
