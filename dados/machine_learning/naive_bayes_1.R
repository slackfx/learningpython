#e1071 klaR -> pacote para Naive Bayes
#install.packages("e1071", dependencies=T)
library(e1071)

credito = read.csv(file.choose(), sep=",", header=T)
head(credito)
fix(credito)
dim(credito)

amostra = sample(2,1000,replace=T,prob=c(0.7,0.3))

creditotreino = credito[amostra==1,]
creditoteste = credito[amostra==2,]

dim(creditotreino)
dim(creditoteste)

# o ponto significa todas as colunas
modelo = naiveBayes(class ~ . , creditotreino)
modelo

predicao = predict(modelo, creditoteste)
predicao

confusao = table(creditoteste$class, predicao)
confusao

taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaacerto

taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
taxaerro

novocredito = read.csv(file.choose(), sep=",", header=T)
fix(novocredito)
dim(novocredito)

predict(modelo, novocredito)
