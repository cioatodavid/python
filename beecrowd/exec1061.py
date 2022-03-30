d, day1 = input().split()
day1 = int(day1)
h1, m1, s1 = map(int, input().replace(':', '').split())
d, day2 = input().split()
day2 = int(day2)
h2, m2, s2 = map(int, input().replace(':', '').split())


def time_diff(day1, h1, m1, s1, day2, h2, m2, s2):
    s = s2 - s1
    m = m2 - m1
    h = h2 - h1
    d = day2 - day1
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h += 24
        d -= 1
    return d, h, m, s


day, hour, minute, second = time_diff(day1, h1, m1, s1, day2, h2, m2, s2)
print(f'{day} dia(s)')
print(f'{hour} hora(s)')
print(f'{minute} minuto(s)')
print(f'{second} segundo(s)')
