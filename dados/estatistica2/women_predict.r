modelo = lm(height ~ weight, data=women)
predict(modelo, data.frame(weight=30))
