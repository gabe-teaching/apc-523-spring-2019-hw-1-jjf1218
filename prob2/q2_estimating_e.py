# =============================================================================
# A code to estimate e using 5 sig figs for every operation
# =============================================================================
import numpy as np
from math import exp
dash = '-' * 30
def rd(x):
    return float(('%.5g'%x))

#%% Parts (a) and (b)
numa = '%.5g' % (1.0,)
dena = '%.5g' % (1.0,)
suma = '%.5g' % (1.0,)
print("\n")
print("--------For parts a & b-------")
print("%02s | %10s  | %10s"%("n", "nth term", "S_n"))
print(dash)
print("%02d | %10s  | %10s"%(0, 1, 1))
suma_list = [numa]
for n in range(0, 30):
    for i in range(n,n+1):
        numa = float(numa)*float('%.5g' % (5.5,))
        dena = float(dena)*float('%.5g' % (n+1,))
        numa =  '%.5g'%numa
        dena =  '%.5g'%dena
    div = float(numa)/float(dena)
    div = '%.5g'%div
    suma = float(suma) + float(div)
    suma = '%.5g'%suma
    suma_list.append(div)
    print("%02d | %10s  | %10s"%(n+1, div, suma))

print("\n")
err = abs((np.exp(5.5) - float(suma))/exp(5.5))
print("The actual value is ", exp(5.5))
print("The 5 mantissa value is ", float(suma))
print("The difference is ", (exp(5.5) - float(suma)))
print("The error is ", err*100)

# Part (c) - right
print("\n")
print("----------For part c----------")
print("%02s | %10s  | %10s"%("n", "nth term", "S_n"))
print(dash)
sum_count = float(suma_list[i])
for i in range(len(suma_list)):
    next_sum = float(suma_list[i]) + float(sum_count)
    next_sum = '%.5g'%next_sum
    sum_count = next_sum
    print("%02d | %10s  | %10s"%(i, suma_list[i], next_sum))

print("\n")
err = abs((np.exp(5.5) - float(next_sum))/exp(5.5))
print("The actual value is ", exp(5.5))
print("The 5 mantissa value is ", float(next_sum))
print("The difference is ", (exp(5.5) - float(next_sum)))
print("The error is ", err*100)


#%% Part (d)
numdi = '%.5g' % (1.0,)
dendi = '%.5g' % (1.0,)
sumdi = '%.5g' % (1.0,)
sumdi_list = [numdi]
for n in range(0, 30):
    for i in range(n,n+1):
        numdi = float(numdi)*float('%.5g' % (5.5,))
        dendi = float(dendi)*float('%.5g' % (n+1,))
        numdi =  '%.5g'%numdi
        dendi =  '%.5g'%dendi
    div = float(numdi)/float(dendi)
    if n%2==0:
        div  = (-1.0)*div
    div = '%.5g'%div
    suma = float(sumdi) + float(div)
    suma = '%.5g'%suma
    sumdi_list.append(div)
#print(sumdi_list)
d_list = sumdi_list
dash = '-' * 35

## We now have d_list for the parts of d

#%%Part (d)(i), left to right
print("\n")
print("------------For part d(i)----------")
print("%02s | %14s  | %10s"%("n", "nth term", "S_n"))
print(dash)
sum_d1 = '%.5g' % (0.0)
for i in range(len(d_list)):
    sum_d1 = float(sum_d1) + float(d_list[i])
    sum_d1 = '%.5g'%sum_d1
    print("%02d | %14s  | %10s"%(i, sumdi_list[i], sum_d1))
    
print("\n")
err = abs((np.exp(-5.5) - float(sum_d1))/exp(-5.5))
print("The actual value is ", exp(-5.5))
print("The 5 mantissa value is ", float(sum_d1))
print("The difference is ", (exp(-5.5) - float(sum_d1)))
print("The error is ", err*100)

#%%Part (d)(ii), right to left
print("\n")
print("------------For part d(ii)---------")
print("%02s | %14s  | %10s"%("n", "nth term", "S_n"))
print(dash)

sum_d1 = '%.5g' % (0.0)
for i in range(len(sumdi_list[0:][-1::-1])):
    sum_d1 = float(sum_d1) + float(d_list[i])
    sum_d1 = '%.5g'%sum_d1
    print("%02d | %14s  | %10s"%(i, sumdi_list[i], sum_d1))

    
print("\n")
err = abs((np.exp(-5.5) - float(sum_d1))/exp(-5.5))
print("The actual value is ", exp(-5.5))
print("The 5 mantissa value is ", float(sum_d1))
print("The difference is ", (exp(-5.5) - float(sum_d1)))
print("The error is ", err*100)

#%%Part (d)(iii), positive left to right, negative left to right, combine
print("\n")
print("------------For part d(iii)--------")
print("%02s | %14s  | %10s"%("n", "nth term", "S_n"))
print(dash)

sum_pos = "1.0"
sum_neg = "-5.5"
for i in range(2,len(sumdi_list)):
    if float(sumdi_list[i]) > 0:
        next_sum1 = float(sumdi_list[i]) + float(sum_pos)
        next_sum1 = '%.5g'%next_sum1
        sum_pos = next_sum1
        print("%02d | %14s  | %10s"%(i, sumdi_list[i], next_sum1))
    elif float(sumdi_list[i]) < 0:
        next_sum2 = float(sumdi_list[i]) + float(sum_neg)
        next_sum2 = '%.5g'%next_sum2
        sum_neg = next_sum2
        print("%02d | %14s  | %10s"%(i, sumdi_list[i], next_sum2))

#now combine results
sum_tot = float(sum_pos) + float(sum_neg)
sum_tot = '%.5g'%sum_tot
print("\n")
err = abs((np.exp(-5.5) - float(sum_tot))/exp(-5.5))
print("The actual value is ", exp(-5.5))
print("The 5 mantissa value is ", float(sum_tot))
print("The difference is ", (exp(-5.5) - float(sum_tot)))
print("The error is ", err*100)

#%%Part (d)(iv), positive right to left, negative right to left, combine
print("\n")
print("------------For part d(iv)---------")
print("%02s | %14s  | %10s"%("n", "nth term", "S_n"))
print(dash)

sum_pos = "1.0"
sum_neg = "-5.5"
for i in range(2,len(sumdi_list)):
    if float(sumdi_list[i]) > 0:
        next_sum1 =  float(sum_pos) + float(sumdi_list[i])
        next_sum1 = '%.5g'%next_sum1
        sum_pos = next_sum1
        print("%02d | %14s  | %10s"%(i, suma_list[i], next_sum1))
    elif float(sumdi_list[i]) < 0:
        next_sum2 = float(sum_neg) + float(sumdi_list[i])
        next_sum2 = '%.5g'%next_sum2
        sum_neg = next_sum2
        print("%02d | %14s  | %10s"%(i, suma_list[i], next_sum2))

#now combine results
sum_tot = float(sum_pos) + float(sum_neg)
sum_tot = '%.5g'%sum_tot
print("\n")
err = abs((np.exp(-5.5) - float(sum_tot))/exp(-5.5))
print("The actual value is ", exp(-5.5))
print("The 5 mantissa value is ", float(sum_tot))
print("The difference is ", (exp(-5.5) - float(sum_tot)))
print("The error is ", err*100)


