novela = matrix(c(19,6,43,32), nrow = 2, byrow = T)
fix(novela)

rownames(novela) = c("Masculino", "Feminino")
colnames(novela) = c("Assiste", "NaoAssiste")

# qui quadrado
chisq.test(novela)
