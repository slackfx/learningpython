eleicao = read.csv(file.choose(), sep=";", header=T)
fix(eleicao)
plot(eleicao$DESPESAS, eleicao$SITUACAO)
summary(eleicao)
cor(eleicao$DESPESAS, eleicao$SITUACAO)

modelo = glm(SITUACAO ~ DESPESAS, data=eleicao, family = "binomial")
summary(modelo)

plot(eleicao$DESPESAS, eleicao$SITUACAO, col='red', pch=20)
points(eleicao$DESPESAS, modelo$fitted, pch=4)


prevereleicao = read.csv(file.choose(), sep=";", header=T)
fix(prevereleicao)

prevereleicao$RESULT = predict(modelo, newdata=prevereleicao, type="response")
prevereleicao$RESULT
