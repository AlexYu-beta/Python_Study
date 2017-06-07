from step_02_data_analyzer import data, target
from step_05_classify_data import t
from sklearn.decomposition import PCA
from pylab import plot, show, figure, subplot


pca = PCA(n_components=2)

pcad = pca.fit_transform(data)

figure()
subplot(211)
plot(pcad[target=='setosa',0],pcad[target=='setosa',1],'bo')
plot(pcad[target=='versicolor',0],pcad[target=='versicolor',1],'ro')
plot(pcad[target=='virginica',0],pcad[target=='virginica',1],'go')
print pca.explained_variance_ratio_
print 1-sum(pca.explained_variance_ratio_)
data_inv = pca.inverse_transform(pcad)
subplot(212)
plot(data[t==1,0],data[t==1,2],'bo')
plot(data[t==2,0],data[t==2,2],'ro')
plot(data[t==3,0],data[t==3,2],'go')
show()

print abs(sum(sum(data - data_inv)))

