#%% ===========================================================================
# A script to look at Wilkinson's Polynomial and conducting an error analysis
# =============================================================================

#%% Import libraries
import numpy as np
#from sympy import *
import sympy as sm
from scipy import optimize
import numpy.polynomial.polynomial as poly

#%% First find coefficients using the CAS-like sympy
x = sm.Symbol('x')
W = 1
for i in range(1, 21):
    W *= (x-i)
print("\nWilkinson's polynomial for k=20:")
print("    "+str(W.expand()))

#%% Here are the coefficients
a20 = 1.0
a19 = -210.0
a18 = 20615.0
a17 = -1256850.0
a16 = 53327946.0
a15 = -1672280820.0
a14 = 40171771630.0
a13 = -756111184500.0
a12 = 11310276995381.0
a11 = -135585182899530.0
a10 = 1307535010540395.0
a9 = -10142299865511450.0
a8 = 63030812099294896.0
a7 = -311333643161390640.0
a6 = 1206647803780373360.0
a5 = -3599979517947607200.0
a4 = 8037811822645051776.0
a3 = -12870931245150988800.0
a2 = 13803759753640704000.0
a1 = -8752948036761600000.0
a0 = 2432902008176640000.0

# We will store these coefficients in a list
wilk_coeffs = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,\
               a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]

# %%===========================================================================
# Now that we have a list of coefficients, we can evaluate this as interger or
# float values, and see what kinds of numerical errors we get. We will also
# look at root-finding methods to see errors in this as well.
# =============================================================================

#%% Evaluating the function as integers or floats

#Defining the function using the integer coefficients obtained from Sympy
def w_int(y):
    return y**20 - 210*y**19 + 20615*y**18 - 1256850*y**17 + 53327946*y**16 - \
           1672280820*y**15 + 40171771630*y**14 - 756111184500*y**13 + \
           11310276995381*y**12 - 135585182899530*y**11 + 1307535010540395*y**10 - \
           10142299865511450*y**9 + 63030812099294896*y**8 - 311333643161390640*y**7 + \
           1206647803780373360*y**6 - 3599979517947607200*y**5 + \
           8037811822645051776*y**4 - 12870931245150988800*y**3 + \
           13803759753640704000*y**2 - 8752948036761600000*y + 2432902008176640000
# Testing out a few values/roots at integer values
print("\nSome values for w_int(x):")
print("    w_int(0)="+str(w_int(0)),"w_int(1)="+str(w_int(1)),"w_int(3)="+str(w_int(3)),"w_int(17)="+str(w_int(17)))

# same function as above, but all coefficients are floats insted of ints
def w(y):
    return y**20.0 - 210.0*y**19 + 20615.0*y**18 - 1256850.0*y**17 + 53327946.0*y**16 - \
           1672280820.0*y**15 + 40171771630.0*y**14 - 756111184500.0*y**13 + \
           11310276995381.0*y**12 - 135585182899530.0*y**11 + 1307535010540395.0*y**10 - \
           10142299865511450.0*y**9 + 63030812099294896.0*y**8 - 311333643161390640.0*y**7 + \
           1206647803780373360.0*y**6 - 3599979517947607200.0*y**5 + \
           8037811822645051776.0*y**4 - 12870931245150988800.0*y**3 + \
           13803759753640704000.0*y**2 - 8752948036761600000.0*y + 2432902008176640000.0
# Testing out a few values/roots at float values
print("Some values for w(x):")
print("    w(0)="+str(w(0.0)),"w(1)="+str(w(1.0)),"w(3)="+str(w(3.0)),"w(17)="+str(w(17.0)))


#%% Something is wonky - now let's try a few root-finding methods
print("\nHighest roots w(x) (should be close to 20.0):")
# Now try to find roots using Newton-Raphson
root_nr = optimize.newton(w, 21)
print("    The highest root using NR (guess of 21) is "+str(root_nr))
# Now try to find roots using poly.polyroots
root_pr = poly.polyroots(wilk_coeffs)
print("    The highest root using poly.polyroots is ",max(root_pr))
# Now try to find roots using np.root
root_np = np.roots(list(reversed(wilk_coeffs)))
print("    The highest root using np.roots is ",max(root_np))

# Error analysis of the three methods above
def err(actual,measured):
    return abs((measured-actual)/(actual))
err_nr = err(20.0,root_nr);err_pr=err(20.0,max(root_pr));err_np=err(20.0,max(root_np))
errors = [err_nr, err_pr, err_np]
print("\nSome error analysis:")
print("    The error using NR is",err_nr)
print("    The error using poly.polyroots is",err_pr)
print("    The error using np.roots is",err_np)
print("So the lowest relative error is ",min(errors))

#%% Now we want to perturb the initial value 20 from 1 to 1+delta
delta = [10.0**-8, 10.0**-6, 10.0**-4, 10.0**-2]
for d in delta:
    print("\n------------- For delta =",d,"-------------")
    wilk_coeffs_pert = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,\
               a11, a12, a13, a14, a15, a16, a17, a18, a19, (a20+d)]
    def w_pert(y):
        return y**20.0 - 210.0*y**19 + 20615.0*y**18 - 1256850.0*y**17 + 53327946.0*y**16 - \
           1672280820.0*y**15 + 40171771630.0*y**14 - 756111184500.0*y**13 + \
           11310276995381.0*y**12 - 135585182899530.0*y**11 + 1307535010540395.0*y**10 - \
           10142299865511450.0*y**9 + 63030812099294896.0*y**8 - 311333643161390640.0*y**7 + \
           1206647803780373360.0*y**6 - 3599979517947607200.0*y**5 + \
           8037811822645051776.0*y**4 - 12870931245150988800.0*y**3 + \
           13803759753640704000.0*y**2 - 8752948036761600000.0*y + (2432902008176640000.0+d)
    # Now try to find roots using Newton-Raphson
    root_nr = optimize.newton(w_pert, 21)
    print("    The highest root using NR (guess of 21) is "+str(root_nr))
    # Now try to find roots using poly.polyroots
    root_pr = poly.polyroots(wilk_coeffs_pert)
    print("    The highest root using poly.polyroots is ",max(root_pr))
    # Now try to find roots using np.root
    root_np = np.roots(list(reversed(wilk_coeffs_pert)))
    print("    The highest root using np.roots is ",max(root_np))

    # Error analysis of the three methods above
    err_nr = err(20.0,root_nr);err_pr=err(20.0,max(root_pr));err_np=err(20.0,max(root_np))
    errors = [err_nr, err_pr, err_np]
    print("Some error analysis for d = ",d,":")
    print("    The error using NR is",err_nr)
    print("    The error using poly.polyroots is",err_pr)
    print("    The error using np.roots is",err_np)
    print("So the lowest relative error is ",min(errors))
    
#%% Now we want to perturb the second term, a19
    
delta = [10.0**-8, 10.0**-6, 10.0**-4, 10.0**-2]
a19p = -210.0-2**(-23.0)
print("\n------------- For a19 = -210-2^-23-------------")
wilk_coeffs_pert2 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,\
           a11, a12, a13, a14, a15, a16, a17, a18, a19p, a20]
def w_pert2(y):
    return y**20.0 - 210.0*y**19 + 20615.0*y**18 - 1256850.0*y**17 + 53327946.0*y**16 - \
       1672280820.0*y**15 + 40171771630.0*y**14 - 756111184500.0*y**13 + \
       11310276995381.0*y**12 - 135585182899530.0*y**11 + 1307535010540395.0*y**10 - \
       10142299865511450.0*y**9 + 63030812099294896.0*y**8 - 311333643161390640.0*y**7 + \
       1206647803780373360.0*y**6 - 3599979517947607200.0*y**5 + \
       8037811822645051776.0*y**4 - 12870931245150988800.0*y**3 + \
       13803759753640704000.0*y**2 - a19p*y + 2432902008176640000.0
# Now try to find roots using Newton-Raphson
root_nr = optimize.newton(w_pert, 21)
print("    The highest root using NR (guess of 21) is "+str(root_nr))
# Now try to find roots using poly.polyroots
root_pr = poly.polyroots(wilk_coeffs_pert)
print("    The highest root using poly.polyroots is ",max(root_pr))
# Now try to find roots using np.root
root_np = np.roots(list(reversed(wilk_coeffs_pert)))
print("    The highest root using np.roots is ",max(root_np))

# Error analysis of the three methods above
err_nr = err(20.0,root_nr);err_pr=err(20.0,max(root_pr));err_np=err(20.0,max(root_np))
errors = [err_nr, err_pr, err_np]
print("Some error analysis for d = ",d,":")
print("    The error using NR is",err_nr)
print("    The error using poly.polyroots is",err_pr)
print("    The error using np.roots is",err_np)
print("So the lowest relative error is ",min(errors))    
    
#%% Now we want to calculate the derivative of w(x)

print("\nThe derivative of Wilkinson's polynomial for k=20:")
w_prime = sm.diff(W.expand(), x)
print(w_prime,"\n")

def w_prime_func(x):
    return 20*x**19 - 3990*x**18 + 371070*x**17 - 21366450*x**16 + \
    853247136*x**15 - 25084212300*x**14 + 562404802820*x**13 - \
    9829445398500*x**12 + 135723323944572*x**11 - 1491437011894830*x**10 + \
    13075350105403950*x**9 - 91280698789603050*x**8 + \
    504246496794359168*x**7 - 2179335502129734480*x**6 + \
    7239886822682240160*x**5 - 17999897589738036000*x**4 + \
    32151247290580207104*x**3 - 38612793735452966400*x**2 + \
    27607519507281408000*x - 8752948036761600000

#print(w_prime_func(0))

#%% Now that we have the derivative, we will calculate condition numbers
# We need the coefficients a_n, which are wilk_coeffs from above
# We also need the roots, phi_k
phi_f = list(np.arange(1.0,21.0))
phi = list(range(1,21))

def cond_num(k):
    cond_sum = 0
    for l in range(len(wilk_coeffs)):
        cond = abs((wilk_coeffs[l]*k**(l-1))/(w_prime_func(k)))
        cond_sum += cond
    return cond_sum
roots = [14,16,17,20]
for r in roots:
    print("Condition number for root r = ",r," = ",cond_num(r))



