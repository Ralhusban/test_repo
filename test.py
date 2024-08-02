# This is a test and its now updated
# This is a change to the python test file
from matplotlib import pyplot as plt
import numpy as np

print(np.random.random())
x= np.arange(0,10,0.1)
plt.plot(x, np.exp(x))
plt.title("Exponential line")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()