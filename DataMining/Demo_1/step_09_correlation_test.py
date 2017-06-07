from step_02_data_analyzer import data
from numpy import corrcoef
from pylab import pcolor, colorbar, xticks, yticks, show
from numpy import arange
corr = corrcoef(data.T) # .T gives the transpose
print corr

pcolor(corr)
colorbar() # add
# arranging the names of the variables on the axis
xticks(arange(0.5,4.5),['sepal length',  'sepal width', 'petal length', 'petal width'],rotation=-20)
yticks(arange(0.5,4.5),['sepal length',  'sepal width', 'petal length', 'petal width'],rotation=-20)
show()
