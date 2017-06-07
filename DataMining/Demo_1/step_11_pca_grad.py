from step_02_data_analyzer import data
from sklearn.decomposition import PCA


for i in range(1,5):
    pca = PCA(n_components=i)
    pca.fit(data)
    print sum(pca.explained_variance_ratio_) * 100,'%'