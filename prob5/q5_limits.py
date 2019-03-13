"""
A python script to calculate values of the sequence of the limit
that represents e, and stop when there are 12 sig figs of similarity
"""
import numpy as np

# First, create vectors of n's and solutions
n_vector = []
soln = []

# Define function for f(n)
def f(n):
    return (1+(1/n))**n

# Now fill with initial values for n=1, n=10
n_vector.extend([1.0,10.0])
soln.extend([f(1.0),f(10.0)])

# Now we create a loop, starting from 10^1, to calculate values of this limit
#print(str(f(10))[:13])
#print("{:.11f}".format(f(10)))

n = 10
while "{:.13f}".format(soln[-1]) != "{:.13f}".format(soln[-2]):
    n *= 10
    n_vector.append(n)
    soln.append(f(n))
n_stop_log = int(np.log10(n_vector[-1]))
n_stop_num = soln[-1]

# Print results
dash = '-' * 35
print(dash)
title1 = f"The value of n_stop where 13 sig-fig convergence is achieved is 10^{n_stop_log-1}"
title2 = f"and 10^{n_stop_log}, with a final value of {n_stop_num}"
print(title1)
print(title2)

print(dash)
print('{:<20s}{:>4s}'.format("n","f(n)"))
print(dash)
for i in range(len(soln)):
    print('{:<20d}{:>4s}'.format(int(n_vector[i]),"{:.11f}".format(soln[i])))
    