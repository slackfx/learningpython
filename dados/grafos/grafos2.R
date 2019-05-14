library(igraph)

install.packages("igraphdata")
library(igraphdata)

data(Koenigsberg)
plot(Koenigsberg)
degree(Koenigsberg, mode="all")


data(kite)
plot(kite)

data(UKfaculty)
plot(UKfaculty)
comun = cluster_edge_betweenness(UKfaculty)
plot(comun, UKfaculty)
tkplot(UKfaculty)
