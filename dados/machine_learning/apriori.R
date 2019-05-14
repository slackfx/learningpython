install.packages("arules", dependencies = T)
install.packages("arulesViz", dependencies = T)

library(arules)

transacoes = read.transactions(file.choose(), format="basket", sep=",")
image(transacoes)
transacoes

regras = apriori(transacoes, parameter=list(support=0.5,conf=0.5))

inspect(regras)


library(arulesViz)
plot(regras)
plot(regras,method="graph", controle=list(type="items"))
