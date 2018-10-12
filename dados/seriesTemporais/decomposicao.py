import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)

# Convertendo em Series
ts = base['#Passengers']
          
plt.plot(ts)

decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.plot(tendencia)
plt.plot(sazonal)
plt.plot(aleatorio)

plt.subplot(4,1,1)
plt.plot(ts, label='Original')
plt.legend(loc='best')

plt.subplot(4,1,2)
plt.plot(tendencia, label='Tendencia')
plt.legend(loc='best')

plt.subplot(4,1,3)
plt.plot(sazonal, label='Sazonalidade')
plt.legend(loc='best')

plt.subplot(4,1,4)
plt.plot(aleatorio, label='Aleatorio')
plt.legend(loc='best')
plt.tight_layout()

help(plt.subplot)