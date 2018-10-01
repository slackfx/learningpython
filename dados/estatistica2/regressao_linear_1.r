dim(cars)
head(cars)
cor(cars)

modelo = lm(speed ~ dist, data=cars)
modelo
plot(modelo)

plot(speed ~ dist, data=cars)
abline(modelo)
modelo$coefficients

# calculando 
modelo$coefficients[1] + modelo$coefficients[2] * 22

# mesmo que acima
predict(modelo, data.frame(dist=22))

predict(modelo, data.frame(dist=50))

summary(modelo)

modelo$residuals

modelo$fitted.values
plot(modelo$fitted.values, cars$dist)
