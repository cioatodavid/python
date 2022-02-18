import math

cat_op = int(input('cat oposto: '))

cat_ad = int(input('cat adj: '))
res_hip = math.sqrt(cat_ad**2 + cat_op**2)
print("a hipotenusa é {:.1f}".format(res_hip))