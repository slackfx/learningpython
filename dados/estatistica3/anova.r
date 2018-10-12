tratamento = read.csv(file.choose(), se=";", header=T)
fix(tratamento)

boxplot(tratamento$Horas ~ tratamento$Remedio)

an = aov(Horas ~ Remedio, data=tratamento)
summary(an)

tukey = TukeyHSD(an)
tukey

plot(tukey)
