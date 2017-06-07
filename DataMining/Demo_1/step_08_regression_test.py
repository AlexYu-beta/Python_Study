from numpy.random import rand
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from numpy import linspace, matrix
from pylab import plot, show


x = rand(40,1) # explanatory variable
y = x*x*x+rand(40,1)/5 # depentend variable

linreg = LinearRegression()
linreg.fit(x,y)

xx = linspace(0,1,40)
print mean_squared_error(linreg.predict(x),y)

plot(x,y,'o',xx,linreg.predict(matrix(xx).T),'--r')
show()



