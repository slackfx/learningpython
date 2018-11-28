mean(AirPassengers)

mean(window(AirPassengers, star=c(1960,1), end=c(1960,12)))

install.packages("forecast")
library("forecast")

mediamovel = ma(AirPassengers, order=12)
plot(mediamovel)

previsao = forecast(mediamovel,h=12)
plot(previsao)

arima = auto.arima(AirPassengers)
arima

previsao = forecast(arima, h=12)
plot(previsao)

plot(forecast(AirPassengers,h=12))