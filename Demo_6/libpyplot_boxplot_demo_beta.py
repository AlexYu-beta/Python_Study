"""
this demo implements showing box plot of given(randomly generated) data by using library pyplot
"""
import matplotlib.pyplot as plt
import numpy as np

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)
# basic plot
plt.boxplot(data)       #show the plot
# notched plot
#plt.figure()            #create a new figure
#plt.boxplot(data,1)     #notch the plot
#plt.figure()
#plt.boxplot(data,2)
# change outlier point symbols
#plt.figure()
#plt.boxplot(data, 0, 'gD')
# horizontal boxes
#plt.figure()
#plt.boxplot(data, 0, 'rs', 0)
# change whisker length
plt.figure()
plt.boxplot(data, 0, 'rs', 0, 0.75)


# fake up some more data
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
data.shape = (-1, 1)
d2.shape = (-1, 1)
data = [data, d2, d2[::2, 0]]

# print the data generated above
print spread,center,flier_low,flier_high
print data
# multiple box plots on one figure
plt.figure()
plt.boxplot(data)

plt.show()