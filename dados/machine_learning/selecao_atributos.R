library(e1071)
credito = read.csv(file.choose(), sep=",", header=T)
#maquina de vetor de suporte
amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))

creditotreino = credito[amostra==1,]
creditoteste = credito[amostra==2,]
modelo = svm(class ~ ., data=creditotreino)

modelo

predicao = predict(modelo, creditoteste)
confusao = table(creditoteste$class, predicao)
confusao
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
taxaacerto

install.packages("FSelector", dependencies = T)

library(FSelector)

random.forest.importance(class ~ ., credito)

modelo = svm(class ~ checking_status + duration + credit_history + purpose, data=creditotreino)
predicao = predict(modelo, creditoteste)
confusao = table(creditoteste$class, predicao)
confusao
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
taxaacerto
taxaerro
