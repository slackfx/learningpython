from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

iris = datasets.load_iris()

r = skfuzzy.cmeans(data=iris.data.T, c=3, m=2, error=0.005, maxiter=1000, init=None)

previsoes_pct = r[1]

previsoes_pct[0][0]
previsoes_pct[1][0]
previsoes_pct[2][0]

previsoes = previsoes_pct.argmax(axis = 0)
resultado = confusion_matrix(iris.target, previsoes)