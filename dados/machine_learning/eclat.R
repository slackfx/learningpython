library(arules)

transacoes = read.transactions(file.choose(), format="basket", sep=",")
image(transacoes)

regras = eclat(transacoes, parameter = list(supp = 0.1, maxlen = 15))

inspect(regras)
plot(regras,method="graph", controle=list(type="items"))
 