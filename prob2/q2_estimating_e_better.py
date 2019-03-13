import numpy as np
from math import exp
dash = '-' * 30
def rd(x):
    return float(('%.5g'%x))

#list for storing variables for d

#parta
print("\n")
print("--------For parts a & b-------")
print("%02s | %10s  | %10s"%("n", "nth term", "S_n"))
print(dash)
num = 1.0 #5.5^0
den = 1.0 #0!
sum1 = rd(num/den)
print("%02d | %10s  | %10s"%(0, 1, 1))
for n in range(1,31):
    num = rd((5.5)**(n))
#    print(num)
    den = rd(den*n)
#    print(den)
    div = rd(num/den)
#    print(sum1)
    sum1 += rd(div)
    sum1 = rd(sum1)
#    print(sum1)
    print("%02d | %10s  | %10s"%(n, div, sum1))

#partc
print("\n")
print("----------For part c--------")
print("%02s | %10s  | %10s"%("n", "nth term", "S_n"))
print(dash)
num = 1.0 #5.5^0
den = 1.0 #0!
sum1 = rd(num/den)
print("%02d | %10s  | %10s"%(0, 1, 1))
for n in range(1,31):
    num = rd((5.5)**(n))
#    print(num)
    den = rd(den*n)
#    print(den)
    div = rd(num/den)
#    print(sum1)
    sum1 = rd(div) + sum1
    sum1 = rd(sum1)
#    print(sum1)
    print("%02d | %10s  | %10s"%(n, div, sum1))    
    
#partd
#we need a list of values for d
num = 1.0 #5.5^0
den = 1.0 #0!
d_list = [1.0]
sum1 = rd(num/den)
print("%02d | %14s  | %10s"%(0, 1, 1))
for n in range(1,31):
    num = rd((5.5)**(n))
    den = rd(den*n)
    div = rd(num/den)
    if n%2==0:
        pass
    else:
        div = div*-1.0
    d_list.append(div)
    sum1 = rd(sum1 + rd(div))
    print("%02d | %14s  | %10s"%(n, div, sum1)) 

