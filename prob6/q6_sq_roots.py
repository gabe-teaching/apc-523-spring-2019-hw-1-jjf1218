# =============================================================================
# A python script to look at error analysis in taking a square root n-time and
# then squaring n-times.
# =============================================================================
#%%
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(1.0,10.0,1001)
y_values = np.linspace(1.0,10.0,1001)

# Change amount of times to square root and square values
n_time = 50

#%%
i = 0
while i<(n_time):
    y_values = np.sqrt(y_values)
    i += 1

i = 0
while i<(n_time):
    y_values = (y_values)**2
    i += 1

plt.scatter(x_values,y_values,s=1,c="g")
plt.plot(x_values,x_values,"k")
title = f"Square-Rooting and Squaring values {n_time} times"
plt.title(title)
save_string = f'square_root_fig_{n_time}.png'
plt.savefig("sqrtfigsnew/" + save_string)

#%% Let's figure out why only certain values are getting back to themselves
special_values_x = []
special_values_y = []
for j in (range(len(y_values))):
    if y_values[j] == y_values[j-1]:
        pass
    else:
        special_values_x.append(x_values[j])
        special_values_y.append(y_values[j])

dash = '-' * 35
print(dash)
title1 = f"The values that got back to themselves after being square rooted\
 and then squared {n_time} times"
print(title1)
print(dash)
print('{:<10s}{:>10s}'.format("x","y"))
print(dash)
for j in (range(len(special_values_x))):
    print('{:<18f}{:>10s}'.format(special_values_x[j],"{:.16f}".format(special_values_y[j])))

    
    
    
    
