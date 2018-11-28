#install.packages("igraph", dependencies = T)
library(igraph)

grafo1 = graph(edges=c(1,2,2,3,3,4,4,1,1,1))
plot(grafo1)

# arestas bidirecionais (circular)
grafo2 = graph(edges=c(1,2,2,3,3,4,4,1,1,4,4,3,3,2,2,1))
plot(grafo2)

grafo3 = graph_from_literal(1-+2, 2-+3, 3++4, 4-+1)
plot(grafo3)

# grafo nao direcional
grafo4 = graph_from_literal(1-2, 2-3, 3-4, 4-1, 5)
plot(grafo4)


###############################################################

grafo2 = graph(edges=c(1,2,2,3,3,4,4,1))
plot(grafo2)
# Atributo D indicando que e direcional
grafo2

grafo3 = graph(edges=c(1,2,2,3,3,4,4,1), directed = F)
plot(grafo3)
# Atributo U indicando que nao e direcional
grafo3

# tera 10 vertices, se eu passar menos a api autocompleta com vertices isolados
grafo4 = graph(edges=c(1,2,2,3,3,4,4,1), directed = F, n = 10)
plot(grafo4)
grafo4

# isola os vertices F e G
grafo5 =  graph(edges=c("A", "B", "B", "C", "C", "D", "D", "E", "E", "A", "A", "C", "C", "B"), isolates = c("F", "G"))
plot(grafo5)
grafo5

###############################################################

grafo5 =  graph(edges=c("A", "B", "B", "C", "C", "D", "D", "E", "E", "A", "A", "C", "C", "B"), isolates = c("F", "G"))
plot(grafo5)
grafo5[] # vendo em forma de matriz
grafo5[1,] # primeira linha inteira
grafo5[,1] # primeira coluna inteira
grafo5[1, 1]

# busca informacoes do vertice
V(grafo5)$name

# busca informacoes dos edges
E(grafo5)

grafo7 = graph(edges=c("Fernando", "Pedro", "Jose", "Antonio", "Fernando", "Jose", "Fernando", "Antonio"))
plot(grafo7)
V(grafo7)$Peso = c(40, 30, 30, 25) # Cria o atributo Peso em V (o atributo nao existe na api)
vertex_attr(grafo7) # lendo atributos ja existentes e os que eu criei como acima

# Igual acima porem com edges
E(grafo7)$TipoAmizade = c("Amigo", "Inimigo", "Inimigo", "Amigo")
edge_attr(grafo7)

vertex_attr(grafo7)$Peso

E(grafo7)$weight = c(1, 2, 1, 3)
grafo7 # DNW- -> Direcional. Nomeado e com pesos(ponderado)

V(grafo7)$type = "Humanos"
grafo7 # DNWB -> Direcional. Nomeado, com pesos e com tipo

plot(grafo7)
