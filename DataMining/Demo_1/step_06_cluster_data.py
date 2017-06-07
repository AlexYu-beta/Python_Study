from step_02_data_analyzer import data, target
from step_05_classify_data import t
from sklearn.cluster import KMeans
from sklearn.metrics import completeness_score, homogeneity_score


kmeans = KMeans(3, init='random') # initialization
kmeans.fit(data) # actual execution

c = kmeans.predict(data)


print completeness_score(t,c)
print homogeneity_score(t,c)