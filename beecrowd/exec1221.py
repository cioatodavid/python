n = int(input())


def is_prime(n):

    if n == 1:
        return 'Not Prime'
    i = 2
    while i*i <= n:
        if n % i == 0:
            return 'Not Prime'
        i += 1
    return 'Prime'


for i in range(n):
    print(is_prime(int(input())))
