# probabilidade exata, por exemplo "2 no segundo dia"
# dpois(x, lambda)

# probabilidade menos que, ou mais que (lower.tail=F)
# ppois(x, lambda, lower.tail=F)

#####################################################

# média de 2 acidentes
# qual a probabilidade de ocorrer 3 ?

dpois(3, lambda=2)

# e a probabilidade de serem 3 ou menos acidentes ?

ppois(3, lambda=2)

# e mais de 3 acidentes ?

ppois(3, lambda = 2, lower.tail = F)
