install.packages('rpart', dependencies = TRUE)

library(rpart)

credito = read.csv(file.choose(), sep=",", header=T)
amostra = sample(2, 1000, replace = T, prob=c(0.7, 0.3))
creditotreino = credito[amostra==1,]
creditoteste = credito[amostra==2,]

arvore = rpart(class ~ ., data = creditotreino, method="class")
print(arvore)

plot(arvore)
text(arvore, use.n = T, all = T, cex=.8)

teste = predict(arvore, newdata=creditoteste)
teste

cred = cbind(creditoteste, teste)
fix(cred)

cred['Result'] = ifelse(cred$bad >= 0.5, "bad", "good")
fix(cred)

confusao = table(cred$class,cred$Result)
confusao

taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
taxaacerto
taxaerro
