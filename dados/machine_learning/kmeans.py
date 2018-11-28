from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()

unicos, quantidade = np.unique(iris.target, return_counts = True)

cluster = KMeans(n_clusters = 3)
cluster.fit(iris.data)

centroids = cluster.cluster_centers_
previsoes = cluster.labels_

unicos2, quantidade2 = np.unique(previsoes, return_counts = True)

resultado = confusion_matrix(iris.target, previsoes)

 