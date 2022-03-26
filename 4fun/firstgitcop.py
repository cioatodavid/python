def daystoyearmonthdays(days):
    year = days // 365
    month = (days % 365) // 30
    day = (days % 365) % 30
    return year, month, day

days= int(input())
year, month, day = daystoyearmonthdays(days)
print(year,'ano(s)')
print(month,'mes(es)')
print(day,'dia(s)')