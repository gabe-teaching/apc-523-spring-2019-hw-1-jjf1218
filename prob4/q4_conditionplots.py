## Plotting condition of functions vs condition of algorithms

import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0.05,1.0,100)
condf = ((x_values)/(np.exp(x_values)-1.0))
conda = (2.0-np.exp(x_values))/(x_values)

plt.scatter(x_values,condf,s=1,c="g")
title = f"(condf)(x) vs x"
plt.title(title)
plt.xlabel("x")
plt.ylabel("(condf)(x)")
plt.savefig('condf.png')

plt.scatter(x_values,conda,s=1,c="b")
title = f"(condA)(x) vs x"
plt.title(title)
plt.xlabel("x")
plt.ylabel("(condA)(x)")
plt.savefig('conda2.png')

