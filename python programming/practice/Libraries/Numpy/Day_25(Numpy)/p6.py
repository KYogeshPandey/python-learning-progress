# Plotting Graphs
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
# y=x
# y = x**2
# y = np.sin(x)
# y = x*np.log(x)
y = 1/(1+np.exp(-x))

 
plt.plot(x,y)
plt.show()