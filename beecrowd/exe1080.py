array = [0] * 100

for i in range(100):
    x = int(input())
    array[i] = x
mval = max(array)
mind = array.index(mval)
print(mval)
print(mind+1)