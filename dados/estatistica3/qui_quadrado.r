novela = matrix(c(19,6,43,32), nrow = 2, byrow = T)
fix(novela)

rownames(novela) = c("Masculino", "Feminino")
colnames(novela) = c("Assiste", "NaoAssiste")

# qui quadrado
chisq.test(novela)


jogo = matrix(c(41,34,18,7),nrow=2, byrow=T)
rownames(jogo) = c("Masculino","Feminino")
colnames(jogo) = c("Joga","NaoJoga")
chisq.test(jogo)