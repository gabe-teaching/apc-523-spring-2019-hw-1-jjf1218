#%%
import numpy as np
import math
import scipy.integrate as integrate

#%%

kfact=math.factorial(20.0)
eps = 2.0**(-52.0)
val=kfact/eps

guess_N=math.factorial(31.0)

#print("value:")
#print('{:<20f}'.format(val))
#print("N!:")
#print('{:<20f}'.format(guess_N))

if guess_N > val:
    print("try again, N! > k!/eps")
    
#%%

#Backward recurrence relation, y_(N-1)=(e-y_N)/N
#want to find y_20, start with y_N=0

N_start = 31
y_next = np.exp(1.0)/N_start
print("\nStarting value: ",y_next)
N = N_start - 1
while N>20:
    y_next = (np.exp(1.0)-y_next)/N
    print("For N = ",N,", then y_next = ",y_next)
    N -= 1
    
#%% Some other integration routines

result = integrate.quad(lambda x: (x**20)*(np.exp(x)),0.0,1.0)
print("\nThe result of integrate.quad: ",result[0])