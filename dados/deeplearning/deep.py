import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist


(x_treinamento, y_treinamento), (x_teste, y_teste) = mnist.load_data()
plt.imshow(x_treinamento[25], cmap='gray')
plt.title(y_treinamento[25])

x_treinamento = x_treinamento.reshape((len(x_treinamento), np.prod(x_treinamento.shape[1:])))
x_teste = x_teste.reshape((len(x_teste), np.prod(x_teste.shape[1:])))

x_treinamento = x_treinamento.astype('float32')
x_teste = x_teste.astype('float32')

x_treinamento /= 255
x_teste /= 255

y_treinamento = np_utils.to_categorical(y_treinamento, 10)
y_teste = np_utils.to_categorical(y_teste, 10)

modelo = Sequential()
modelo.add(Dense(units = 64, activation = 'relu', input_dim = 784))
modelo.add(Dropout(0.2))

modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))

modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))

modelo.add(Dense(units = 10, activation = 'softmax'))

modelo.summary()

modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
historico = modelo.fit(x_treinamento, y_treinamento, epochs = 20, validation_data = (x_teste, y_teste))

historico.history.keys()

plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_acc'])

previsoes = modelo.predict(x_teste)

y_teste_matriz = [np.argmax(t) for t in y_teste]
y_previsoes_matriz = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matriz, y_previsoes_matriz)

y_treinamento[20]
novo = x_treinamento[20]
novo = np.expand_dims(novo, axis = 0)
pred = modelo.predict(novo)
