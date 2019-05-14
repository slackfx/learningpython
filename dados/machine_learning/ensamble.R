install.packages('randomForest', dependencies = T)
library(randomForest)

#file.choose()
credito = read.csv("/home/fernando/projects/learningpython/dados/machine_learning/Credit.csv", sep=",", header=T)
amostra = sample(2, 1000, replace = T, prob=c(0.7, 0.3))
creditotreino = credito[amostra==1,]
creditoteste = credito[amostra==2,]

floresta = randomForest(class ~ ., data=creditotreino, ntree=100, importance = T)
floresta

varImpPlot(floresta)

previsao = predict(floresta, creditoteste)
confusao = table(previsao, creditoteste$class)
confusao

taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
taxaacerto
