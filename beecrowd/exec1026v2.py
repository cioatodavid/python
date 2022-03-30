while True:
    try:
        x, y = map(int, (input().split()))

        final = x ^ y

        print(final)

    except EOFError:
        break
