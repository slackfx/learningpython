install.packages("neuralnet", dependencies=T)
library(neuralnet)

myiris = iris

myiris = cbind(myiris, myiris$Species=='setosa')
myiris = cbind(myiris, myiris$Species=='versicolor')
myiris = cbind(myiris, myiris$Species=='virginica')
head(myiris)
tail(myiris)

names(myiris)[6] = 'setosa'
names(myiris)[7] = 'versicolor'
names(myiris)[8] = 'virginica'
summary(myiris)


amostra = sample(2,150,replace=T,prob=c(0.7,0.3))
treino = myiris[amostra==1,]
teste = myiris[amostra==2,]

modelo = neuralnet(setosa + versicolor + virginica ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, treino, hidden=c(5,4))
plot(modelo)

testenet = compute(modelo,teste[,1:4])
testenet$net.result

resultado = as.data.frame(testenet$net.result)
names(resultado)[1] = 'setosa'
names(resultado)[2] = 'versicolor'
names(resultado)[3] = 'virginica'

resultado$class = colnames(resultado[,1:3])[max.col(resultado[,1:3], ties.method = 'first')]

resultado

confusao = table(resultado$class, teste$Species)
confusao
sum(diag(confusao) * 100 / sum(confusao))

 