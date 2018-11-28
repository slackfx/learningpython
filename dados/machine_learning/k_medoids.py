from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster.get_medoids()
cluster.process()
previsoes = cluster.get_clusters()
medoides = cluster.get_medoids()

v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, iris.data[:, 0:2], marker='*', markersize=15)
v.show()

lista_previsoes = []
lista_real = []
for i in range(len(previsoes)):
    for j in range(len(previsoes[i])):
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])

lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)

resultado = confusion_matrix(lista_real, lista_previsoes)